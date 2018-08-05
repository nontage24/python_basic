import time

if __name__ == '__main__':
    number = range(0,1000)

    t1 = time.time()

    for n in number:
        print(n)

    t2 = time.time()
    print("All time" ,t2-t1 , "sec")