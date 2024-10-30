import torch
import gensim
from flask import Flask
from flask_cors import CORS
from common.decorator import http_base
from service.score_service import handler_score
from ai.train_classification import Model
from ai.ai_handler import AiHandler


def create_app():
    app = Flask(__name__)
    app.DEBUG = True
    CORS(app, resources=r"*")
    # 在应用创建时加载模型
    AiHandler.model = torch.load("data/classification.model", map_location="cpu")
    AiHandler.fasttext_model = gensim.models.fasttext.load_facebook_vectors('data/cc.zh.300.bin')

    @app.route("/chat", methods=['POST'])
    @http_base
    def chat(token, request_dict):
        # todo token 校验程序暂时忽略
        from service.chat_service import handler_chat
        return handler_chat(token, request_dict)

    @app.route("/score", methods=['POST'])
    @http_base
    def score(token, request_dict):
        # todo token 校验程序暂时忽略
        return handler_score(token, request_dict)

    return app


def main():
    app = create_app()
    app.run(port=5000, host="0.0.0.0")


if __name__ == '__main__':
    main()
