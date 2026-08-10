print(f"Welcome nice to meet you ❤")
prob=str(input("plese insert number of program\n 1- decide if the name rejected or acepted depinding on the first letter or the lenth of the name\n 2-the sum of digits that constaract a number\n 3- deciding wich word is longer\n")).strip()
if prob=="1":
    user=str(input("please insert the name: ")).strip()
    if user[0].lower()=="a" or len(user)>=7:
        print("Accepted")
    else:
        print("Rejected")
elif prob=="2":
    num=str(input("plese insert the number that you want to use ")).strip()
    container=[]
    for i in num:
        container.append(i)
    total=0
    for a in container:
        total=total+int(a)
    print(f"the summition of digits is {total} ")
elif prob=="3":
    num=int(input("please insert number of words you want to compare "))
    words=[]
    for i in range(num):
        word=str(input("plese insert word ")).strip()
        words.append(word)
    L_word=max(words,key=len)
    print(f"the longest wors is {L_word} and the lenth is {len(L_word)} ")
else:
    print("plese insert a valid number ")



