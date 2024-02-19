import matplotlib.pyplot as plt

subjects=["English","Physics", "Chemistry","Maths","C.S."]
marks=eval(input("Enter Marks obtained in English,Physics,Chemistry,Maths,C.S."))

plt.pie(marks,labels=subjects,autopct="%1.1f%%")
plt.title("Marks Pie Chart")

plt.show()
