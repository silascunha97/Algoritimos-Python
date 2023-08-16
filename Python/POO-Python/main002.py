class A:
    fasgas = 123
    
    def __init__(self):
        self.fasgas = 321
a1= A()
a2= A()

A.fasgas = 321


print(a1.__dict__)
print(A.__dict__)
print(a1.fasgas)
print(a2.fasgas)

