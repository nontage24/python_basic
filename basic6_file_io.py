
if __name__ == '__main__':
    massage = input("Enter Massgae : ")
    file = open('test.txt','w')
    file.write(massage)
    file.close()

    read = open('test.txt','r')
    msg = read.read()
    read.close()
    print("Read: ", msg)
