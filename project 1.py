decide=int(input("please insert program number \n 1-basic calculator \n 2- avarage for 3 numbers \n 3- cost for painting an appartment\n"))
if decide ==1:#البرنامج ده علشان اقدر اعمل عمليات حسابيه علي الارقام البسيطه زي الجمع والطرح والضرب والقسمه
    num1=float(input("please inupt first number"))
    num2=float(input("please input second number"))
    Sum=num1+num2
    Sub=num1-num2
    Mul=num1*num2
    print("the sum is",Sum)
    print("the sub is",Sub) 
    print("the mul is",Mul)
    if num2==0:
        print("the divisible cannoy be possible")
    else:
        div=float(num1/num2)
        print("the div is",div)
elif decide==2:#البرنامج ده علشان اقدر احسب معدل لاي عدد من الارقام ادخلها
    count=int(input("please insert number of numbers"))
    numbers=[]
    if count >0:
     for i in range(count):
          num=float(input("please insert number"))
          numbers.append(num)
     times=len(numbers)
     total=sum(numbers)
     av=total/times
     print("the avarage is",av)
    else:
        print("no numbers to calculate average")
elif decide==3:#البرنامج ده علشان اعرف احسب تكلفه دهان شقه هتساوي كام وبعمله اي
    lenth=float(input("please insert the length of the appartment "))
    width=float(input("please inssert the width "))
    payment=str(input("please insert the unit you will pay with "))
    cost=float(input("inter the cost per meter square "))
    area=lenth*width
    total_cost=area*cost

    print("the total cost will be ",total_cost ,payment)
