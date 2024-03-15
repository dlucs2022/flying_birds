import os

# 数据库连接
SQLALCHEMY_DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://root:FlyingBirdsDB@188.100.4.237:23306/flying_birds"
)
development = True
