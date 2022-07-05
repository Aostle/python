import datetime

from pip import main


def getYesterday():
    now = datetime.date.today()
    return now + datetime.timedelta(-1)

if __name__ == '__main__':
    print(getYesterday())