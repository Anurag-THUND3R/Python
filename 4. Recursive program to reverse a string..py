def reverse(string):
  if len(string)==0:
    return string
  else:
    return reverse(string[1:])+string[0]

s=str(input("Enter A String to reverse"))
print(reverse(s))
