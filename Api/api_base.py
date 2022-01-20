import json

import requests
from loguru import logger


class ApiBase:
    def __init__(self):
        self.url = 'http://123.56.138.96:3012'
        self.header = {'Content-Type': 'application/json;charset=UTF-8',
                       'authorization': self.get_token()}

    @staticmethod
    def send(data):
        """
        接口发送请求
        :param data:request参数
        :return:将返回体转化为python合法数据
        """
        r_body = requests.request(**data)
        # print(json.dumps(r_body.json(), indent=4, ensure_ascii=False))
        logger.info(json.dumps(r_body.json(), indent=4, ensure_ascii=False))
        # print(r_body)
        return r_body

    def get_token(self):
        """
        获取令牌
        :return: 令牌
        """
        req = {'method': 'post',
               'url': self.url + '/api/ainews-user/user/login',
               'headers': {'Content-Type': 'application/json;charset=UTF-8'},
               'json': {"name": "lsj1", "password": "123123"}
               }
        return self.send(req).json().get('access_token')
