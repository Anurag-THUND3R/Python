import matplotlib.pyplot as plt

subject=input("Enter name of Subject : ")
students=eval(input("Enter names of all Students: "))
marks=eval(input("Enter marks obtained by Students"))

plt.plot(students,marks)
plt.title(subject)
plt.xlabel("Student's Name")
plt.ylabel("Marks")

plt.show()
