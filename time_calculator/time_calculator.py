def add_time(start, duration):
    
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
            new_period = start_period
    else: 
        new_minute = duration_minute - (60-start_minute)
        if start_hour + duration_hour < 12:
            new_hour = start_hour + duration_hour
            new_period = start_period
        elif start_hour + duration_hour >= 12 and start_hour + duration_hour < 24:
            new_hour = duration_hour - (12-start_hour) + 1
            if start_period == 'PM':
                new_period = 'AM'
            elif start_period == 'AM':
                new_period = 'PM'
        elif start_hour + duration_hour == 24:
            new_hour = 1
            new_period = start_period

    if new_minute < 10:
        new_minute = '0'+str(new_minute)

    new_time = str(new_hour)+':'+str(new_minute)+' '+new_period

    return(new_time)

print(add_time('11:30 AM', '2:32'))
