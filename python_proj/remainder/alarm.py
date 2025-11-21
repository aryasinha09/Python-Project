import time
import winsound

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    while True:
        current = time.strftime("%H:%M")
        if current == alarm_time:
            print("⏰ Alarm ringing!")
            winsound.Beep(1000, 3000)
            break
        time.sleep(1)
