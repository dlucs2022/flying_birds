'''
写的配置使用数据库



'''

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///./flying.brids'
# SQLALCHEMY_DATABASE_URL='postgresql://root:FlyingBirdsDB@188.100.4.237:23306/postgres'  #mysql

engine = create_engine(
    # echo=True表示引擎将用repr()函数记录所有语句及其参数列表到日志
    # 由于SQLAlchemy是多线程，指定check_same_thread=False来让建立的对象任意线程都可使用。这个参数只在用SQLite数据库时设置
    SQLALCHEMY_DATABASE_URL, echo=True, connect_args={ }
)


sessionLocal = sessionmaker(bind=engine, autocommit=False, expire_on_commit=True)
# 创建基本映射

Base = declarative_base(name='Base')
