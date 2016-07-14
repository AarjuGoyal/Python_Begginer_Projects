import webbrowser
import time

count = 0
print("this program started on " + time.ctime() )
while(count < 3):
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=CdFIKU53KEU")
    count = count + 1
    
