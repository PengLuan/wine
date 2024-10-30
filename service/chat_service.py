from peewee import DoesNotExist
from typing import Dict, Tuple, Optional, Union, List
from model.model import ChatLog, Wine
from service.base import save_chat
from common.custom_exception import CustomException, Status
from setting import ChatExample, StageMap, IntentMap, IntentFiledMap
from ai.ai_handler import AiHandler


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
        intent, wine = find_wine_name_and_intent(text)
        if last_chat is not None and intent < 0 < last_chat.intent:
            intent = last_chat.intent
        if isinstance(wine, list) and len(wine) == 0:
            wine = Wine.get_or_none(last_chat.wine_id)
        if intent > 0:
            # 直接回答问题
            if isinstance(wine, Wine):
                res_text = f"您所咨询的{wine.name}的{IntentMap.get(intent)}为{getattr(wine, IntentFiledMap.get(intent))}"
                return save_chat(token, text, res_text, StageMap.AskingOther.value, wine=wine, intent=intent)
            elif isinstance(wine, list) and len(wine) > 0:
                wine_text = ['、'.join([item.name for item in wine])]
                res_text = f"请从{wine_text}中选择您所要咨询的酒品"
                return save_chat(token, text, res_text, StageMap.ConfirmWine.value, intent=intent)
            else:
                res_text = ChatExample.HelloOnlyIntent.value.replace("**", IntentMap.get(intent))
                return save_chat(token, text, res_text, StageMap.ConfirmWine.value, intent=intent)
        else:
            if isinstance(wine, Wine):
                res_text = ChatExample.HelloOnlyWine.value.replace("**", wine.name)
                return save_chat(token, text, res_text, StageMap.ConfirmWine.value, wine=wine, intent=intent)
            elif isinstance(wine, list) and len(wine) > 0:
                wine_text = ['、'.join([item.name for item in wine])]
                res_text = f"请从{wine_text}中选择您所要咨询的酒品"
                return save_chat(token, text, res_text, StageMap.ConfirmWine.value, intent=intent)
            else:
                return save_chat(token, text, ChatExample.Hello.value, StageMap.Hello.value)
    else:
        raise CustomException(Status.PARAM_ERROR, "请您详细描述您的问题")


def find_wine_name_and_intent(text: str) -> Tuple[int, Union[Wine, List[Wine]]]:
    """
    分析酒品和 询问意图
    :param text:
    :return:
    """
    intent = AiHandler().classification_intent(text)
    wine_id = AiHandler().find_wine_id(text)
    return intent, wine_id
