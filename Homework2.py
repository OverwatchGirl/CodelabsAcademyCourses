import string

file = open('CLA_homework\student_names.txt', 'r+')

#one_variable = file.read()

#print(one_variable)

file.write("Emma stone" + "\n" + "Glenn Close" + "\n" + "Joel Fry" + "\n" + "Mark Strong")
file.close()

file = open('CLA_homework\student_names.txt', 'r+') 
#print(file.read())

n = 2

for i in range(n) :
    print(file.readline())

for line in (file.readlines() [-n:]):
    print(line)

print("Emma Watson" in file.read())

alphabet = list(string.ascii_lowercase)
print(alphabet)

print(len(alphabet))
for i in range(len(alphabet)) :
    path = 'CLA_homework' +'\\' + alphabet[i] +'.txt'
    print(path)
    with open(path, 'w') : pass

 