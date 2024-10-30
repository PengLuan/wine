from __future__ import annotations
import torch
from transformers import BertTokenizer, BertModel, AdamW
from transformers.optimization import get_scheduler
from datasets import load_dataset
token = BertTokenizer.from_pretrained('bert-base-chinese')
pretrained = BertModel.from_pretrained('bert-base-chinese')
for param in pretrained.parameters():
    param.requires_grad_(False)
pretrained.to('cpu')


class Dataset(torch.utils.data.Dataset):

    def __init__(self, split):
        self.dataset = load_dataset('csv', data_files='./classification.csv')[split]

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, i):
        text = self.dataset[i]['text']
        label = self.dataset[i]['label']
        return text, label


def collate_fn(data):
    sents = [i[0] for i in data]
    labels = [i[1] for i in data]
    data = token.batch_encode_plus(
        batch_text_or_text_pairs=sents, truncation=True, padding='max_length', max_length=50, return_tensors='pt',
        return_length=True)
    input_ids = data['input_ids']
    attention_mask = data['attention_mask']
    token_type_ids = data['token_type_ids']
    labels = torch.LongTensor(labels)
    input_ids = input_ids.to('cpu')
    attention_mask = attention_mask.to('cpu')
    token_type_ids = token_type_ids.to('cpu')
    labels = labels.to('cpu')
    return input_ids, attention_mask, token_type_ids, labels


class Model(torch.nn.Module):

    def __init__(self):
        super().__init__()
        self.rnn = torch.nn.GRU(input_size=768, hidden_size=768, batch_first=True)
        self.fc = torch.nn.Linear(768, 3)

    def forward(self, input_ids, attention_mask, token_type_ids):
        with torch.no_grad():
            out = pretrained(input_ids=input_ids, attention_mask=attention_mask, token_type_ids=token_type_ids)
        out, _ = self.rnn(out.last_hidden_state[:, 0])
        out = self.fc(out)
        out = out.softmax(dim=1)
        return out


def main():
    dataset = Dataset('train')
    loader = torch.utils.data.DataLoader(
        dataset=dataset, batch_size=16, collate_fn=collate_fn, shuffle=True, drop_last=True)
    model = Model()
    model.to('cpu')
    optimizer = AdamW(model.parameters(), lr=5e-4)
    criterion = torch.nn.CrossEntropyLoss()
    scheduler = get_scheduler(name='linear', num_warmup_steps=0, num_training_steps=len(loader), optimizer=optimizer)
    model.train()
    print(len(loader))
    for epoch in range(5):
        for i, (input_ids, attention_mask, token_type_ids, labels) in enumerate(loader):
            out = model(input_ids=input_ids, attention_mask=attention_mask, token_type_ids=token_type_ids)
            loss = criterion(out, labels)
            loss.backward()
            optimizer.step()
            scheduler.step()
            optimizer.zero_grad()
            out = out.argmax(dim=1)
            acc = (out == labels).sum().item() / len(labels)
            lr = optimizer.state_dict()['param_groups'][0]['lr']
            print(epoch, i, loss.item(), lr, acc)
    torch.save(model, 'classification.model')


def test():
    pass
    # # test
    # load_test = torch.utils.data.DataLoader(
    #     dataset=Dataset['train'], batch_size=32, collate_fn=collate_fn, shuffle=True, drop_last=True)
    # model.eval()
    # correct, total = 0, 0
    # for i, (input_ids, attention_mask, token_type_ids, labels) in enumerate(load_test):
    #     if i == 5:
    #         break
    #     print(i)
    #     with torch.no_grad():
    #         out = model(input_ids=input_ids, attention_mask=attention_mask, token_type_ids=token_type_ids)
    #     out = out.argmax(dim=1)
    #     correct += (out == labels).sum().item()
    #     total += len(labels)
    # print(correct / total, 'test_correct')


if __name__ == '__main__':
    main()
