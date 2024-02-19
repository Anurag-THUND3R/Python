import matplotlib.pyplot as plt
subjects=["English","Physics", "Chemistry","Maths","C.S."]
marks=eval(input("Enter Marks obtained in English,Physics,Chemistry,Maths,C.S."))
plt.bar(subjects,marks,width=0.5,color=['b','r','c','m','g'])
plt.title("Marks Graph")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()
