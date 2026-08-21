#variable define

#variable name=variable value
#name="amit gupta"
#age=21
#price=25.99
#print("name")
#print(21)
#print("my name is:",name)
#print("my age is :",age)
#print(type(name))
#print(type(price))
#print(type(age))

#data types

#age =23
#old  = False
#a =None
#print(type(old))
#print(type (a))

 #arithmatic operation

#
"""" a=2
b=5

sum=2+5
print(sum)#

sub=2-5
print(sub)"""
 
#arthmatic operatora
#a=2
#b=5
#print(a+b)
#print(a-b)
#print(a*b)
#print(a/b)
#print(a%b) #remainder
#print(a**b)#a^b""""""""

  #relational operators
#a=50
#b=20
#print(a==b) false
#print(a!=b) true
#print(a>=b) true
#print(a>b)  True
#print(a<=b) false
#print(a<b)  false

# assignment operators 

#num=10
#num=num+10
#num+=10
#print("num:",num)

# logical operators

#a=50 
#b=30
#print(not False)  not operators
#print(not(a>b))

#val1=True 
#val2=False
#print("and operator:",val1 and val2)
#print("OR operator:",val1 or val2)

# type conversion
#a= int("2")
#b=4.25
#print(type(a))
# print(a+b)

#user se input 
#practice question

#wap to input 2 number & print their sum
#first=int(input("enter first:")) 
#second=int(input("enter second:"))

#print("sum=",first+second)

# wap to input side of square & print its area

#side=float(input("enter square side:"))
#print("area=",side* side)

 #wap to input 2 floating point number & print their average

#a=float(input("enter first:"))
#b=float(input("enter second:"))
#print("avg=",(a+b)/2)

#wap to input 2 int number,a and b.
#print true if a is greater than or equal to b.if not print false

#a=int(input("enter first:"))
#b=float(input("enter second:"))
#print(a>=b)
 
#string operation

#str1="this is a string.\n we are creaing it in python"
#print(str1)

#concatenation (merged)
#str1="apna"
#str2="college"
#final_str=str1+str2
#print(final_str)

#first_name ="Ajay"
#last_name =" kumar"
#full_name = first_name+""+last_name
#print(full_name)

#length(string)

#str1="apna"
#len1=len(str1)
#print(len1)

#str2="college"
#len2=len(str2)
#print(len2)

#index value print

#str="apna"
#print(str[3])

#slicing index

#str="apna college"
#print(str[1:4])
#print([str[0:4]])
#print([str[5:12]])
#print([str[5:len(str)]])

#st= "hello good evening"
#print(st[6:10])
#print(st[7:10])
#print(st[6:])
#print(st[:10])
#print(st[::2])
#print(st[::-1])

#first_name ="Ajay"  # repitation function
#last_name =" kumar"
#full_name = first_name+""+last_name
#print(full_name)
#print(full_name*10)
#print((full_name+"\n")*10)

#print("j" in full_name)  # members operators
#print("j" not in full_name)
#print("kumar" in full_name)

#str= "hello good evening"   # traversing string
#for i in range(len(str)):
    #print(i)

#st="hello good evening"    # string method
#print(st.upper())
#print(st.lower())
#print(st.title())
#print(st.capitalize())
#print(st.swapcase())


#st1=st.replace("evening","morning")  #changing
#print(st1)

#print(st.find("n"))
#print(st.find("o"))
#print(st.find("o,9"))
#print(st.index("o"))
#print(st.find("n"))

#st="hello good evening" 
#print(st.startwith("hello")) # true
#print(st.endwith("morning")) # false

#name=input("enter name")  # name mai vowels check
#c=0
#for i in name:
 #if i in "aeiou":
   #  c+=1
    # print(name)
     #print("total vowels=",c)

#colors="red,green,yellow ,black"  # splite method by default
#fruits="apple orange banana kiwi"
#print(fruits.split())
#print(fruits.split("a"))

#colors="red,green,yellow ,black"  # splite converts to list
#fruits="apple orange banana kiwi"
#fruits_list=fruits.split()
#colors_list=fruits.split(",")
#print(fruits_list)
#print(colors_list)

