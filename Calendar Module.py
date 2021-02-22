import calendar

def dayReturn(month, day, year):
    return str(calendar.day_name[calendar.weekday(year, month, day)]).upper()
if __name__ == "__main__":
    
    month, day, year = input().split(' ')
    
    print(dayReturn(int(month), int(day), int(year)))     
