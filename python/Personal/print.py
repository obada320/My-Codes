import time

while True:
    wordin = input()
    if wordin == '':
        print("invalid")
    else:
        time_to = 4 + 1
        for i in range(0,time_to,1):
            print(i,"/",time_to - 1)
            time.sleep(1)
        print(wordin)

    exit1 = input("Exit? Y/N : ")
    if exit1[0] == "y" or exit1[0] == "Y":
        print("ok Goodbye")
        time.sleep(3)
        exit()
    else:
        9 or 8