#new_colorst=" ".join(colors_list)
#print(new_colorst)

#st = " hello "
#print(st,"size=",len(st))
#print(st.strip(),"size=",len(st.strip()))
#print(st.lstrip(),"size=",len(st.lstrip()))
#print(st.lstrip(),"size=",len(st.lstrip()))
#print(st.rstrip(),"size=",len(st.rstrip()))

#st="python" 
#print(st)
#print(st.center(20))
#print(st.center(20,"*"))

#st="hello"         # isalpha()- checks alphabets
#print(st.isalpha())
 
#st="hello123&"
#print(st.isalnum())  #checks alpahanumeric 
#st="hello123"
#print(st.isalnum())

#st="hello"
#print(st.islower())    # check all letters are lower case

#st="hello"
#print(st.isupper)  # upper case 

#st="amit kumar"
#print(st.istitle())  # check title case

#st="  "
#print(st.isspace())  # checks space only

#st="12334"
#print(st.isnumeric)  # checks numeric value

#st="python" # positive indexinng
#print(st[0])
#print(st[1])
#print(st[2])
#print(st[3])
#print(st[4])
#print(st[5])

# negative indexing
#print(st[-1])
#print(st[-3])


   
   #string function

#str=" i am studing  python from apnacollege"
#print(str.endswith("ege"))
#print(str.endswith("apna"))

#str= "i am studing  python from ApnaCollege"
#print(str.capitalize())
#print(str)



#str= "i am studing  python from ApnaCollege"
#print(str.replace("o","a"))
#print(str.replace("python","javascript"))


#str= "i am studing  python from ApnaCollege"
#print(str.find("o"))
#print(str.find("from"))

# practice question

#q1=wap to input user first name& print is length
 
#name=input("enter your name:")
#print("length  of your name is " ,len(name))

#wap to find the occurence of '$' in a string

#tr="hi, $iam the $ symbol $99.99"
#print(str.count("$"))
  
# list data type

#mylist=[]  # empyt list    
#print(mylist)
#print(type(mylist))

#colors=["red","green","blue","pink"]
#print(colors)
#print(type(colors))

#my_list=[5,6.5,"python",True,[10,20],5]  #one variable  different value
#print(my_list)

#mylist=[2,3,4,4,5,6,7]
#print(len(mylist))   # slicing list method
#print(mylist[2:6])
#print(mylist[:6])
#print(mylist[::-1])

#print("before changing",mylist) 
 # update method
#mylist[3]=400
#print("after changing",mylist)


#list=[4,8,3,9]
#print(list)

# ADD ELEMENT
#list.append(1)
#list.append(20)
#list.append(40)
#print(list)

# insert
#list.insert(2,200)
#print(list)

# EXTEND multiple value add
#list.extend([400,600,100])
#print(list)

# REMOVE ELEMENT
# POP
#print(list)
#list.pop()
#list.pop(-1)
#print(list)

#list.pop(2)  # index according
#print(list)


#list.clear()
#print(list)

#name_list=[]
#for i in range(5):
    #name=input("enter name")
    #name_list.append(name)
    #print(name_list)


#even_list=[]
#for i in range(10):
        #num=int(input("enter any number"))
        #if num%2==0:
            #even_list.append(num)
            #print(even_list)


        #L1=[1,2,3]    # list operators add 
        #L2=[4,5,6]
        #L3=L1+L2
        #print(L3)
        #print(L3*2)
        # 
        
#L1=[[1,2,3],[40,50,60],[17,18,19]]   #  nested  one list list mai another list
#print(L1) 
#print(L1[1])
#print(L1[1][1])


#mylist=[2,4,6,8]
#for i in range(len(mylist)):
    #print(i,":",mylist[i])


#L1=[[1,2,3],[40,50,60],[17,18,19]]
#for i in L1:
    #print(i)

#for inner_list in L1:
    #for ele in inner_list:
        #print(ele)

#for row in range(1,6):
    #for col in range(row):
        #print("*",end=" ")
        #print()  

#for row in range(5,0,-1):
#for col in range(row):
    #print("*",end=" ")
 #print()

#for row in range(1,6):
    #for col in range(6-row):   
        #print(" ",end=" ")
