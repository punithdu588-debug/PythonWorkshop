student1="Punith D U"
student2="Rajesh"
student3="Prakash"
student4="Mahesh"
student5="Ramesh"
student6="Gudkesh"



student_names=["Punith D U","Rajesh","Prakash","Mahesh","Ramesh","Gudkesh"]
print(student_names)

print(student_names[1])
print(student_names[-1])
student_names[2]="Babu"
print(student_names)

student_names.remove("Punith D U")
student_names.remove("Rajesh")

print(f"remove Punith D U and Rajesh:{student_names}")

student_names.insert(1,"om")
print(student_names)

student_names.insert(2,"Ram")
student_names.insert(3,"Raju")

print(student_names)

student_names.pop(3)

print(f"Length of list:{len(student_names)}")

print(student_names.reverse())



