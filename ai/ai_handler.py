import pickle
import torch
import gensim
from LAC import LAC
from typing import Union, List
from transformers import BertTokenizer
from model.model import Wine
from ai.train_classification import Model
from common.func import change_to_int, change_to_float


class AiHandler:
    CLASS_LIMIT = 0.6
    CLASS_EMPTY = -1
    SAME_LIMIT = 0.9
    SAME_LIMIT_BASE = 0.1
    effect_map = ['ORG', 'LOC', 'n']  # 12
    token = BertTokenizer.from_pretrained('bert-base-chinese')
    model = torch.load("./data/classification.model", map_location="cpu", pickle_module=pickle)
    fasttext_model = gensim.models.fasttext.load_facebook_vectors('data/cc.zh.300.bin')
    model.eval()

    def __init__(self):
        pass

    def encoder(self, text: str):
        data = self.token.encode_plus(
            text=text, truncation=True, padding='max_length', max_length=50, return_tensors='pt',
            return_length=True)
        input_ids = data['input_ids']
        attention_mask = data['attention_mask']
        token_type_ids = data['token_type_ids']
        input_ids = input_ids.to('cpu')
        attention_mask = attention_mask.to('cpu')
        token_type_ids = token_type_ids.to('cpu')
        return input_ids, attention_mask, token_type_ids

    def classification_intent(self, text) -> int:
        input_ids, attention_mask, token_type_ids = self.encoder(text)
        with torch.no_grad():
            out = self.model(input_ids=input_ids, attention_mask=attention_mask, token_type_ids=token_type_ids)
        out_max = out.argmax(dim=1)
        if change_to_float(max(out.reshape(-1))) >= self.CLASS_LIMIT:
            return change_to_int(out_max, self.CLASS_EMPTY)
        else:
            return self.CLASS_EMPTY

    def find_wine_id(self, text: str) -> Union[List[Wine], Wine]:
        # 加载意图分类和NER模型
        # 示例用户输入
        # 实体识别
        res = LAC(mode='lac').run(text)
        one_word = ''
        one_word_list = list()
        for word, word_type in zip(res[0], res[1]):
            if word_type in self.effect_map:
                one_word += word
            else:
                one_word_list.append(one_word)
                one_word = ''
        if one_word.strip():
            one_word_list.append(one_word)
        effect_dict = dict()
        wine_dict = dict()
        for item in Wine.select():
            item: Wine = item
            wine_dict.update({item.id: item})
            for word in one_word_list:
                same_score = self.fasttext_model.similarity(word, item.name)
                if same_score >= self.SAME_LIMIT:
                    return item
                elif same_score > self.SAME_LIMIT_BASE:
                    effect_dict.update({Wine.id: same_score})
        result = list()
        if effect_dict:
            for key in sorted(effect_dict, key=effect_dict.get, reverse=True)[:3]:
                result.append(wine_dict.get(key))
        return result


def main():
    AiHandler().find_wine_id('AAA')


if __name__ == '__main__':
    main()
