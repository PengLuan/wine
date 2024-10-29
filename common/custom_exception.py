from enum import Enum


class Status(Enum):
    """
    异常状态的枚举类
    """
    SUCCESS = 200, "SUCCESS"
    NEED_LOGIN = 401, "需要登陆"
    PARAM_ERROR = 400, "参数错误"
    NOT_EXIST = 404, "信息不存在"
    CANT_EDIT = 403, "不允许修改"
    THIRD_ERROR = 488, "对接第三方失败"
    NOW_IS_VIP = 489, "已经是会员"
    IS_RUNNING = 490, "任务执行中请稍候"
    NOT_IS_RUNNING = 491, "无正在执行的任务"
    MASTER_USER_FULL = 492, "家庭组满了"
    TRY_TOO_MANY_TINES = 493, "尝试次数过多"
    ADD_GROUP_OVER_TIMES = 494, "该账号已加入太多家庭套餐，不能激活！请使用其他账号激活或联系客服！"
    NOT_SUPPORT = 495, "功能暂未实现"


class CustomException(Exception):

    def __init__(self, status: Status, msg: str = None):
        """
        :return 报错状态枚举
        """
        super().__init__(self)
        self.code = status.value[0]
        self.msg = status.value[-1] if msg is None else msg

    def __str__(self) -> str:
        """
        :return 报错信息
        """
        return repr(f"{self.code}:{self.msg}")
