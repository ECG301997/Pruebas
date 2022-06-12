# importar fizzbuzz
from fizz_buzz import FizzBuzz

# crear nuevo objeto
test_object = FizzBuzz()
test_list = test_object.fizzBuzz(100)
print(test_list)

def test_fizz():
    # multiplos de 3
    multiple_3 =[]
    for index, item in enumerate(test_list):
        if item == 'Fizz':
            multiple_3.append(index+1)
    return multiple_3


def test_buzz():
    multiple_5 = []
    for index,item in enumerate(test_list):
        if item == 'Buzz':
            multiple_5.append(index+1)
    return multiple_5


def test_fizz_buzz():
    multiple_15 = []    
    for index,item in enumerate(test_list):
        if item == 'Fizz Buzz':
            multiple_15.append(index+1)
    return multiple_15