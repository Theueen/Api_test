# todo:舆情分组接口测试

from Api.api_base import ApiBase


class AiGrouping(ApiBase):

    def more(self):
        """
        快讯”more“按钮
        :return: 无
        """
        req = {'method': 'post',
               'url': self.url + '/api/ainews-espy/api/opinion/flash-news',
               'json': {"start_time": "2021-12-20T17:24:05",
                        "end_time": "2021-12-26T17:24:05",
                        "page": 1,
                        "pagesize": 20
                        },
               'headers': self.header
               }
        self.send(req)

    def create_group(self, group_name):
        """
        创建分组
        :param group_name: 新建的分组名
        :return: 无
        """
        req = {'method': 'post',
               'url': self.url + '/api/ainews-user/company-group/create',
               'json': {"name": group_name},
               'headers': self.header
               }
        self.send(req)

    def inquire_group_id(self, group_name):
        """
        查询分组id
        :param group_name: 查询的分组名
        :return: 查询分组的id
        """
        req = {'method': 'get',
               'url': self.url + '/api/ainews-user/company-group/user-custom-group',
               'params': {'page': 1,
                          'per_page': 10,
                          'start_time': '2021-12-28',
                          'end_time': '2022-01-14'},
               'headers': self.header
               }
        for i in range(len(self.send(req))):
            if self.send(req)[i].get('name') == group_name:
                return self.send(req)[i].get('id')

    def add_company_to_group(self, cp_code, group_name):
        """
        添加公司到分组
        :param cp_code: 添加公司的股票代码
        :param group_name: 要添加公司的分组名
        :return: 无
        """
        req = {'method': 'post',
               'url': self.url + '/api/ainews-user/company-group/company-create',
               'json': {"company_code": cp_code,
                        "group_id": self.inquire_group_id(group_name)},
               'headers': self.header
               }
        self.send(req)

    def del_group(self, group_name):
        """
        删除分组
        :param group_name: 要删除的分组名
        :return: 无
        """
        req = {'method': 'get',
               'url': self.url + '/api/ainews-user/company-group/delete',
               'params': {"id": self.inquire_group_id(group_name)},
               'headers': self.header
               }
        self.send(req)
