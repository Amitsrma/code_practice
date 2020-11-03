import time
import bisect

def median(arr, n):
    return (arr[n//2]+arr[n//2-1])/2 if n%2==0 else arr[(n+1)//2-1]


def check_process_flow1(expenditure, d):
    begin = expenditure[:d]
    begin.sort()
    to_check = expenditure[d]
    mid = median(begin, d)
    num_notification = 0
    if to_check >= 2*mid:
        print("notified!")
        num_notification += 1
    n = len(expenditure)
    hashes_s = {}
    for index, i in enumerate(begin):
        try:
            hashes_s[i].append(index)
        except:
            hashes_s[i] = [index,]
    start = 0
    for i in range(d+1, n):
        to_check = expenditure[i]
        to_add = expenditure[i-1]
        to_remove = expenditure[start]
        start += 1
        begin.pop(bisect.bisect_left(begin, to_remove))
        bisect.insort_left(begin, to_add)

        if median(begin, d)*2 <= to_check:
            num_notification += 1
    print(num_notification)


def activityNotifications(expenditure, d):
    begin = expenditure[:d]
    begin.sort()
    to_check = expenditure[d]
    mid = median(begin, d)
    num_notification = 0
    if to_check >= 2*mid:
        print("notified!")
        num_notification += 1
    n = len(expenditure)
    hashes_s = {}
    for index, i in enumerate(begin):
        try:
            hashes_s[i].append(index)
        except:
            hashes_s[i] = [index,]
    start = 0
    for i in range(d+1, n):
        to_check = expenditure[i]
        to_add = expenditure[i-1]
        to_remove = expenditure[start]
        start += 1
        begin.pop(bisect.bisect_left(begin, to_remove))
        bisect.insort_left(begin, to_add)

        if median(begin, d)*2 <= to_check:
            num_notification += 1

    return(num_notification)


def get_data(filename):
    with open(filename, 'r') as f:
        data = f.readlines()

    expenditures = [int(i) for i in data[1].strip().split()]

    d = int(data[0].strip().split()[1])

    return expenditures, d

test = 1

filenames = ["Fraudulent Activity Notifications 03.txt",
             'Fraudulent Activity Notifications 05.txt']

if test:
    for f in filenames:
        expenditure, d = get_data(f)
        start = time.time()
        print(activityNotifications(expenditure, d))
        print("Time taken:", time.time() - start)
        #break