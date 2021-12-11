from ShopListBH import theShopList

def ShopListloop
    li = []
    count = 0

    while count <1:
        count = int(input("insert amount of items to buy"))
        if (count < 1):
            print("item bought must be atleast 1")

    for i in range(count):
        print(f"item #{i + 1}-")
        food_name = str(input("insert food name: "))
        food_amount = 0
        while food_amount <= 0:
            food_amount = float(input("Enter amount of pounds: "))
            if food_amount <= 0:
                print("insufficient fund")

        li.append(theShopList(food_name, food_amount))

    return li

def ShowList(resultlist):
    print("Here are the items you have purchased: \n")
    for theShopList in resultlist:
        print(f"Item: {theShopList.getNameBH()}")
        print(f"Amount ordered in pounds: {theShopList.getAmountBH():.1f}")
        print(f"Price per pound: ${theShopList.getPriceBH():.2f}")
        print(f"Price of order: ${theShopList.getcountBH():.2f}")

def TotalList(thelist):
    total = 0
    for i in thelist:
        total = i.getcountBH() + total
    print("Here is your bill : ${:.2f}.".format(total), "Thankyou you for purchasing")

def main():
    thelist = ShopListloop()
    ShowList(thelist)
    TotalList(thelist)


main()