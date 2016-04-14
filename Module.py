try:
    from urllib import urlretrieve
    from urllib import urlencode
except ImportError:
    from urllib.request import urlretrieve

    from urllib.parse import urlencode
#
import os
import csv
#Date,Open,High,Low,Close,Volume,Adj Close
class Share(object):

    def __init__(self, stock,start,finish):
        self.quote =stock
        self.start=start
        self.finish=finish
        self.params = urlencode({
        's': self.quote,
        'a': int(start[5:7]) - 1,
        'b': int(start[8:10]),
        'c': int(start[0:4]),
        'd': int(finish[5:7]) - 1,
        'e': int(finish[8:10]),
        'f': int(finish[0:4]),
        'g': 'd',
        'ignore': '.csv',
        })

    def getopen(self):
        try:
            url = 'http://real-chart.finance.yahoo.com/table.csv?%s' % self.params
            urlretrieve(url, '%s.csv' % self.quote)
            with open("%s.csv" % self.quote,'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    print(row['Open'] +' '+ row['Date'])
            os.remove('%s.csv' % self.quote)
        except:
            cleanup(self.quote)

    def gethigh(self):
        try:
            url = 'http://real-chart.finance.yahoo.com/table.csv?%s' % self.params
            urlretrieve(url, '%s.csv' % self.quote)
            with open("%s.csv" % self.quote,'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    print(row['High'] +' '+ row['Date'])
            os.remove('%s.csv' % self.quote)
        except:
            cleanup(self.quote)

    def getlow(self):
        try:
            url = 'http://real-chart.finance.yahoo.com/table.csv?%s' % self.params
            urlretrieve(url, '%s.csv' % self.quote)
            with open("%s.csv" % self.quote,'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    print(row['Low'] +' '+ row['Date'])
            os.remove('%s.csv' % self.quote)
        except:
            cleanup(self.quote)


    def getclose(self):
        try:
            url = 'http://real-chart.finance.yahoo.com/table.csv?%s' % self.params
            urlretrieve(url, '%s.csv' % self.quote)
            with open("%s.csv" % self.quote,'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    print(row['Close'] +' '+ row['Date'])
            os.remove('%s.csv' % self.quote)
        except:
            cleanup(self.quote)


    def getvolume(self):
        try:
            url = 'http://real-chart.finance.yahoo.com/table.csv?%s' % self.params
            urlretrieve(url, '%s.csv' % self.quote)
            with open("%s.csv" % self.quote,'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    print(row['Volume'] +' '+ row['Date'])
            os.remove('%s.csv' % self.quote)
        except:
            cleanup(self.quote)


    def getadj(self):
        try:
            url = 'http://real-chart.finance.yahoo.com/table.csv?%s' % self.params
            urlretrieve(url, '%s.csv' % self.quote)
            with open("%s.csv" % self.quote,'r') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    print(row['Adj Close'] +' '+ row['Date'])
            os.remove('%s.csv' % self.quote)
        except:
            cleanup(self.quote)

def cleanup(quote):
        print("Error")
        try: os.remove('%s.csv' % quote)
        except: pass