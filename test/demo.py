def main():
    # 示例字典
    data = {
        'apple': 10,
        'banana': 5,
        'orange': 15,
        'grape': 20,
        'kiwi': 12
    }
    # 获取值排名前三的键
    top_keys = sorted(data, key=data.get, reverse=True)[:3]
    print("排名前三的键:", top_keys)


if __name__ == '__main__':
    main()
