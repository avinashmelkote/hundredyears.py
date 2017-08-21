# hundredyears.py
The program you what year you will turn 100 years old if you enter your name and age in the year 2017.
name = raw_input("Please enter your name: ")
age = raw_input("Please enter your age: ")
hundredyear = 2017 - float(age) + 100
print "Hello",name,"you will be 100 years old in the year",int(hundredyear),"because you are",age,"years old today."
