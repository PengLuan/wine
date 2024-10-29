from peewee import DoesNotExist
from typing import Dict, Tuple, Optional
from model.model import ChatLog
from service.base import save_chat
from common.custom_exception import CustomException, Status
from setting import ChatExample, StageMap


def handler_chat(token: str, request_dict: Dict[str, str]):
    """
    处理用户的对话语句
    :param token:
    :param request_dict:
    :return:
    """
    text = str(request_dict.get('text'))
    if text.strip():
        try:
            last_chat: Optional[ChatLog] = ChatLog.select().where(
                ChatLog.token == token).order_by(ChatLog.create_time.desc()).get()
        except DoesNotExist:
            last_chat = None
        else:
            if last_chat.stage == StageMap.ByeBye.value:
                last_chat = None  # 如果 bye bye 就重新开启一段信息
        intent, wine_id = find_wine_name_and_intent(text)
        if intent and wine_id:
            # 直接回答问题
            pass
        elif intent:
            # 直接回答问题
            pass
        elif wine_id:
            # 直接回答问题
            pass
        else:
            if last_chat:
                pass
            else:
                return save_chat(token, text, ChatExample.Hello.value, StageMap.Hello.value)
    else:
        raise CustomException(Status.PARAM_ERROR, "请您详细描述您的问题")


def find_wine_name_and_intent(text: str) -> Tuple[Optional[str], Optional[int]]:
    """
    分析酒品和 询问意图
    :param text:
    :return:
    """
    return None, None
