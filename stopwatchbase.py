from datetime import datetime 

def stopwatch():
    
    start_timer = datetime.now() 
    print(f"Started at: {str(start_timer).split(".")[0]}") ## start_timer.strftime("%H:%M:%S") 

    input("Press ENTER to stop the timer...")

    end_time = datetime.now()
    print(f"Ended at: {str(end_time).split(".")[0]}")

    duration = end_time - start_timer
    clean_duration = str(duration).split(".")[0]
    print(f"Duration: {clean_duration}")

stopwatch()