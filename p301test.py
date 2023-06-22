class Person:
    _money = 0
    greeting = 'hello'
    _favourites = {
        'dog': 'ferbie',
        'food': 'sushi',
    }

    def set_money(self, num):
        self.money = num
    
    def get_favourites(self):
        return self._favourites

    @property
    def money(self):
        return self._money
    
    @money.setter
    def money(self, num):
        self._money = num
    
    # def func_name(func):
    #     def decorator():
    #         print(func.__name__)
    #         func(self)
    #     return decorator
    
    # @func_name
    # def get_money(self):
    #     return(self.money)


chris = Person()
# print(chris._favourites['dog'])
# chris._favourites['food'] = [1,2]
# print(chris._favourites['food'])
# print(chris.money)
# chris.set_money(1)
# print(chris.money)
# print(chris.get_favourites())

print(chris.money)
chris.money = 100
print(chris.money)




def func_name(func):
    print('in func_name(), but outside decorator()')
    def decorator():
        print('inside decorator() inside func_name()')
        print(func.__name__)
        func()
        return 'decorator return statement'
    print('in func_name() after defining decorator')
    return decorator

@func_name
def money():
    print('inside money()')
    return('money() return')

print(money())

def func(f):
    print('func')
    def func_func():
        print('func_func')
    f()
    return func_func

def test():
    print('test')
    return('return statement inside test')

# test = func(test)
# print(test())
print(func(test)())

def func1(f):
    print('func1')
    def func_func1():
        print('func_func1')
    f()
    return func_func1

@func1
def test1():
    print('test1')
    return('return statement inside test1')

print(test1())



try:
    print('trying 1/0 :')
    total = 1/0
    print('will not print')
except Exception as err:
    print('there was an error:')
    print(err)
else:
    print('nothing went wrong :)')

print('out of try/except block')

try:
    print('trying 1/1 :')
    total = 1/1
    print('will print')
except Exception as err:
    print('there was an error:')
    print(err)
else:
    print('nothing went wrong :)')

print('out of try/except block')

# num1 = input('Please enter a number to double: ').lower().strip()
# try:
#     num1 = float(num1)
#     num1 *= 2
# except Exception as err:
#     print(f'Exception found: {err}')
#     print(f'{num1} is not a valid number')
# else:
#     print(num1)
# print('program done')

# while True:
    # num2 = input('Please enter a dividend number: ').lower().strip()
    # num3 = input('Please enter a divisor number: ').lower().strip()
    # try:
    #     num2 = float(num2)
    #     num3 = float(num3)
    #     result = num2 / num3
    # except ValueError:
    #     print(f'Either the dividend or divisor were not a valid number')
    # except ZeroDivisionError:
    #     print(f'Your divisor can not be 0')
    # except Exception as err:
    #     print(f'an exception of type {type(err)} was raised')
    #     continue
    # else:
    #     print(result)
    #     break
# print('program done')   


# regular function vs generator
def first_n(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums

sum_of_first_n = sum(first_n(1000000))
print(sum_of_first_n)

def gen_first_n(n):
    num = 0
    while num < n: 
        yield num
        num += 1

sum_of_first_n_gen = sum(gen_first_n(1000000))
print(sum_of_first_n_gen)
print(gen_first_n(10))
print(list(gen_first_n(10)))


