import datetime

class DateFormat():
    
    @classmethod
    def convert_date(selk,date):
        return datetime.datetime.strftime(date,'%d/%m/%y')