# coding=utf-8
from environs import Env
import platform

env = Env()
# 拨号间隔
ADSL_CYCLE = 60

# 拨号出错重试间隔
ADSL_ERROR_CYCLE = 1

# 删除代理到重新获取代理间�?
DEL_TO_GET = 60

# ADSL命令,adsl-stop;adsl-start �?.bashrc
# alias adsl-start=pppoe-start
# alias adsl-stop=pppoe-stop
#�? subprocess.getstatusoutput(ADSL_BASH) 会发生错�?，只能执�?/bin/sh �?的命�?
ADSL_BASH = 'pppoe-stop;pppoe-start'

# 代理运�?��??�?
PROXY_PORT = 8877

# 客户�?�?一标识
CLIENT_NAME = platform.node()

# 拨号网卡
ADSL_IFNAME = 'ppp0'

# Redis数据库IP
REDIS_HOST = env.str('REDIS_HOST', 'r-t4nehwc2cu8cr9mmhcpd.redis.singapore.rds.aliyuncs.com')

# Redis数据库密�?, 如无则填None
REDIS_PASSWORD = env.str('REDIS_PASSWORD', 'Wasd1234')

# Redis数据库�??�?
REDIS_PORT = 6379

# 代理池键�?
PROXY_KEY = 'adsl'

# 测试URL
TEST_URL = 'http://www.google.com/recaptcha/api.js'

# 测试超时时间
TEST_TIMEOUT = 1

# API�?�?
API_PORT = 8000
