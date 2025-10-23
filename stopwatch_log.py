import csv
import os
from stopwatchbase import stopwatch_save

activity, start_timer, end_timer, clean_duration = stopwatch_save()

file_exists = os.path.isfile("log.csv")

with open("log.csv", mode="a", newline="") as file:
    writer = csv.writer(file)

    if not file_exists:
        writer.writerow(["activity", "start_time", "end_time", "duration"])
        
    writer.writerow([activity, str(start_timer).split('.')[0], str(end_timer).split('.')[0], clean_duration])

print(f"🟢 Logged: {activity} ({clean_duration})")