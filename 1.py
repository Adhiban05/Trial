hello git hub

2nd line
class Person:
    mylist = ["3", "5", "1"]

    def operation(self, value):
        if value == "1":
            u = input("Enter the element to be added: ")
            self.mylist.append(u)
            print(self.mylist)
        elif value == "2":
            print(self.mylist)
            e = input("Enter the element to be removed: ")
            self.mylist.remove(e)
            print(self.mylist)
        elif value == "3":
            print("Current list is: " + str(self.mylist))
        elif value == "4":
            self.mylist.sort()
            print("Sorted list is: " + str(self.mylist))
        elif value == "5":
            d = len(self.mylist)
            print("Length of the list is: " + str(d))
        else:
            print("Invalid case")

    def run(self):
        while True:
            case = input("Enter a case (1-5) or any other key to exit: ")
            self.operation(case)

person = Person()
person.run()

                                        
