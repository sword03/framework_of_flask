DEBUG = True # 启动Flask的Debug模式
ENV = "development" # 缺省是production

import os
LOG_PATH = os.environ['HOME'] + '/.frameworkofflask/rest.log'
LOG_LEVEL = 'DEBUG'
