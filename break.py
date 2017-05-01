import webbrowser
import time

count = 0

while(count < 3):
    count = count + 1
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/")
    print("The program opened at" + time.ctime())
