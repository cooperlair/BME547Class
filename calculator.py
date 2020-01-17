#calculator.py

def add(x,y) :
	z = int(x) + int(y)
	symbol = "+";
	return z,symbol

def subtract(x,y) :
	z = int(x) - int(y)
	symbol = "-";
	return z,symbol

def multiply(x,y) :
	z = int(x) * int(y)
	symbol = "*";
	return z,symbol

def divide(x,y) :
	z = int(x) / int(y)
	symbol = "/";
	return z,symbol

x = input("Enter a letter: ")
print("You entered {}".format(x))
a = input("Enter a number: ")
b = input("Enter a second number: ")
if x == "a":
	r, s = add(a,b)

elif x == "s":
	r,s = subtract(a,b)

elif x == "m":
	r,s =multiply(a,b)

elif x == "d":
	r,s = divide(a,b)	

else:
	print("The {} command is not recognized".format(x))

print("{} {} {} = {} ".format(a,s,b,r))	
print("Done")	

