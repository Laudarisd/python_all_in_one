def add_time(start, duration, day = None):
    starting_hour, form = start.split()
    start_hrs, start_min = starting_hour.split(':')

    dur_hrs, dur_min = duration.split(':')

    total_hrs = int(start_hrs) + int(dur_hrs)
    total_min = int(start_min) + int(dur_min)
    day_ = 0
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    day_ = total_hrs / 24
    if day_ < 1:
        day_ = 0
    if day_ > 1:
        day_ = int(day_)

    if total_min > 59:
        total_hrs += 1
        total_min %= 60
    while total_hrs > 11:
        total_hrs -= 12
        if form == "AM":
            form = 'PM'
            day_ -=1
        else:
            form = "AM"
            day_ += 1

    if total_hrs == 0:
        total_hrs = 12

    time = f"{total_hrs}:{str(total_min).zfill(2)} {form}"

    if day:
        current_day_index = days.index(day.title())
        next_day_index = int((current_day_index + day_) % 7)
        time += f", {days[next_day_index]}"
    if day_ == 1:
        time += " (next day)"
    if day_ > 1:
        time += f" ({int(day_)} days later)"
    return time
