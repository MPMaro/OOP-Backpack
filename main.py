
class Backpack:
    def __init__(self, color, size):
        print("Constructor")
        self.color = color
        self.size = size
        self.items = []
        self.open = False

    
    def openBag(self):
        print("Open")
        self.open = True
    
    def closeBag(self):
        print("Close")
        if self.open == True:
            self.open = False


    def putin(self, item):
        print("putIn")
        if self.open == True:
            self.items.append(item)
            print("Item Added Inside Backpack")
            print(self.items)


    def takeout(self, item):
        print("takeout")
        for x in range(len(self.items)):
            if self.open == True and item == self.items[x]:
                self.items.pop(x)
                print("Item Removed")
                print(self.items)
                
                
   # Task 2              
backpack_1 = Backpack("blue", "small")
backpack_2 = Backpack("red", "medium")
backpack_3 = Backpack("green", "large")

# Task 3 

backpack_1.openBag()
backpack_1.putin("Lunch")
backpack_1.putin("Jacket")
backpack_1.closeBag()
backpack_1.openBag()
backpack_1.takeout("Jacket")
backpack_1.closeBag()



