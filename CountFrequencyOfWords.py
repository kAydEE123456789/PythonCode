str = input("Enter the String\n")

def fre(str):
    str = str.split()
    strr = []

    for i in str:
        if i not in strr:
            strr.append(i)
    count = 0
    for i in strr:
        for j in range(0,len(str)):
            if(i==str[j]):
                count = count + 1
        print(i,' ',count,'times')
        count = 0

fre(str)