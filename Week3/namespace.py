class MyClass:
    def __init__(self, value):
        self.value = value

    def method1(self):
        print("This is method1 from MyClass.")

print("Class namespace:")
print(MyClass.__dict__)
