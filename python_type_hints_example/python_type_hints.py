from typing import Union


# using type hints using union
def give_age(age: Union[int], name: str = 'rajnish') -> str:
    return "age of {} is {}".format(name, age)


print(give_age(89))
print(give_age(56,'deepesh'))


# here age can be int or string
def give_age(age: Union[int,str], name: str = 'rajnish') -> str:
    return "age of {} is {}".format(name, age)


print(give_age('89'))
print(give_age(56,'deepesh'))


# using simple type hints
def give_age(age: int, name: str = 'rajnish') -> str:
    return "age of {} is {}".format(name, age)


print(give_age(89))
print(give_age(56,'deepesh'))
