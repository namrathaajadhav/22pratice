# string formating 
name =  input("enter your name:")
surname = input("enter your surname:")
hobbies = int("enter you hobbies:")
greeting = f"hello,{name}! my surname{surname}! my hobbies{hobbies}
print(greeting)

name = "namratha"
surname = "jadhav"
hobbies = "cooking"
print(("{}surname is {} and my hobbies is{}".format(name,surname,hobbies)))

name = "namratha"
surname = "jadhav"
hobbies = "cooking"
print(("{1}surname is {1} and my hobbies is{2}".format(name,surname,hobbies)))


name = "namratha"
surname = "jadhav"
hobbies = "cooking"
print(("{2}surname is {1} and my hobbies is{0}".format(name,surname,hobbies)))



name = "namratha"
surname = "jadhav"
hobbies = "cooking"
print(name,"surname is",surname, "my hobbies is",hobbies)


#list>>> 

#access list
marks = [55,65,85,95]
highest_marks = marks[3]
average_marks = sum(marks)
marks.append
number_marks = len(marks)
print("marks:", marks)
print("average marks:", average_marks)

number = "50 + 20 - 10"
number1 = 50
number2 = 20
number3 = 10
more = eval(number)
print(more)

#nested list
list1 = ['a', 'b','c','d',['apple','blue'],['300','500','800']]
print(list1[4])




