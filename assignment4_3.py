def num_devide3(lim):
    count = 0
    for x in range(1,lim + 1):
        if x % 3 == 0:
            count +=1
    return count

while True:
    input_num = input("Enter a number: ")
    if input_num == "done":
        print("bye!!")
        break
    try:
        num = int(input_num)
        if num >= 0:
            print("numbers divisible by 3 among numbers from 1 to",num,":",num_devide3(num))
        else:
            print("Enter a positive integer")
    except:
        print("Enter a positive integer")
