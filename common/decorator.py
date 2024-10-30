import time
import json
import functools
import traceback
from flask import request
from common.log_func import LOG
from common.custom_exception import CustomException


def http_base(func) -> callable:
    """
    基础装饰器
    :param func:
    :return:
    """
    @functools.wraps(func)
    def real_wrapper(*arg, **kwargs) -> callable:
        client_ip = request.remote_addr
        x_forwarded_for = request.headers.get('X-Forwarded-For')
        if x_forwarded_for:
            client_ip = x_forwarded_for.split(',')[0]
        t1 = time.time()
        result = {}
        try:
            params = request.form if request.method == 'POST' else request.args
            token = params.get('session_id')
            data = func(token, params)
        except CustomException as e:
            result = {'data': None, 'msg': e.msg, 'code': e.code}
        except Exception as e:
            LOG.exception(traceback.format_exc())
            result = {'data': None, 'msg': str(e), 'code': -1}
        else:
            result = {'data': data, 'msg': "成功", 'code': 0}
        finally:
            t2 = time.time()
            try:
                param = json.dumps(request.form)
            except Exception as e:
                param = str(e)
            _str = f'耗时：{func.__module__}{func.__name__} 入参: {param} 用时 {round((t2 - t1), 2)} s ip:{client_ip}'
            LOG.info(_str)
            return result
    return real_wrapper


def timer(func):
    def wrapper(*arg, **kw):
        t1 = time.time()
        try:
            res = func(*arg, **kw)
        except Exception as e:
            t2 = time.time()
            LOG.exception(f'报错了：{func.__module__}{func.__name__} 用时 {round((t2 - t1), 4)} s')
            raise e
        else:
            t2 = time.time()
            LOG.info(f'耗时：{func.__module__}{func.__name__} 用时 {round((t2 - t1), 4)} s')
        return res

    return wrapper
