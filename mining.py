#!/usr/bin/env python3

""" Docstring """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import json
import os.path


def read_json_from_file(file_name):
    with open(os.path.join(os.path.dirname(__file__), file_name)) as file_handle:
        file_contents = file_handle.read()

    return json.loads(file_contents)


class StockMiner:
    def __init__(self, stock_name, stock_file_name):
        self.stock_data = []
        self.monthly_averages_list = []
        self.stock_data = read_json_from_file(stock_file_name)
        self.dic_monthly = {}


    def month_averages(self):
        for daily_data in self.stock_data:
            if daily_data["Date"][0:7] in self.dic_monthly:
                self.dic_monthly[daily_data["Date"][0:7]][0] += daily_data["Close"]*daily_data["Volume"]
                self.dic_monthly[daily_data["Date"][0:7]][1] += daily_data["Volume"]
            else:
                self.dic_monthly[daily_data["Date"][0:7]] = [daily_data["Close"]*daily_data["Volume"], daily_data["Volume"]]

        for month in self.dic_monthly:
            self.monthly_averages_list.append((month.replace("-", "/"), round(self.dic_monthly[month][0] / self.dic_monthly[month][1], 2)))

        #dic key是date value是两个需要用来使用的值 看起来像这样  “2005/07”：［VC, V］

        # 每个月的average  append在一个list里面

    def six_best_months(self):
        for a in range(0, len(self.monthly_averages_list)-1):
            for i in range(0, len(self.monthly_averages_list)-1):
                if self.monthly_averages_list[i][1] < self.monthly_averages_list[i+1][1]:
                    self.monthly_averages_list[i],self.monthly_averages_list[i+1] = self.monthly_averages_list[i+1], self.monthly_averages_list[i]
        return self.monthly_averages_list[0:6]

    def six_worst_months(self):
        for a in range(0, len(self.monthly_averages_list)-1):
            for i in range(0, len(self.monthly_averages_list)-1):
                if self.monthly_averages_list[i][1] > self.monthly_averages_list[i+1][1]:
                    self.monthly_averages_list[i], self.monthly_averages_list[i+1] = self.monthly_averages_list[i+1], self.monthly_averages_list[i]
        return self.monthly_averages_list[0:6]


def read_stock_data(stock_name, stock_file_name):
    global stock
    stock = StockMiner(stock_name, stock_file_name)
    stock.month_averages()


def six_best_months():
    global stock
    return stock.six_best_months()


def six_worst_months():
    global stock
    return stock.six_worst_months()