from datetime import date

CHRISTMAS = date(date.today().year, 12, 25)

#get today's date
def getToday():
    return date.today()

#find how many days between today and christmas
def daysUntil(today):
    until = CHRISTMAS - today
    return until.days
    
#shows days until in a progress bar
def progressBar(until):
    progress_bar_length = 60 
    percent = (365 - until) / 365 
    progress = int(progress_bar_length * percent)
    leftover = progress_bar_length - progress

    progress_bar = str(round((percent*100), 1)) + '% |' + '█'*progress + '-'*leftover + '|' 
    return progress_bar

def main():
    today = getToday()
    until = daysUntil(today)
    progress = progressBar(until)
    
    if until == 0:
        message = (f'CHRISTMAS LOADED!\n\nMERRY CHRISTMAS!\n{progress}') 
    else:
        message = (f'Christmas Loading...\n\n{until} days until Christmas!\n{progress}') 

    return message
    

if __name__ == '__main__':
    print(main())
