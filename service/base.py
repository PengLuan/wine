import datetime
from typing import Optional, Dict, Union
from model.model import ChatLog


def save_chat(token: str, user_content: str, flat_content: str, stage: int, wine_id: Optional[int] = None,
              intent: Optional[int] = None) -> Dict[str, Union[int, str]]:
    """
    保存会话信息
    :param token: 用户凭证
    :param user_content: 用户发送的内容
    :param flat_content: 平台返回的内容
    :param stage: 当前的问答阶段
    :param wine_id
    :param intent
    :return:
    """
    chat_obj = ChatLog(
        token=token, create_time=datetime.datetime.now(), stage=stage, user_content=user_content,
        flat_content=flat_content)
    if wine_id is not None:
        chat_obj.wine_id = wine_id
    if intent is not None:
        chat_obj.intent = intent
    chat_obj.save()
    return {'flat_content': flat_content, 'wine_id': wine_id}
