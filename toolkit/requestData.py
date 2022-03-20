# -*- coding:utf-8 -*-

from urllib import response
import requests

class GetColorNumData(object):
    def __init__(self) -> None:
        self.url = "http://www.cwl.gov.cn/cwl_admin/front/cwlkj/search/kjxx/findDrawNotice?name=ssq&issueCount=&issueStart=2018001&issueEnd=2018050&dayStart=&dayEnd="

    def get_all_history_data(self):
        pass

    def get_one_history_data(self):
        response = requests.get(self.url)
        return response.text

    def get_new_data(self):
        pass