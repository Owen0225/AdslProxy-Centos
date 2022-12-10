# coding=utf-8
import re
import time
# import requests
import httpx
# from requests.exceptions import ConnectionError, ReadTimeout
# from adslproxy.db import RedisClient
from adslproxy.config import *
import platform
import logging
import os

if platform.python_version().startswith('2.'):
    import commands as subprocess
elif platform.python_version().startswith('3.'):
    import subprocess
else:
    raise ValueError('python version must be 2 or 3')
logging.basicConfig(
        level=logging.DEBUG,  # 定义输出到文件的log级别，大于此级别的都被输出
        format='%(asctime)s  %(filename)s : %(levelname)s  %(message)s',  # 定义输出log的格式
        datefmt='%Y-%m-%d %A %H:%M:%S',  # 时间
        filename=os.path.join(os.getcwd(),'log.txt'),  # log文件名
        filemode='w')

class Sender():
    def get_ip(self, ifname=ADSL_IFNAME):
        """
        获取本机IP
        :param ifname: 网卡名称
        :return:
        """
        # (status, output) = subprocess.getstatusoutput('ifconfig')
        # if status == 0:
        #     pattern = re.compile(ifname + '.*?inet.*?(\d+\.\d+\.\d+\.\d+).*?Mask', re.S)
        #     result = re.search(pattern, output)
        #     if result:
        #         ip = result.group(1)
        #         return ip
        try:
            response = httpx.get('http://ifconfig.me/ip', timeout=5)
            if response.status_code == 200:
                return response.text.strip()
        except:
            return ''


    def test_proxy(self, proxy):
        """
        测试代理
        :param proxy: 代理
        :return: 测试结果
        """
        try:
            response = httpx.get(TEST_URL, proxies={
                'http': 'http://' + proxy,
                'https': 'https://' + proxy
            }, timeout=TEST_TIMEOUT)
            if response.status_code == 200:
                return True
        except:
            return False

    def remove_proxy(self):
        """
        移除代理
        :return: None
        """
        # self.redis = RedisClient()
        # self.redis.remove(CLIENT_NAME)
        logging.debug('Successfully Removed Proxy')

    def set_proxy(self, proxy):
        """
        设置代理
        :param proxy: 代理
        :return: None
        """
        # self.redis = RedisClient()
        # if self.redis.set(CLIENT_NAME, proxy):
        #     print('Successfully Set Proxy', proxy)
        response = httpx.get('http://43.135.87.43:8899/Put?ip='+proxy, timeout=5)
        if response.status_code == 200:
            # print('Successfully Set Proxy', proxy)
            logging.debug('Successfully Set Proxy')
            return True
        else:
            return False



    def adsl(self):
        """
        拨号主进程
        :return: None
        """
        while True:
            logging.debug('ADSL Start, Remove Proxy, Please wait')
            time.sleep(DEL_TO_GET)
            (status, output) = subprocess.getstatusoutput(ADSL_BASH)
            if status == 0:
                logging.debug('ADSL Successfully')
                ip = self.get_ip()
                if ip:
                    logging.debug('Now IP', ip)
                    logging.debug('Testing Proxy, Please Wait')
                    proxy = '{ip}:{port}'.format(ip=ip, port=PROXY_PORT)
                    logging.debug('ProxyInfo', proxy)
                    if self.test_proxy(proxy):
                        logging.debug('Valid Proxy')
                        self.set_proxy(proxy)
                        logging.debug('Sleeping')
                        time.sleep(ADSL_CYCLE)
                    else:
                        logging.debug('Invalid Proxy')
                else:
                    logging.debug('Get IP Failed, Re Dialing')
                    time.sleep(ADSL_ERROR_CYCLE)
            else:
                logging.debug('ADSL Failed, Please Check')
                time.sleep(ADSL_ERROR_CYCLE)


def run():
    sender = Sender()
    sender.adsl()


if __name__ == '__main__':
    run()
