from abc import ABC
from peewee import Model, CharField, IntegerField, DateTimeField, TextField
from playhouse.shortcuts import ReconnectMixin
from playhouse.pool import PooledMySQLDatabase
from setting import DB_NAME, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD


class ReconnectMySQLDatabase(ReconnectMixin, PooledMySQLDatabase, ABC):
    _instance = None

    @staticmethod
    def get_db_instance():
        if not ReconnectMySQLDatabase._instance:
            ReconnectMySQLDatabase._instance = ReconnectMySQLDatabase(
                database=DB_NAME,
                host=DB_HOST,
                port=DB_PORT,
                user=DB_USER,
                passwd=DB_PASSWORD,
                charset='utf8',
                max_connections=500,
                stale_timeout=600,
                # sql_mode='NO_AUTO_CREATE_USER'
            )
        return ReconnectMySQLDatabase._instance


class BaseModel(Model):

    class Meta:
        database = ReconnectMySQLDatabase.get_db_instance()


class ChatLog(BaseModel):
    id = IntegerField(unique=True)
    token = CharField()
    create_time = DateTimeField()
    stage = IntegerField()
    user_content = TextField()
    flat_content = TextField()
    wine_id = IntegerField()
    intent = IntegerField()

    class Meta:
        database = ReconnectMySQLDatabase.get_db_instance()
        db_table = 'chat_log'


class Wine(BaseModel):
    id = IntegerField(unique=True)
    name = CharField()
    year = IntegerField()
    create_time = DateTimeField()
    desc = TextField()  # 口感等描述信息
    price = IntegerField()  # 以分为单位

    class Meta:
        database = ReconnectMySQLDatabase.get_db_instance()
        db_table = 'wine'


class Score(BaseModel):
    id = IntegerField(unique=True)
    token = CharField()
    star = IntegerField()
    desc = TextField()
    wine_id = IntegerField()
    create_time = DateTimeField()

    class Meta:
        database = ReconnectMySQLDatabase.get_db_instance()
        db_table = 'score'


