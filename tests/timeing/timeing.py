import time

def current_milli_time():
    return round(time.time() * 1000)

print(current_milli_time())
time.sleep(1)
print(current_milli_time())
print(current_milli_time())