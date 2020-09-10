import time
import os

files1 = ["loading\loading_10.txt", "loading\loading_20.txt", "loading\loading_30.txt", "loading\loading_40.txt",
          "loading\loading_50.txt", "loading\loading_60.txt", "loading\loading_70.txt", "loading\loading_80.txt",
          "loading\loading_90.txt"]

files2 = ["loading\loading_99.txt", "loading\loading_100.txt"]

frames1 = []

frames2 = []


def loading_1():
    for name in files1:
        with open(name, "r", encoding="utf8") as f:
            frames1.append(f.readlines())
    for i in range(1):
        for frame in frames1:
            print("".join(frame))
            time.sleep(0.2)
            os.system("cls")

    loading_2()


def loading_2():
    for name in files2:
        with open(name, "r", encoding="utf8") as f:
            frames2.append(f.readlines())
    for i in range(1):
        for frame in frames2:
            print("".join(frame))
            time.sleep(1)
            os.system("cls")
