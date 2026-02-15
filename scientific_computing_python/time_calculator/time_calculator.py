def add_time(start, duration, week_day=False):
    
    start_period = start.split(' ')[1]
    start_hour = int(start.split(' ')[0].split(':')[0])
    start_minute = int(start.split(' ')[0].split(':')[1])
    
    duration_hour = int(duration.split(':')[0])
    duration_minute = int(duration.split(':')[1])

    if start_minute + duration_minute < 60:
        new_minute = start_minute + duration_minute
        if start_hour + duration_hour < 12:
            new_hour = start_hour + duration_hour
            new_period = start_period
        elif start_hour + duration_hour == 12:
            new_hour = start_hour + duration_hour
            if duration_hour == 0:
                new_period = start_period
            else:
                if start_period == 'PM':
                    new_period = 'AM'
                elif start_period == 'AM':
                    new_period = 'PM'
        elif start_hour + duration_hour > 12 and start_hour + duration_hour < 24:
            new_hour = duration_hour - (12-start_hour)
            if start_period == 'PM':
                new_period = 'AM'
            elif start_period == 'AM':
                new_period = 'PM'
        elif start_hour + duration_hour == 24:
            new_hour = 12
            if duration_hour%24 == 0:
                new_period = start_period
            else:
                if start_period == 'PM':
                    new_period = 'AM'
                elif start_period == 'AM':
                    new_period = 'PM'
        elif start_hour + duration_hour > 24:
            new_hour_24 = (start_hour + duration_hour)%24
            if new_hour_24 == 0:
                new_hour = 12
                if start_period == 'PM':
                    new_period = 'AM'
                elif start_period == 'AM':
                    new_period = 'PM'
            elif new_hour_24 < 12:
                new_hour = new_hour_24
                new_period = start_period
            elif new_hour_24 == 12:
                new_hour = new_hour_24
                new_period = start_period
            elif new_hour_24 > 12:
                new_hour = new_hour_24 - 12
                if start_period == 'PM':
                    new_period = 'AM'
                elif start_period == 'AM':
                    new_period = 'PM'
    else: 
        new_minute = duration_minute - (60-start_minute)
        sum_hour = start_hour + duration_hour + 1 
        if sum_hour < 12:
            new_hour = sum_hour
            new_period = start_period
        elif sum_hour == 12:
            new_hour = sum_hour
            if start_period == 'PM':
                new_period = 'AM'
            elif start_period == 'AM':
                new_period = 'PM'
        elif sum_hour > 12 and sum_hour < 24:
            new_hour = sum_hour - 12
            if start_period == 'PM':
                new_period = 'AM'
            elif start_period == 'AM':
                new_period = 'PM'
        elif sum_hour == 24:
            new_hour = 12
            if start_period == 'PM':
                new_period = 'AM'
            elif start_period == 'AM':
                new_period = 'PM'
        elif sum_hour > 24:
            new_hour_24 = sum_hour % 24
            if new_hour_24 == 0:
                new_hour = 12
                if start_period == 'PM':
                    new_period = 'AM'
                elif start_period == 'AM':
                    new_period = 'PM'
            elif new_hour_24 < 12:
                new_hour = new_hour_24
                new_period = start_period
            elif new_hour_24 == 12:
                new_hour = new_hour_24
                if start_period == 'PM':
                    new_period = 'AM'
                elif start_period == 'AM':
                    new_period = 'PM'
            elif new_hour_24 > 12:
                new_hour = new_hour_24 - 12
                if start_period == 'PM':
                    new_period = 'AM'
                elif start_period == 'AM':
                    new_period = 'PM'

    if new_minute < 10:
        new_minute = '0'+str(new_minute)

    new_time = str(new_hour)+':'+str(new_minute)+' '+new_period
    
    if start_period == 'AM':
        days_later = (start_hour + duration_hour + (start_minute + duration_minute)//60)//24
    elif start_period == 'PM':
        if start_hour == 12:
            days_later = (duration_hour + (start_minute + duration_minute)//60)//24
        else:
            days_later = (12 + start_hour + duration_hour + (start_minute + duration_minute)//60)//24

    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f' ({days_later} days later)'

    week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    if week_day:
        week_day = week_day.capitalize()
        start_index = week_days.index(week_day)
        if days_later < 1:
            new_index = start_index
            new_day = week_days[new_index]
            new_time += f', {new_day}'  
        if days_later == 1:
            new_index = (start_index + days_later)%7
            new_day = week_days[new_index]
            new_time = str(new_hour)+':'+str(new_minute)+' '+new_period + f', {new_day}' + " (next day)"
        if days_later > 1:
            new_index = (start_index + days_later)%7
            new_day = week_days[new_index]
            new_time = str(new_hour)+':'+str(new_minute)+' '+new_period + f', {new_day}' + f' ({days_later} days later)'

    return(new_time)

print(add_time('11:59 AM', '0:01', 'Monday'))
