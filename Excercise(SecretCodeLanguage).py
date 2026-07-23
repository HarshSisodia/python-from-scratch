# import random
# import string
# char=random.choice(string.ascii_letters) 
# a="Harry"
# b= a[1:]
# print(b)
# c=b+a[0]+ "ten"
# print(c)

# d= c[:5]
# print(d)
# e=a[0]+d[:4]
# print(e)

a="Harry"
first_char=a[0]
remaining=a[1:]

secret=remaining+first_char+"ten"
print(secret)


remove=secret[:-3]
print(remove)
remain=remove[-1]
print(remain)
remain1=remove[:-1]

decode=remain+remain1
print(decode)