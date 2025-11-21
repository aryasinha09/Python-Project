import time

def set_timer(seconds):
    print(f"Timer set for {seconds} seconds.")
    time.sleep(seconds)
    print("⏳ Time's up!")
