def print_params(msg, *numbers, **pairs):
    print("msg",msg)
######################


print_params("hello",1,2,3,4,"TEST",name="bob",age=13,5)

"""
OUTPUT:
_______________
msg hello
numbers:
1
2
3
4
TEST

pairs
key: name | value : bob
key: age | value :13
"""