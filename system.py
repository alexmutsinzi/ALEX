student={}
   
            
def add_student():
 name=input("please enter the student's name here: /n")
 class_name=input("enter class")
 student_number=input("enter your student_number")
 student[name]=student_number
 if name in student:
    print("The student already exist")
 else:
    print("student added successfully")
 course_unit=[]
 for i in range(5):
  unit=input("enter your course_unit here:/n")
 course_unit.append(unit)
marks={}
for unit in course_unit:
    mark=int(input("enter marks for unit"))
    marks[unit]=mark
while True:
   def main():
    print("__welcome home")
    print("1.add student")
    print("2.view student")
    print("1.exit")
    choice=input("enter your choice /n")
                 
    if choice=="1":
     add_student() 
    
          
main()
print("hello world")
    
                




            


    
        