#3/50 python 50 exercises: run timing

def run_timing():
    list = []
    avg = 0
    while True:
        times = input("Enter 10 km run time: ")
        if not times: #only runs for loop (aka avg calculator) when user presses enter
            for i in list: #for loop to take avg of times
                avg += i
            avg /= len(list)
            print(avg) #shit way of doing this tbh
            break
        else:
            list.append(float(times)) #if user does input a time, turn it into float and append to list

run_timing()