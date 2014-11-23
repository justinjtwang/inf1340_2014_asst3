#!/usr/bin/env python3

""" Docstring """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import json
import datetime


class StockMiner:
    def __init__(self, stock_data, monthly_averages,dic_daily):
        self.stock_data = []
        self.monthly_averages_list = []
        self.dic_monthly = {}

    def read_stock_data(self,stock_name, stock_file_name):
        self.stock_data = read_json_from_file(stock_file_name)

    def get_monthly_averages(self, dic_monthly, monthly_averages_list):
        for daily_data in self.stock_data:
            if daily_data["Date"][0:7] in dic_monthly.key():
                dic_monthly[daily_data["Date"][0:7]][0] += daily_data["Close"]*daily_data["Volume"]
                dic_monthly[daily_data["Date"][0:7]][1] += daily_data["Volume"]
            else:
                dic_monthly[daily_data["Date"][0:7]] = [daily_data["Close"]*daily_data["Volume"], daily_data["Volume"]]

        for month in dic_monthly:
            monthly_averages_list.append(month.replace("-", "/"), (dic_monthly[month][0] / dic_monthly[month][1]))

        #dic key是date value是两个需要用来使用的值 看起来像这样  “2005/07”：［VC, V］

        # 每个月的average  append在一个list里面
        return monthly_averages_list

    def six_best_months(self,monthly_averages_list):
        for i in range(0,len(monthly_averages_list)):
            if monthly_averages_list[i][1] < monthly_averages_list[i+1][1]:
                monthly_averages_list[i],monthly_averages_list[i+1] = monthly_averages_list[i+1], monthly_averages_list[i]
        return monthly_averages_list[0:6]

    def six_worst_months(self,monthly_averages_list):
        for i in range(0,len(monthly_averages_list)):
            if monthly_averages_list[i][1] > monthly_averages_list[i+1][1]:
                monthly_averages_list[i],monthly_averages_list[i+1] = monthly_averages_list[i+1], monthly_averages_list[i]
        return monthly_averages_list[0:6]

def read_json_from_file(file_name):
    with open(file_name) as file_handle:
        file_contents = file_handle.read()
    return json.loads(file_contents)

