#question1
str=input("enter the string ")                                    #asking for input
str=str.lower()
str=str.strip()                                                  #striping the string 
if ' ' in str:                                                   #string will be sentence if ithas space in it otherwise word
     str=str+' '                                                 #in case of sentence adding space at last because program recognise word by spaces
     while len(str)>0:                                           #looping till we extract every word of string
           print(str[0:str.find(' ')+1],str.count(str[0:str.find(' ')]))                  #print the first word and number of times it occur and removing every intance of it from string
           str=str.replace(str[0:str.find(' ')+1],'')
else:
     while len(str)>0:                                           #if string is word extracting every letter and displaying its count
          print(str[0],str.count(str[0]))                        
          str=str.replace(str[0],'')                             #removing every instance of letter which we have counted and printed


#question2
day=int(input("enter date "))
month=int(input("enter month "))
year=int(input("enter year "))                          #taking the input
if 1<=day<=31 and 1<=month<=12 and 1800<=year<=2025:
   if month==12 and day == 31:                            #cheching if it is last day of year
      day=1
      month=1
      year+=1
   elif day==31 and month in [1,3,5,7,9,11]:              #checking if it islast day of month
     day=1
     month+=1
   elif day==30 and month in [4,6,8,10]:
     day=1
     month+=1
   elif day==29 and month==2 and year%4==0:
     day=1
     month+=1
   elif day==28 and month==2 and year%4!=0:
     day=1 
     month+=1
   else:                                        #if it neither last day of year nor last day of moth then increasing the day by 1
     day+=1
   print("next date is")
   print("day - ",day)
   print("month - ",month)
   print("year - ",year)
else:
 print("enter valid date")                        #erroe message if conditions given in question are not met 


#question3
lst=[3,6,9]                             #definig the given list
sqr=[]                                  #creating an empty list that will store the tuples of number and its squre
for i in lst:                           #looping through the entrie list tocreate tuples of list
  sqr.append((i,i*i))
print(sqr)                              #printing the entire list




#question4
table=[{"letter":"A+","performance":"Outstanding","points":10},
{"letter":"A","performance":"Excellent","points":9},
{"letter":"B+","performance":"Very Good","points":8},
{"letter":"B","performance":"Good","points":7},
{"letter":"C+","performance":"Average","points":6},
{"letter":"C","performance":"Below Average","points":5},
{"letter":"D","performance":"Poor","points":4}]                       #creating the list of dictionary of table given in the question
student_points=int(input("enter your grades "))                       #inputting the grades
for i in table:                                                       #checking if grade is in list
    if i["points"]==student_points:
        print("Your grade is",i["letter"],"and",i["performance"])     #printing the required grade
        break
else:
   print("grade is out of range")                                     #error messsage




#question5
pattren='ABCDEFGHIJK'                                  #string required for given pattern
for i in range(1,7):                                   #defining number of lines in pattern
   print(pattren[0:2*(6-i)+1].center(11))              #printing the required number of chracers and centering them


#question6
dic={}                                  #creating a dictionary to store values
while 1:                                # starting an infinite loop
    a=input("enter Y to enter students detail enter N to exit ")        #getting value to continue dictionary or not
    if a=='y'or a=="Y":
        Sid=int(input("enter SID "))
        name=input("enter name ")
        dic.update({Sid:name})                                        #adding given value to dictionary
    elif a=="n"or a=="N":                                             #checking if user wants to end loop
        break
    else:
        print("enter only y or n")
if len(dic):                           #checking if dictionary is empty or not 
   print("all students details\n",dic)         #a part of question to display whole dictionary


   names=[]                           #creating a copy of list of values to sort as dic.values() give view only object it cannot be sorted 
   for a in dic.values():
      names.append(a)
   names.sort()
   print("\nstudents sorted by thier names")
   for x in names:                  #comparing names in dictionary to sorted list to display dictory sorted by names
      for y in dic:
        if x==dic[y]:
           print(y,dic[y])


   sid=[]
   print("\nstudents sorted by their SID")
   for a in dic.keys():              #creating a copy of key of dictionary as dic.keys() give view only obbject which cannot be sorted
       sid.append(a)
   sid.sort()
   for x in sid:                    #printing dictionary according to sorted sid
      print(x,dic[x])



   sid=int(input("\nenter the sid to search "))          
   if sid in dic.keys():                       #checking if given sid is in dictionary
       print (sid,dic[sid])        
   else:
       print(" no such sid")                 #error message if searchedsid not found 
else:
    print("no values entered")               #error message if dictionary is empty



#question7
a=1                                          #entring first two terms of series a,b
b=1
c=0                                          #defining next term of series
r=int(input("enter number of terms of fibonacci series "))  #asking for number of terms of sries
sum=0
count=0                                      #counting number of terms
print(a)                                     #printing first two terms
print(b)
for i in range(3,r+1):                       #looping from 3 as 1,1are first two terms
    c=a+b                                    #looping for series and then shifing values of b toa and c to b to make c empty for next term
    print(c)
    a=b
    b=c
    sum+=c                                   #adding the term of series to net sum
    count+=1
avg=sum/count                                #counting average
print("average is",avg)



#question8
Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}
print("Set1",Set1,"\nSet2",Set2,"\nSet3",Set3)              #creating original sets
#creating necessary sets to make program neater

Set123=Set1.union(Set2,Set3)                                #defining union of three sets
Set12=Set1.intersection(Set2)
Set23=Set2.intersection(Set3)
Set13=Set1.intersection(Set3)
Set12_23_13=Set12.union(Set23,Set13)                        #defining union of all elements which are atlest in two sets
Set1_2_3=Set1.intersection(Set2,Set3)                       #altough intersection is an empty set but if original sets are altered it would bbe required
Set1_10={1,2,3,4,5,6,7,8,9,10}

#using union , interstion , diffrence of various sets to achive required set
Set_a=Set1.symmetric_difference(Set2)                       
print("elements whichare in set1 or Set2 but not both\n",Set_a)

Set_b=Set123.symmetric_difference(Set12_23_13)
print("elements that are in only one of the three sets Set1,Set2 and Set3\n",Set_b)

Set_c=Set12_23_13.symmetric_difference(Set1_2_3)
print("elements that are exactly two of the sets Set1, Set2 and Set3\n",Set_c)

Set_d=Set1_10.symmetric_difference(Set1)
print("all integers in the range 1 to 10 that are not in Set1\n",Set_d)

Set_e1=Set1_10.intersection(Set123)                              #defining all the elemnts in set which are in sets 1,2,3
Set_e=Set1_10.symmetric_difference(Set_e1)                       #removing all those elements from set of 1 to 10
print("all integers in the range 1 to 10 that are not in Set1,Set2 and Set3\n",Set_e)




