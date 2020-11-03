import time
import bisect

def median(arr, n):
    return (arr[n//2]+arr[n//2-1])/2 if n%2==0 else arr[(n+1)//2-1]

def activityNotifications(expenditure, d):
    hashes_s = {}
    to_check = expenditure[d]
    n = len(expenditure)
    num_notification = 0
    
    begin = expenditure[:d]
    begin.sort()

    if to_check >= 2*median(begin, d):
        num_notification += 1
    
    for index, i in enumerate(begin):
        try:
            hashes_s[i].append(index)
        except:
            hashes_s[i] = [index,]
    
    for i in range(d+1, n):
        to_check = expenditure[i]
        to_add = expenditure[i-1]
        to_remove = expenditure[start]
        #using bisect to add element to a previously sorted array
        #this is faster
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
