import datetime
import json

import requests


class DingRobot:
    def __init__(self):
        self.allure = "http://admin:123456@47.93.88.94:9000/job/Api_test/allure/widgets/suites.json"
        self.ding = 'https://oapi.dingtalk.com/robot/send?access_token=' \
                    '3f7a97e1b19df92bfb87b6d38728c9278c42eb2b4c0d8544b8959e83317f35aa'
        self.error = self.get_allure_error()

    def get_allure_error(self):
        jenkins_data = requests.get(self.allure).json()
        case_error = jenkins_data["items"][0]["statistic"]["failed"]
        return case_error

    def send_report(self):
        if self.error > 0:
            headers = {"Content-Type": "application/json;charset=utf-8"}
            content = {
                "msgtype": "link",
                "link": {
                    "text": "郑浩：账号admin,密码123456",
                    "title": "~" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    "picUrl": "",
                    "messageUrl": "http://jenkisn5:123456@47.93.88.94:9000/job/Api_test/allure/"
                }
            }
            response = requests.post(self.ding, headers=headers, data=json.dumps(content))
        else:
            print('无报错')


if __name__ == '__main__':
    DingRobot().send_report()
