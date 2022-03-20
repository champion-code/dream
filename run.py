# -*- coding:utf-8 -*-
from toolkit.requestData import GetColorNumData

if __name__ == "__main__":
    colorNumData = GetColorNumData()
    print(colorNumData.get_one_history_data())