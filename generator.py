import datetime
import numpy
import pandas as pd


class Data:

    def __init__(self, rate, num_days):
        self.m = rate
        self.num_days = num_days - 1
        self.date_list = []
        self.df = pd.DataFrame({"Дата": [], "Курс $": [], "Биржа": []})
        self.stock_markets = ['СПБ Биржа', 'Мосбиржа',
                              ' New York Stock Exchange (NYSE)',
                              'National Association of Securities Dealers Automated Quotation (NASDAQ)',
                              'Japan Exchange Group(JPX)',
                              'Shanghai Stock Exchange (SSE)',
                              'Euronext']
        self.create_date_list()

    def create_date_list(self):
        a = datetime.date.today()
        for x in range(self.num_days, -1, -1):
            self.date_list.append(a - datetime.timedelta(days=x))

        for date in self.date_list:
            for s in self.stock_markets:
                if len(self.df.index) <= len(self.stock_markets):
                    k = numpy.round(numpy.random.normal(loc=self.m, scale=self.m*0.5/3), 2)
                else:
                    k = self.df['Курс $'].loc[len(self.df.index)-len(self.stock_markets)]
                    k = numpy.round(numpy.random.normal(loc=k, scale=k*0.1/3), 2)
                self.df.loc[len(self.df.index)] = [date, k, s]

        self.df = self.df.groupby('Дата').mean(numeric_only=True).round(2)

    def show_data(self, rows=None):
        if rows is None:
            rows = ['Дата', 'Курс $', 'Биржа']
        print(self.df[rows])

    def get_data(self):
        return self.df



