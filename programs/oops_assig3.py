class Parent1:
    def show(self):
        print("Parent1 method")

class Parent2:
    def show(self):
        print("Parent2 method")

class Child(Parent1, Parent2):
    def show(self):
        super().show()
        Parent1.show(self)
        Parent2.show(self)

child = Child()
child.show()

print(Child.mro())
