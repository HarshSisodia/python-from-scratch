import random
import string
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

# a=input("Enter message: ")
# first_char=a[0]
# remaining=a[1:]

# secret=remaining+first_char+"ten"
# print(secret)


# remove=secret[:-3]
# print(remove)
# remain=remove[-1]
# print(remain)
# remain1=remove[:-1]

# decode=remain+remain1
# print(decode)



#New Code:- 
st = input("Enter message: ")
words = st.split(" ")

coding = input("1 for Coding or 0 for Decoding")
coding=True if coding =="1" else False #Short Hand Code
print(coding)

if coding:
    nWords = []

    for word in words:
        if len(word) >= 3:
            first_char = word[0]
            remaining = word[1:]
            r1=random.choice(string.ascii_letters) 
            r2=random.choice(string.ascii_letters) 
            

            secret = r1 + remaining + first_char + r2
            nWords.append(secret)
        else:
            nWords.append(word[::-1])
    print("Encoded Message: ")
    print(" ".join(nWords))

else:
    nWords=[]
    for word in words:
            if(len(word)>=3):
                stNew = word[1:-1]
                stNew=stNew[-1]+stNew[:-1]
                nWords.append(stNew)
            else:
                nWords.append(word[::-1])
    print("Decoded Message:")
    print(" ".join(nWords))

                                   
#    else:
#     nWords = []

#     for word in words:
#         if len(word) >= 3:
#             # Remove "ten"
#             remove = word[:-3]

#             # Remove "Start"
#             remove = remove[5:]

#             # Bring last character to the front
#             remain = remove[-1]
#             remain1 = remove[:-1]

#             decode = remain + remain1
#             nWords.append(decode)
#         else:
#             nWords.append(word[::-1])

#     print(" ".join(nWords))
