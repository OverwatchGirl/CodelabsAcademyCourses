# Python program to print Even Numbers in given range
list = []  
start, end = 1, 299
  
# iterating each number in list
for num in range(start, end + 1):
      
    # checking condition
    if num % 2 == 0:
        #print(num, end = " ")
        list.append(num)

for i in list :
    print(len(list))
    print(i**2)

print(57 in list)