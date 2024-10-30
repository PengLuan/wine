import json
import datetime
from typing import Dict, Union
from model.model import Wine, Score
from service.base import save_chat
from setting import ScoreMap, ChatExample, StageMap
from common.custom_exception import CustomException, Status


def handler_score(token: str, request_dict: Dict[str, Union[int, str]]) -> Dict[str, Union[str, int]]:
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
    wine_id = request_dict.get('wine_id', '')
    wine_obj = Wine.get_or_none(Wine.id == wine_id)
    if wine_obj is not None:
        wine_obj: Wine = wine_obj
        # 落库 更改状态
        already_count = Score.select().where(Score.token == token, Score.wine_id == wine_obj.id).count()
        if already_count > 0:
            pre_text = f"您已经对{wine_obj.name}提交过评价，"
            return save_chat(
                token, json.dumps(request_dict), pre_text + ChatExample.ByeBye.value, StageMap.ByeBye.value)
        else:
            score_obj = Score(token=token, star=star, desc=desc, wine_id=wine_id, create_time=datetime.datetime.now())
            score_obj.save()
        # 祝贺词
        return save_chat(token, json.dumps(request_dict), ChatExample.ByeBye.value, StageMap.ByeBye.value)
    else:
        raise CustomException(Status.NOT_EXIST, "您选择打分的酒品不存在")
