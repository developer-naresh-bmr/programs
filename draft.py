name=input("Enter the name of student:")
age =input("Enter the age of student:")
#marks=85
print("\n\n")
print("Enter the marks got in 10th in 5 subjects")
m1=int(input("enter marks of student in first subject:"))
m2=int(input("enter marks of student in second subject:"))
m3=int(input("enter marks of student in third subject:"))
m4=int(input("enter marks of student in fourth subject:"))
m5=int(input("enter marks of student in fifth subject:"))

def sum(x,y,z,u,v):
 return m1+m2+m3+m4+m5
a=sum(m1,m2,m3,m4,m5)
percentage=a/5
#print(a)
#marks12= print(input("Enter the marks got in 12th:"))
gender= input("Enter the gender of student(m/f).")
if(gender=='m'):
 g="he"
else:
 g="she"

#print("{0} was {1} years old when we get {2} marks in 10th".format(name,age,marks))
print()

print(f'{name} was {age} years old when {g} got {percentage} percentage in class 10th .')