#for col in range(row):
    #print("*",end=" ")
#print()     





        
for row in range(1,6):           # 1,5 ,row=5
    for col in range(6-row):     # (6-5)=1-1=0
        print(" ", end=" ")
    for col in range(row):
        print("*", end=" ")
print()

     
#start_num=int(input("enter ist num")) #1
#end_num=int(input("enter 2nd num"))   #10

#for num in range(start_num,end_num+1):  #(1,11)
    #if num>=2: # num>=2   5>=2
        #for i in range(2,num): #(2,5)
         #if num%i==0:  #5%2==0
            #break
        #else:
            #print(num)
#i=1

#while i<=5:
        #print(i)
       # i+=1

        #num=int(input("enter number"))  
        #f = 1
        #for i in range (1,num+1):
                #f=f*i              # f=1*1, f=1 #f=2*3,f=6
                #print(f)


        #import random
        #print(random.randint(1,100))

        # symbol=@
raw_data = "sumit1234567@890"
name=" "
emial_id=""
phone_no=" "
domain=" " 
symbol=" "
for i in raw_data:
    if not i.isnumeric():
        emial_id +=i
    elif i.isnumeric():
        phone_no+=i
        if not i.isalnum():
            symbol+=1

    list=["aman kuymar","rohit ahuja","ravi yadav","adi sahu"]
    f=[]
    l=[]
    for i in list:
        f.append(i[:i.find(" ")]) 
        l.append(i[i.find(" ")+1:]) 
        print(f) 
        print(l)

        # tuple method
        tup=()
        print(tup,type(tup))


        

 

  #conditinal statment
#age=24


#(age>=18)
#print("can vote & apply  for lincese")

 #elif condition

#light="green"

#if(light=="red"   ):
 #print ("stop")
#elif(light=="green") : 
#print("go")  
#elif(light=="yellow"):
#print("look")

#num=5
#if(num>2):
#print("greater than2")
#elif(num>3):
#print("greater than 3")

#light="pink"

#if(light=="red"):
      #print("stop")
#elif(light=="green") :
      #print("go")  
#elif(light=="yellow"):
      #print("look")
#else:
      #print("light is broken")

#print("end od code")

#age=13
#if( age>= 18):
      #print("can vote")  # indentation
#else:
      #print("cannot vote")

#marks= int(input("enter student marks:"))   # student grade question

#if(marks>=90):
   #grade="A"
#elif(marks>=80 and marks<90):
   #grade="B"
#elif(marks>=70 and marks<80):
    #grade="C"
#else:
   #grade="D"
#print("grade of the student->",grade)

#age=95

#if(age>=18):       # nesting  condition
    #if(age>=80):
      # print("cannot drive")

#else: 
   #print("can drive")
   # else:
#print("cannot drive")

#practice question

#WAP TO CHECK IF A NUMBER ENTERED BY  THE USERS IS ODD OR EVEN

#num=int(input("enter number:"))
#rem= num%2
#if(rem==0):
    #print("even")
#else:
    #print("odd")

    #WAP TO FIND THE GARGEST OF 3 number entered by the users

#a= int(input("enter  first number"))
#b= int(input("nter second number:"))
#c= int(input("enter third numbers:"))

#if(a>=b and a>=c):
    #print("first number is largest",a)
#elif(b>=c):
    #print("second number is largest",b)
#else:
    #print("third number is largest",c)

   # WAP TO CHECK IF  number is a multiple of 5  or not

#x=int(input("enter number:"))
#if(x%5==0):
    #print("multiple of 5")
#else:
    #print("not a multiple")
    
 # list  in python

#marks=[94.4, 87.5, 95.2, 66.4, 45.1]
#print(marks)
#print(type(marks))
#print(marks[0])
#print(marks[1])

#student=["amit",95.4,17,"delhi"]
#print(student[0])
#student[0]="arjun" name change
#print(student)

#marks=[84,94,76,63,48]
#print(marks[1:])
#print(marks[-3:-1])

#list method

#list=[2,1,3]   #append method
#list.append(4)
#print(list.sort())   #sort method
#print(list.sort(reverse=True))  # reverse list
#print(list)

