import datetime
import random

def print_lunch_break(current_time, lunch_duration):
    print("\tLunch: {} - {}".format(current_time.strftime('%I:%M %p'), (current_time + lunch_duration).strftime('%I:%M %p')))
    return current_time + lunch_duration

def generate_day_timetable(current_time, end_time):
    labs = ["applied physics Lab ", " electrical and electronics engineering Lab ", "python programming Lab ", "Engineering Drawing Lab "]
    theory_periods = ["Theory 1", "Theory 2", "Theory 3", "Theory 4"]
    other_periods = ["Library", "Sports", "DI classes", "Remedial"]

    lab_period_duration = datetime.timedelta(hours=2, minutes=40)
    theory_period_duration = datetime.timedelta(minutes=50)
    other_period_duration = datetime.timedelta(minutes=50)
    break_duration = datetime.timedelta(minutes=10)
    lunch_duration = datetime.timedelta(minutes=40)

    random.shuffle(labs)
    random.shuffle(theory_periods)
    random.shuffle(other_periods)

    num_labs = random.randint(1, min(2, len(labs)))
    num_theory_periods = random.randint(1, min(3, len(theory_periods)))
    num_other_periods = random.randint(1, min(3, len(other_periods)))

    for lab in labs[:num_labs]:
        if current_time.time() >= datetime.time(12, 0):
            current_time = print_lunch_break(current_time, lunch_duration)

        if current_time > end_time:
            break

        print(f"\t{lab}: {current_time.strftime('%I:%M %p')} - {(current_time + lab_period_duration).strftime('%I:%M %p')}")
        current_time += lab_period_duration

    current_time += break_duration

    for period in theory_periods[:num_theory_periods]:
        if current_time.time() >= datetime.time(12, 0):
            current_time = print_lunch_break(current_time, lunch_duration)

        if current_time > end_time:
            break

        print(f"\t{period}: {current_time.strftime('%I:%M %p')} - {(current_time + theory_period_duration).strftime('%I:%M %p')}")
        current_time += theory_period_duration

    for period in other_periods[:num_other_periods]:
        if current_time.time() >= datetime.time(12, 0):
            current_time = print_lunch_break(current_time, lunch_duration)

        if current_time > end_time:
            break

        print(f"\t{period}: {current_time.strftime('%I:%M %p')} - {(current_time + other_period_duration).strftime('%I:%M %p')}")
        current_time += other_period_duration

    current_time += lunch_duration
    current_time = current_time.replace(hour=9, minute=20)

    return current_time

def create_timetable():
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    start_time = datetime.datetime(2023, 7, 31, 9, 20)
    end_time = datetime.datetime(2023, 7, 31, 16, 0)  # 4:00 PM

    for day in days_of_week:
        print(day)
        start_time = generate_day_timetable(start_time, end_time)
        print()

if __name__ == "__main__":
    create_timetable()