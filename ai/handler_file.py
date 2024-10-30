import json


def main():
    file_to_write = "label,text"
    label_map = {"价格": 0, "口感": 1, "年份": 2}
    with open('classification.json', 'r') as f:
        data = json.load(f)
    for label in data:
        for text in data.get(label):
            file_to_write += f"\n{label_map.get(label)},{text}"
    with open('classification.csv', 'w') as f:
        f.write(file_to_write)


if __name__ == '__main__':
    main()