#list=['a','d','e','f','c','b']
#list.reverse()
#print(list)

#list=[2,1,3]
#list.insert(1,5)
#list.remove(1)
#list.pop(2)
#print(list)  

#Typles in python

#tup=(2,1,3,1)
#print(type(tup))

#tup=(1,)
#print(tup)
#print(type(tup))

#tup=(1,)
#print(tup)
#print(type(tup))

#tup=(1)
#print(tup)
#print(type(tup))

#tup=(1,2,3,4)
#print(tup[1:3])

#tuple method

#tup=(1,2,3,4)
#print(tup.index(2))

#tup=(1,2,3,4,2,2)
#print(tup.count(2))

#WAP TO ASK THE USER TO ENTER NAMES OF THEIR 3 FAVOURITE MOVIES &STORE THAN  IN A LIST
#movies=[]
#mov1=input("enter  first movie:")
#mov2=input("enter  second movie:")
#mov3=input("enter  third movie:")

#movies.append(mov1)
#movies.append(mov2)
#movies.append(mov3)

#print(movies)

#WAP TO CHECKIF A LIST CONTAIN A PALINDROME O ELEMENT .(HINT:USE COPY()METHOD)

#list1=[1,2,1]
#list2=[1,2,3]

#copy_list1=list1.copy()
#copy_list1.reverse()

#if(copy_list1==list1):
    #print("palindrome")
#else:
    #print( "not palindrime")

#list1=["m","a","a","m","p"]
#copy_list1.reverse()

#if(copy_list1==list1):
    #print("palindrome")
#else:
    #print( "not palindrime")


    #wap to count the number of student with the "a" grade in the following tuple

#grade=["C","D","A","B","B","A"]
#grade.sort()
#print(grade)

# DICTINARY IN PYTHON

#info = {
#"key" : "value",
#"name": "apna college",
#"learning" : "coding"
#}

#print(info)

#info={
    #"name":"apna college",
    #"subject":["python","c","java"],
    #"topics":("dict","set"),
    #"age":35,
    #"is_adult":True,
    #12.99:94.4
#}
#print(type(info))
  
#student={
    #"name":"amit gupta",
    #"subjects":{
        #"phy":97,
        #"chem":98,
        #"math":95
    #}
#}
#student.update()
#print(student)

# python in sets

#collection={1,2,3,4,"hello","world"}

#print(collection)
#print(type(collection))
#print(len(collection))

#collection =set() #empty set; syntax
#print(type(collection))

#collection =set()
#collection.add(1)
#collection.add(1)
#collection.add(2)
#print(collection)
#collection.clear()
#collection.remove(1)
#print( len(collection))

#set1={1,2,3}
#set2={2,3,4}

#print(set1.union(set2))
#print(set1.intersection(set2))
#print(set1)
#print(set2)

#PRACTICE QUESTION
#QUESTION 1

#table:"a piece of furniture","lists of acts of figure"
#cat:"a small animal"


#DICTIONARY={
#"CAT":"A SMALL ANIMAL",
#"TABLE":("A PIECE OF FURNITURE","LIST OF FACTS & FIGURES")
#}
#print(DICTIONARY)

#
#Q2 you are given a lists of subjects foe student.assume one classroom is reqried for 1subject.how many classroom are needed by by all subjects.

#subject={
    #"python","java","c++","python","javascript","java","python","java","c++","c"
#}
#print(subject)
#print(len(subject))

#Q3 wap to enter marks of 3 subject from the users and store thenm in a dictinary.start with an empty
#dictionary & add one by one.use subject name as key & marks as value

#marks={}

#x=int(input("enter phy:"))
#marks .update({"phy":x})

#x=int(input("enter math:"))
#marks .update({"math":x})

#x=int(input("enter chem:"))
#marks .update({"chem":x})

#print(marks)

#values={9,9.25,8,8.0}
#print(values)


# calc_sum(a,b):
  #  sum=a+b
   # print(sum)
    #return sum

#calc_sum(5,1)


#cities=["delhi","pune","noida","chennai", "mumbai" ]
#heroes=[ "thor","ironman","captain  america","shaktiman" ]

