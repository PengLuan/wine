import datetime
from model.model import ChatLog


def save_chat(token: str, user_content: str, flat_content: str, stage: int) -> str:
    """
    保存会话信息
    :param token: 用户凭证
    :param user_content: 用户发送的内容
    :param flat_content: 平台返回的内容
    :param stage: 当前的问答阶段
    :return:
    """
    chat_obj = ChatLog(
        token=token, create_time=datetime.datetime.now(), stage=stage, user_content=user_content,
        flat_content=flat_content)
    chat_obj.save()
    return flat_content
