import json
from typing import Dict, Union
from service.base import save_chat
from setting import ScoreMap, ChatExample, StageMap


def handler_score(token: str, request_dict: Dict[str, Union[int, str]]) -> str:
    """
    打分信息
    :param token:
    :param request_dict:
    :return:
    """
    star = request_dict.get('star', ScoreMap.Good.value)  # 默认好评
    if star not in [item.value for item in ScoreMap]:
        star = ScoreMap.Good.value
    desc = request_dict.get('desc', '')
    # 获取 酒品ID
    # 落库 更改状态
    # 祝贺词
    return save_chat(token, json.dumps(request_dict), ChatExample.ByeBye.value, StageMap.ByeBye.value)

