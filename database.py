import qrcode
import math
PRODUCT=[]


def read_from_database():
    f=open("my-project\session_7\database.txt" , "r") 
    for line in f.readlines():
        result=line.split(",")
        my_dict={"code": result[0] , "name": result[1] , "price": result[2] , "count": result[3]}
        PRODUCT.append(my_dict)
    f.close()

def QRcode():
   code=input("enter the code: ")
   for product in PRODUCT:
     if code== product["code"]:
        img=qrcode.make(product["code"]+ "|" + product["name"] + "|" + product["price"] + "|" + product["count"])
        img.save("QRcode.png")
   

def write_to_database():
    f=open("my-project\session_7\database.txt" , "w")
    for product in PRODUCT:
       f.write(product["code"])
       f.write(",")
       f.write(product["name"])
       f.write(",")
       f.write(product["price"])
       f.write(",")
       f.write(product["count"])
    f.close()


def show_menu():
    print("1- Add")
    print("2- Edit")
    print("3- Remove")
    print("4- Search")
    print("5- Show list")
    print("6- buy")
    print("7- QRcode")
    print("8- exit")
for product in PRODUCT:
    print(product)

def add():
    code = input("enter code: ")
    name= input("enter name: ")
    price= input("enter price: ")
    count= input("enter count: ")
    new_product={"code":code , "name": name , "price": price , "count": count}
    PRODUCT.append(new_product)
    for product in PRODUCT:
        print(product)
    

def edit():
    choose=0
    code=input("enter the code: ")
    for product in PRODUCT:
        if code== product['code']:
         print("1- name")
         print("2- price")
         print("3- count")
         choose=int(input("which one do you wanna edit? "))
         if choose==1:
            new=input("enter new name: ")
            product["name"]=new
            print(product)
            print("update succesfully")
            break
         elif choose==2:
            new=input("enter new price: ")
            product["price"]=new
            print(product) 
            print("update succesfully")  
            break
         elif choose==3:
            new=input("enter new count: ")
            product["count"]=new
            print(product)
            print("update succesfully")
            break

    else:
          print("the code not found")
    

def remove():
    
    code = input("enter the code: ")
    for product in PRODUCT:
        if product["code"]==code:
            product.pop("code")
            product.pop("name")
            product.pop("price")
            product.pop("count")
            print(product)
            break
    else:
           print("this product not found")
       

def search():
    user_input=input("enter key word: ")
    for product in PRODUCT:
        if user_input==product["code"] or user_input==product["name"]:
          print(product["code"] , "\t" , product["name"] , "\t" , product["price"] , "\t" , product["count"])  
          break
    else:
        print("not found")
    

def show_list():
    print("code\tname\tprice\tcount")
    for product in PRODUCT:
        print(product["code"] , "\t" , product["name"] , "\t" , product["price"] , "\t" , product["count"])


def buy():
    cart=0
    i=1
    factor_price=0
    while i==1:
        user_code=input("enter the code of the product that you wanna to buy: ")
        for product in PRODUCT:
            if user_code== product["code"]:
                print("the product is exist in the store")
                number=int(input("how many will you wanna to buy? "))
                if number > int(product["count"]):
                    print("Sorry,there are not enouph of this product")
                    break
                elif number <=int(product["count"]):
                    factor_price = factor_price + number*int((product["count"]))
                    product["count"]=int(product["count"]) - number
                    cart=cart+number
                    break
        else:
                print("Sorry,the product is not exist in the store")

        i=int(input("if you wanna buy another product enter 1 else enter 0: "))
           
    print("price that you should pay: " , factor_price)
    print("sum of the products that buy them: " , cart)  
    

print("WELCOME TO THIS MENU")
print("loading...")
read_from_database()
print("data loaded")

while 1==1:

    show_menu()

    user_choice=int(input("Enter your choice: "))
    if user_choice==1:
        add()
    elif user_choice==2:
        edit()
    elif user_choice==3:
        remove()
    elif user_choice==4:
        search()
    elif user_choice==5:
        show_list()
    elif user_choice==6:
        buy()
    elif user_choice==7:
        QRcode()
    elif user_choice==8:
        write_to_database()
        exit(0)