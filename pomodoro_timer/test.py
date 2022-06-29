import time

# x = datetime.datetime.now().strftime("%X")
#
#
# print(x)
def countdown(t):
    while t != 0:
        time.sleep(1)
        t -= 1
    return 0

t = int(input("How many secs: "))
countdown(t)
