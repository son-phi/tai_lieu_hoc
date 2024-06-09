s= input()
c= input()
print(s.find(c) if s.count(c)<=1 else "{} {}".format(s.find(c), s.rfind(c)))
# len(s)-s[::-1].find(c)-1