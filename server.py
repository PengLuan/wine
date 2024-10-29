from flask import Flask
from flask_cors import CORS
from common.decorator import http_base
from service.score_service import handler_score
from service.chat_service import handler_chat
app = Flask('__main__')
CORS(app, resources=r"*")


@app.route("/chat", methods=['POST'])
@http_base
def chat(token, request_dict):
    # todo token 校验程序暂时忽略
    return handler_chat(token, request_dict)


@app.route("/score", methods=['POST'])
@http_base
def score(token, request_dict):
    # todo token 校验程序暂时忽略
    return handler_score(token, request_dict)


if __name__ == '__main__':
    app.DEBUG = True
    app.run(port=5000, host="0.0.0.0")


