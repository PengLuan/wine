from typing import Any, Optional, Union


def change_to_int(original: Any, default_value: Optional[int] = 0) -> int:
    """
    类型转换转换为整数类型
    :param original 原始入参
    :param default_value 默认值
    :return 转换后的整数
    """
    try:
        result = int(float(original))
    except (ValueError, TypeError):
        return default_value
    else:
        return result


def change_to_float(original: Union[str, bytes, float], default_value: Optional[float] = 0) -> Optional[float]:
    """
    转换浮点型的安全方法
    :param original 转换前的内容
    :param default_value 默认值
    :return 转换后的浮点值
    """
    try:
        result = float(original)
    except (ValueError, TypeError):
        return default_value
    else:
        return result
