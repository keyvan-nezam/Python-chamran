import msvcrt
import time

while True:
    print("Hello! Press Q to stop the program.")

    time.sleep(1)

    if msvcrt.kbhit():
        key = msvcrt.getch().decode("utf-8").lower()

        if key == "q":
            print("Program stopped. Goodbye!")
            break
