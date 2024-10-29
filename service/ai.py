from transformers import pipeline

# 加载意图分类和NER模型
intent_classifier = pipeline("text-classification", model="bert-base-uncased")
ner = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")


def main():
    # 示例用户输入
    user_input = "请告诉我关于2015年份的红酒口感如何？"

    # 意图分类
    intent = intent_classifier(user_input)[0]['label']
    print("Intent:", intent)

    # 实体识别
    entities = ner(user_input)
    print("Entities:", entities)


if __name__ == '__main__':
    main()

