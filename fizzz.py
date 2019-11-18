
fizznum = int(input("input fizz number: "))
buzznum = int(input("input buzz number: "))
minnum = int(input("input min number: "))
maxnum = int(input("input max number: "))

fizzList = []
buzzList = []
both = []

for i in range(minnum,maxnum+1):
    result = ""
    fb = fizznum*buzznum
    if i%fb==0:
        result="FizzBuzz"
        both.append(i)
    elif i%fizznum==0:
        result="Fizz"
        fizzList.append(i)
    elif i%buzznum==0:
        result="Buzz"
        buzzList.append(i)
    else:
        result=str(i)
    print(result)

want = input("What want? Fizz,Buzz, or fizzybuzzy/both: ?")
if want.lower() == "fizz":
    print(fizzList)
elif want.lower() == "buzz":
    print(buzzList)
elif want.lower() == "both":
    print(both)
elif want.lower() == "fizzybuzzy":
    print(both)
else:
    print("jacob die")
ser = int(input("what number to search listssssss:" ))
if ser in fizzList:
    print("fizzList")
elif ser in buzzList:
    print("buzzList")
elif ser in both:
    print("both")
else:
    print("you dum")







    
