

########################################################################


###Answer1

str = "Python is a case sensitive language"
#(a) finding length of string
print(len(str))

#(b) reversing the string
print(str[::-1])

#(c) slicing and storing in new string
str1 = str[10:27]
print(str1)

#(d) replacing substring
print(str.replace("a case sensitive", "object oriented"))

#(e) finding the index of 'a'
print(str.index("a"))

#(f) removing white spaes
print(str.replace(" ", ""))


########################################################################


###Answer2

# store details
Name = "Dolfy"
SID = 21104015
DepN = "Electrical"
CGPA = 9.9

#printing required results
print("Hey,", Name, "Here!")
print("My SID is", SID)
print("I am from", DepN, "department and my CGPA is", CGPA)


########################################################################


##Answer3

#using bitwise operators
a = 56
b = 10

#(a)
print("a&b : ", a&b)

#(b)
print("a|b : ", a|b)

#(c)
print("a^b : ", a^b)

#(d)
print("Left shift both a and b with 2 bits: ", a<<2 and b<<2)

#(e)
print("Right shift a with 2 bits and b with 4 bits: ", a>>2 and b>>4)


########################################################################


##Answer4

#Enter the numbers
n1 = float(input("1st Number: "))
n2 = float(input("2nd Number: "))
n3 = float(input("3rd Number: "))

#finding the greatest number in them
print("Greatest of the above three is: ", max(n1, n2, n3))


########################################################################


##Answer5

# string to be entered by user
str = input("Enter your string here:")

print("Is 'name' present in the string?")

# check the results
if "name" in str:
    print("Yes")
else:
    print("No")


########################################################################


##Answer6

#taking sides of triangle
a = float(input("Length of Side1: "))
b = float(input("Length of Side2: "))
c = float(input("Length of Side3: "))

#converting them into integers
A = int(a)
B = int(b)
C = int(c)

#output of the conversion
print("Integral value of A: ",A)
print("Integral value of B: ",B)
print("Integral value of C: ",C)

#Check whether Triangle can be formed or not
print("Can the triangle be formed with these dimensions?")
if A>=(B+C) or B>=(C+A) or C>=(A+B) :
    print("No, Triangle cannot be formed")
else:
    print("Yes, Triangle can be formed")


########################################################################