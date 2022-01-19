import pytest

from Api.api_grouping import AiGrouping


class TestAiGrouping:
    def setup_class(self):
        self.group = AiGrouping()

    def test_more(self):
        self.group.more()

    @pytest.mark.parametrize('group_name',
                             [
                                 'zh_test_1',
                                 'zh_test_2'
                             ], ids=
                             [
                                 'create_group_1',
                                 'create_group_2'
                             ])
    def test_create_group(self, group_name):
        self.group.create_group(group_name)

    @pytest.mark.parametrize('group_name',
                             [
                                 'zh_test_1',
                                 'zh_test_2'
                             ], ids=
                             [
                                 'inquire_group_1',
                                 'inquire_group_2'
                             ])
    def test_inquire_group_id(self, group_name):
        self.group.inquire_group_id(group_name)

    @pytest.mark.parametrize('cp_code,group_name',
                             [
                                 ('000001', 'zh_test_1'),
                                 ('000002', 'zh_test_1'),
                                 ('000004', 'zh_test_2'),
                                 ('000005', 'zh_test_2')
                             ], ids=
                             [
                                 'add_company_to_group_1',
                                 'add_company_to_group_2',
                                 'add_company_to_group_3',
                                 'add_company_to_group_4'
                             ])
    def test_add_company_to_group(self, cp_code, group_name):
        self.group.add_company_to_group(cp_code, group_name)

    @pytest.mark.parametrize('group_name',
                             [
                                 'zh_test_1',
                                 'zh_test_2'
                             ], ids=
                             [
                                 'del_group_1',
                                 'del_group_2'
                             ])
    def test_del_group(self, group_name):
        self.group.del_group(group_name)
