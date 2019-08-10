import time

i = 0

def loadingSequence(t):
    print("Loading", end="")
    for i in range(4):
        time.sleep(t/4)
        print(".", end="")

def closingSequence(t):
    print("Quitting", end="")
    for i in range(4):
        time.sleep(t/4)
        print(".", end="")