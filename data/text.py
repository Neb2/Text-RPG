import time
import sys


def typewriter(text):
    words = text
    for char in words:
        time.sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()
