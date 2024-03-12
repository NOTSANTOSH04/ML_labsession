list = [2,7,4,1,3,6]
length = len(list)             #length of the list
count = 0                 #variable to store the number of pairs that satisifes the condition
for i in range(length):
    for j in range(i+1 ,length):
        if list[i] + list[j] == 10:         #checking condition if pair sum equals target
            count += 1
print(count)