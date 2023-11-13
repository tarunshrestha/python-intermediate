def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum
print(add(2, 3, 4, 5))

def calculator(i, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key) # print(kwargs['add']
    #     print(value)
    i += kwargs["add"]
    i *= kwargs["multiply"]
    print(i)

calculator(0, add=3, multiply=2)

class DemoCar:
    def __init__(self, **kw):
        self.name=kw['name']
        self.model=kw.get('model') #Wont give error only shows None

car =DemoCar(name = "Tata", model = 1145)
print(car.name)