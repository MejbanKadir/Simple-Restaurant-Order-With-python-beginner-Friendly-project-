from colorama import Fore
#menu={
# "Pizza":40,
# "Burger":50,
# "Coffe":25,
# "Roll":35,
#}
total=[]
print(Fore.BLUE+"Welcome To Our Resturant",Fore.RESET)
print(" _________________________")
print("|Food:      Price:        |")
print("|1.Pizza      :40 BDT     |")
print("|2.Burger     :50 BDT     |")
print("|3.Coffe      :25 BDT     |")
print("|4.Roll       :35 BDT     |")
print("|_________________________|")
x=input("What Do You Want Sir?: ")

if x=='1':
	total.append(40)
elif x=='2':
	total.append(50)
elif x=="3":
	total.append(25)
elif x=="4":
	total.append(35)
print(total)	
y=input("Do You Want Something Else (y/n)")

if y=="n" or "N":
	print(f"Your Total Bill Is {total}BDT")
	exit()
print(" _________________________")
print("|Food:      Price:        |")
print("|1.Pizza      :40 BDT     |")
print("|2.Burger     :50 BDT     |")
print("|3.Coffe      :25 BDT     |")
print("|4.Roll       :35 BDT     |")
print("|_________________________|")
x2=input("What Do You Want Sir?: ")

if x2=='1':
	total.append(40)
elif x2=='2':
	total.append(50)
elif x2=="3":
	total.append(25)
elif x2=="4":
	total.append(35)
print(f"Sir your Total bill is {sum(total)} BDT")	