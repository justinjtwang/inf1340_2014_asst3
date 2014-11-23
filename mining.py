#!/usr/bin/env python3

"""
 Sort out the six best and six worst months with a Google stock's historical prices file
Assignment 3,INF1340 Fall 2014
"""

__author__ = 'Xiwen Zhou, Juntian Wang,Susan Sim'
__email__ = "xw.zhou@mail.utoronto.ca,,ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import json
import os.path


def read_json_from_file(file_name):
    """
    Gets data into a list from json file
    :param file_name: json file
    :return: a list, contains data to be sorted
    """
    with open(os.path.join(os.path.dirname(__file__), file_name)) as file_handle:
        file_contents = file_handle.read()

    return json.loads(file_contents)


class StockMiner:
    def __init__(self, stock_file_name):
        """
        Initializes variables,constructor for class StockMiner
        :param stock_file_name:json file
        """
        self.stock_data = []
        self.monthly_averages_list = []
        self.stock_data = read_json_from_file(stock_file_name)
        self.dic_monthly = {}

    def month_averages(self):
        """
        Calculates monthly averages close prices
        :return:a list of tuples,containing month and corresponding average
        """
        for daily_data in self.stock_data:
            if daily_data["Date"][0:7] in self.dic_monthly:
                #Sorts data on monthly basis while adding up for average calculation later
                self.dic_monthly[daily_data["Date"][0:7]][0] += daily_data["Close"]*daily_data["Volume"]
                self.dic_monthly[daily_data["Date"][0:7]][1] += daily_data["Volume"]
            else:
                self.dic_monthly[daily_data["Date"][0:7]] = [daily_data["Close"]*daily_data["Volume"], daily_data["Volume"]]

        for month in self.dic_monthly:
            self.monthly_averages_list.append((month.replace("-", "/"), round(self.dic_monthly[month][0] / self.dic_monthly[month][1], 2)))
            #Caculates monthly averages and put them into a list
            #Changes string - into / according to test file
            #Round up to 2 decimals

    def six_best_months(self):
        """
        Sorts out six months with highest averages
        :return:A list of tuple, containing month and corresponding average
        """
        #Sort the list from highest to lowest then return the first six
        for a in range(0, len(self.monthly_averages_list)-1):
            for i in range(0, len(self.monthly_averages_list)-1):
                if self.monthly_averages_list[i][1] < self.monthly_averages_list[i+1][1]:
                    self.monthly_averages_list[i], self.monthly_averages_list[i+1] = self.monthly_averages_list[i+1], self.monthly_averages_list[i]
        return self.monthly_averages_list[0:6]


    def six_worst_months(self):
        """
         Sorts out six months with lowest averages
        :return:A list of tuple, containing month and corresponding average
        """
        #Sort the list from lowest to highest then return the first six
        for a in range(0, len(self.monthly_averages_list)-1):
            for i in range(0, len(self.monthly_averages_list)-1):
                if self.monthly_averages_list[i][1] > self.monthly_averages_list[i+1][1]:
                    self.monthly_averages_list[i], self.monthly_averages_list[i+1] = self.monthly_averages_list[i+1], self.monthly_averages_list[i]
        return self.monthly_averages_list[0:6]


def read_stock_data(stock_file_name):
    """
    Manage data on monthly basis
    :param stock_file_name: json file
    """
    global stock
    stock = StockMiner(stock_file_name)
    stock.month_averages()


def six_best_months():
    """
    Sorts out six months with highest averages for calling in test file
    :return:A list of tuple, containing month and corresponding average
    """
    global stock
    return stock.six_best_months()


def six_worst_months():
    """
    Sorts out six months with lowest averages for calling in test file
    :return:A list of tuple, containing month and corresponding average
    """
    global stock
    return stock.six_worst_months()