import os
from datetime import timedelta


class BaseConfig:  # 基本配置
    SECRET_KEY = os.urandom(24)
    # 不設定的話Flask會使用緩存的js跟css不會更新
    SEND_FILE_MAX_AGE_DEFAULT = timedelta(seconds=1)
    # 中文設置
    JSON_AS_ASCII = False


class DevelopmentConfig(BaseConfig):
    DEBUG = False
    WTF_CSRF_CHECK_DEFAULT = True
    WTF_CSRF_SSL_STRICT = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost:3306/test"
    # use docker compose use this
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@mysql:3306/tttest"


class TestingConfig(BaseConfig):
    TESTING = True


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
}
