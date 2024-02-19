x=3
while x>0:
        print("\1")
        a=float(input("Enter Marks Obtained in English: "))
        b=float(input("Enter Marks Obtained in Hindi: "))
        c=float(input("Enter Marks Obtained in Maths: "))
        d=float(input("Enter Marks Obtained in Science: "))
        e=float(input("Enter Marks Obtained in So. Sci.: "))
        p=(a+b+c+d+e)/5
        s=a+b+c+d+e
        print ("\1")
        if(p>=33):
                print ("PASS")
        if(p<33):
                print("FAIL")
        print ("Total Marks Obtained=", s)
        print ("Percentage Secured=", p, "%")
        if(p>=90):
            print("Grade: A")
        elif(p>=80 and p<90):
            print("Grade: B")
        elif(p>=70 and p<80):
            print("Grade: C")
        elif(p>=60 and p<70):
            print("Grade: D")
        else:
            print("Grade: F")
        print ("_"* 80)
