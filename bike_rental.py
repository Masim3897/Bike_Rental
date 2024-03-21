class BikeShop:
    def __init__(self, stock):
        self.stock=stock

    def DisplayBike(self):
        print("Total Bikes", self.stock)

    def rentForBike(self, q):
        if q < 0:
            print("please enter the positive value")
        elif q > self.stock:
            print("please enter the less than stock")
        else:
            print("Total prices", q * 100)
            print("Total bikes", self.stock)


while True:
    obj=BikeShop(100)
    uc=int(input('''
    1 Display Stock
    2 Rent a Bike
    3 Exit
    '''))
    if uc==1:
        obj.DisplayBike()
    elif uc==2:
        n=int(input("Enter the value"))
        obj.rentForBike(n)
    else:
        break
