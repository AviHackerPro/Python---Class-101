import time
seconds = int(input("Enter the Time in number of Seconds"))

def count_timer(sec):
    while sec > 0 : 
        mins = int(sec/60)
        secs = int(sec%60)
        timer = f'{mins}:{secs}'
        print(timer)
        time.sleep(1)
        sec-=1
    print("Time Up!")

count_timer(seconds)