class db_config:
    db_type = 'mysql'
    db_host = 'localhost'
    db_port = 3306
    db_user = 'blogadmin'
    db_password = 'admin123'
    db_name = 'blogdb'

    # 数据库连接字符串
    SQLALCHEMY_DATABASE_URI =f'{db_type}+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
    # SQLALCHEMY_DATABASE_URI='mysql+pymysql://blogadmin:admin123@localhost:3306/blogdb'

    # 是否追踪数据库的修改
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 是否自动提交
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    # 是否自动刷新
    SQLALCHEMY_ECHO = True

    # 是否自动回收连接
    SQLALCHEMY_POOL_RECYCLE = 60

    # 连接池大小
    SQLALCHEMY_POOL_SIZE = 100

    # 连接池超时时间
    SQLALCHEMY_POOL_TIMEOUT = 10

    # 连接池空闲时间

    SQLALCHEMY_MAX_OVERFLOW = 10

    # 是否使用懒加载
    SQLALCHEMY_USE_LAZY_LOADING = True

    # 是否使用异步
    SQLALCHEMY_USE_ASYNC = True



