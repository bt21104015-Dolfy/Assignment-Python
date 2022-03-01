############################################################################
##QUESTION1
def hanoi(n, fro, to, aux):
    if n == 0:
        return

    hanoi(n-1, fro, aux, to)
    print(f"move Disk {n} from {fro} to {to}")
    hanoi(n-1, aux, to, fro)
    
#calling function for 3 disks
hanoi(3, 'P', 'Q', 'R')
print("")

############################################################################

##QUESTION2
n = int(input("Enter the number of rows in Pascal's Triangle:"))
#recursive method
print("\n Using recursion: ")

def pascal(n, originaln = n):
    if n == 0:
        return

    pascal(n-1, originaln)
    print(' ' * (originaln - n), end='')

    entry = 1
    for i in range(1, n+1):
        print(entry, end=' ')

        entry = entry * (n-i) // i
    print()


pascal(n)

#iteration method
print("\n Using Iterative method: ")
for line in range(1, n+1):

    print(' ' * (n - line), end='')

    x = 1
    for i in range(1, line +1):
        print(x, end=' ')

        x = x*(line - i)//i

    print()
print("")

############################################################################

##QUESTION3
print("(a).")
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
c = a%b
d = a//b
print("Remainder is: ", c)
print("Quotient is: ", d)

print("\n(b).")
if (c != 0):
    if (d != 0):
        print("Both the values are non-zero")
    else:
        print("One value is zero")
else:
    if (d != 0):
        print("One value is zero")
    else:
        print("Both the values are zero")
print("\n(c) and (d).")
set1 = set()
for i in range(4,7):
    f = c+i
    g = d+i
    if (f>4):
        set1.add(f)
        print(set1)
    if (g>4):
        set1.add(g)
        print(set1)

print(set1)
print("\n(e).")
set2 = frozenset(set1)
print("Immutable set: ", frozenset(set1))
print("\n(f).")
print("Largest value in the set: ", max(set2))
k = max(set2)
print("Hash value: ", hash(k))
print("")

############################################################################

##QUESTION4
class Student:
    def __init__(self, student, sid):
        self.name = student
        self.sid = sid

    def __del__(self):
        print("Object destroyed")

student1 = Student("Dolfy", 21104015)
print("Object created.")

print(f"The name of the student is {student1.name} and SID is {student1.sid}.")

del student1
print(student1)
print("")

############################################################################

##QUESTION5
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

employee1 = Employee("Mehak", 40000)
employee2 = Employee("Ashok", 50000)
employee3 = Employee("Viren", 60000)

employee1.salary = 70000
print(f"(a). The updated salary of the employee {employee1.name} is {employee1.salary}")

del employee3
print("(b). Employee Viren record deleted.", end='')

print(" ")

############################################################################

##QUESTION6
word = input("Enter the first word: ")

testword = input("\nEnter a new meaningful word to test your friendship: ")

def count_in_dict(word):
    count = {}
    list1 = list(word)

    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count

if count_in_dict(word) != count_in_dict(testword):
    print("The letters aren't exact, friendship is fake!!")

def userinput():
    ans = input("\nDoes the word make any sense? (y or n)\n")

    if ans == 'y':
        print("The friends pass the friendship test!!")
    elif ans == 'n':
        print("The word doesn't have a meaning, friendhsip is fake!!\n")
    else:
        print("Invalid input, Try again!")
        userinput()

userinput()
print("")

############################################################################