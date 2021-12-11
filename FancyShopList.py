class ShopList
    def __init__(self, foodName, foodAmount):
        self.__foodName = foodName
        self.__foodAmount = foodAmount
        self.__foodPrice = self.__Price()
        self.__calculator = self.calcshoplist()

    def __Price(self):
        if self.__foodName == "Dry Cured Iberian Ham":
            self.__foodPrice = 177.80
        elif self.__foodName == "Wagyu Steaks ":
            self.__foodPrice = 450.00
        elif self.__foodName == "Matsutake Mushrooms":
            self.__foodPrice = 272.00
        elif self.__foodName == "Kopi Luwak Cofee":
            self.__foodPrice = 306.50
        elif self.__FoodName == 'Moose Cheese':
            self.__FoodPrice = 487.20
        elif self.__FoodName == 'White Truffles':
            self.__FoodPrice = 3600.00
        elif self.__FoodName == 'Blue Fin Tuna':
            self.__FoodPrice = 3603.30
        elif self.__FoodName == 'Le Bonnotte Potatoes':
            self.__FoodPrice = 270.81
        else:
            self.__FoodPrice = 0.00

        return self.__foodPrice

    def calcshoplist(self):
        self.calculator = self.__foodAmount * self.__foodPrice