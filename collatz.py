def collatz(num):
    steps = []
    while num != 1:
        if num % 2 == 0:
            num = num/2
        else:
            num = (3*num) + 1
        steps.append(int(num))
    return steps

start=1
while True:
    print("Start: {} | Steps: {}".format(start, collatz(start)))
    start+=1


