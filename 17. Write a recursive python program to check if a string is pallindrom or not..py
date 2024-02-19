def st_Palindrome(string):
          if len(string)<1:
                    return True
          else:
                    if string[0] == string[-1]:
                              return st_Palindrome(string[1:-1])
                    else:
                              return False
#Calling Program

s=str(input("Enter String : "))
if st_Palindrome(s) == True:
          print("String is Pallindrom")
else:
          print("String is not Pallindrom")