#def print_len(list):
    #print(len(list))

    #print_len(cities)
    #print_len(heroes)  


    # OOPS IN PYTHON 

    
#class student:
    #name="karan"

#s1=student()
#print(s1.name)



#class Car:
    #color = "blue"
    #brand = "mercedes"

#car1 = Car()
#print(car1.color)
#print(car1.brand)

#constructor



#class student:
    #name = "karan"

    #def __init__(self):   #default constructor
        #print("adding new student in database")


#s1 = student()

#class student:
    #name = "karan"
# parametrized constructor
    #def __init__(self,name,marks):
        #self.name=name
        #self.marks=marks
        #print("adding new student in database")

#s1 = student("karan",78)
#print(s1.name,s1.marks)

#s2=student("arjun",88)
# print(s2.name,s2.marks)

#Q1 CREATE A ACCOUNT CLASS WITH 2 ATTRIBUTES- BALANCE& ACCOUNT NO.



#class Account:
    #def __init__(self, bal, acc):
        #self.balance = bal
        #self.account_no = acc

    #def debit(self, amount):
        #self.balance -= amount
        #print("Rs.", amount, "was debited")
        #print("Total balance:", self.get_balance())

    #def credit(self, amount):
        #self.balance += amount
        #print("Rs.", amount, "was credited")
        #print("Total balance:", self.get_balance())

    #def get_balance(self):
        #return self.balance


# object creation (outside class)
#acc1 = Account(100000, 12345)

#acc1.debit(10000)
#acc1.credit(500) 



#class Student:
    #def __init__(self, name):
        #self.name = name

# object creation
#s1 = Student("Shradha")

# print student name
#print(s1.name)

# delete object
#del s1


#class Account:
    #def __init__(self, acc_no, acc_pass):
        #self.acc_no = acc_no
        #self.acc_pass = acc_pass

# object create
#acc1 = Account("12343", "abcde")

# print values
#print(acc1.acc_no)
#print(acc1.acc_pass)

# del keyword
# used to delete object properties or object itself

# opps concept public Attributes
#class account:
 #def    __init__(self, acc_no, acc_pass):
 # self.acc_no = acc_no
  ##self.acc_pass = acc_pass


#acc1 = account("12345", "abcde")
   
#print(acc1.acc_no)
#print(acc1.acc_pass)

#def : private(like) attributes & methods
#conceptual implement & method are meant to used only with 
# in the class and are not accessible from outside the class 
# private concept

#class account:
    #def __init__(self, acc_no, acc_pass):
        #self.acc_no = acc_no
        #self.__acc_pass = acc_pass

#acc1 = account("12345", "abcde")

#print(acc1.acc_no)
#print(acc1.__acc_pass)

# inheritance: when one class(child/derived) derives the properties & method of another class
#(parents /base) 

#class car:
    #@staticmethod
    #def start():
        #print("carstarted..")


    #@staticmethod  
    #def stop():
        #print("car started.")

#class toyotacar(car):
    #def __init__(self, name):
        #self.name = name

#car1 = toyotacar("fortuner")
#car2 = toyotacar("prius")

#print(car1.start())
        
# INHERITANCE
 # multilevel inheritance

#class car:
    #@staticmethod
    #def start():
        #print("car started..")


    #@staticmethod  
    #def stop():
        #print("car started.")

#class toyotacar(car):
    #def __init__(self, brand):
        #self.brand= brand

#class fortuner(toyotacar):
 #def __init__ (self, type):
        #self.type= type

#car1 =fortuner("diesel")
#car1.start()

# multiple inheritance

#class a:
    #vara="welcome to class a"
#class b:
    #varb ="welcome to class b"
#class c(a,b):
    #varc ="welcome to class c"

#c1 = c()
#print(c1.varc)
#print(c1.varb)  
#print(c1.vara)     
 
 # class method
 # a class method is bound to the class & recevies the class as  an implicit first argument.
 # static method  cannot access or modify class state & gernerally for utility.
        
  #class student:
  #def __ init__(self, phy, chem, math):
  #self.phy = phy 
  #self.chem = chem
 ##self.math = math
 