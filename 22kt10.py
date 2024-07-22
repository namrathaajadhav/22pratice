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
print(list1[4][1][2])
print(list1[-1])



#acceing element from the list

list1 = eval(input("enter list:"))
print(list1[2])
print(list1[0:4])

list[0]= "a"
list1[1]= "b"
print(list1)

#looping through the list
numbers =(1,2,3,4,5)
i = 0
while i < len(numbers):
  print(numbers[i])
i= i+1

numbers = [10,20,30,40]
for element in numbers:
  print(element)


#insert>>>
numbers = [1,3,5]
numbers.insert(1,2)
numbers.insert(1,4)
print(numbers)
numbers.insert(10,True)
print(numbers)

numbers.insert(10,50.0)
print(numbers)
