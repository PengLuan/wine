import gensim
from LAC import LAC
from model.model import Wine
print('AAA')
fasttext_file = '../data/cc.zh.300.bin'
print('BBB')
fasttext_model = gensim.models.fasttext.load_facebook_vectors(fasttext_file)
print('CCC')


def main():
    effect_map = ['ORG', 'LOC', 'n']
    # 加载意图分类和NER模型
    # 示例用户输入
    user_input = "碧尚男爵的年份是多少"
    # 实体识别
    res = LAC(mode='lac').run(user_input)
    one_word = ''
    one_word_list = list()
    for word, word_type in zip(res[0], res[1]):
        if word_type in effect_map:
            one_word += word
        else:
            one_word_list.append(one_word)
            one_word = ''
    if one_word:
        one_word_list.append(one_word)
    for item in Wine.select():
        item: Wine = item
        for word in one_word_list:
            print(item.name, word, fasttext_model.similarity(word, item.name))


if __name__ == '__main__':
    main()
