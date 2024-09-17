str="hello    This     is      AIML"
s = str.strip().replace("  ", " ")
r = " ".join(s.split()[::-1])
print(r)
