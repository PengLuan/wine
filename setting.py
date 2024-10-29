from enum import Enum


DB_NAME = "wine"
DB_HOST = "127.0.0.1"
DB_PORT = 3306
DB_USER = "root"
DB_PASSWORD = "mm123456"


class StageMap(Enum):

    Hello = 1  # 招呼阶段
    ConfirmWine = 2  # 确认酒品
    AskingOther = 3  # 其他询问意图
    Score = 4  # 打分阶段
    ByeBye = 5  # 收尾阶段


class ScoreMap(Enum):
    VeryGood = 5
    Good = 4
    Common = 3
    Bad = 2
    VeryBad = 1


class ChatExample(Enum):
    Hello = "我们这边是一家酒庄，请问您这边有什么问题需要询问的？"
    HelloOnlyWine = "请问您需要对**这款酒的哪个方面进行了解呢？"
    HelloOnlyIntent = "请问哪款酒**方面的信息呢？"
    ByeBye = "感谢您的评价，祝您生活愉快！"
