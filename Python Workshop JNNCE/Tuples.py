'''student_names=("Punith D U","Suresh","Kamalesh","Prakash","Lokesh","Harish","Komal")

print(student_names.count("Punith DU"))

print(student_names.append(3,"Raju"))


print(student_names.pop(3,"Raju"))'''



student_names={"Punith D U","Suresh","Kamalesh","Prakash","Lokesh","Harish","Komal","Punith D U"}

print(student_names)

student_names.add("Power")
print(student_names)
student_names.remove("Power")
student_names.clear()

print(type(student_names))




data={'name':"Punith",'age':222,'Qualify':"Gate"}
print(type(data))

data={'name':"Punith",'age':22,'Qualify':"Gate"}
print(data)

print(data.values())

print(data.update("name":"puni","name":"baba"))

