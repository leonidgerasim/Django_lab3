import datetime
import numpy


class Data:

    def __init__(self, m):
        self.m = m
        self.dateList = []
        self.stock_markets = ['СПБ Биржа', 'Мосбиржа',
                              ' New York Stock Exchange (NYSE)',
                              'National Association of Securities Dealers Automated Quotation (NASDAQ)',
                              'Japan Exchange Group(JPX)',
                              'Shanghai Stock Exchange (SSE)',
                              'Euronext']

    def create_date_list(self):
        a = datetime.datetime.today()
        numdays = 10
        for x in range(0, numdays):
            self.dateList.append(a - datetime.timedelta(days=x))




