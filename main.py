import os
import time
from win10toast import ToastNotifier
import pyttsx3
import pathlib


def main():
    tst = ToastNotifier()

    #setting icon path
    a = pathlib.Path().resolve()
    ico = "alram.ico"

    full_path = os.path.join(a, ico)

    tst.show_toast("Back To Work!", "Time to go-to work!!", duration=10, icon_path=full_path)

    #change the interger to modify the delay
    time.sleep(10)


if __name__ == '__main__':
    while True:
        main()
