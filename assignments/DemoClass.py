# # class test:
# #     def __init__(self):
# #         print("Test")
# #
# # t = test()
# from pdoc.cli import args
#
#
# def concat(*str, sep="/"):
#      print(sep.join(str))
#
#
# concat('hello', 'how', 'are', 'you')


def convertTuple(tup):
    str = ' '.join(tup)
    return str

tuple = ('Teckiy','how','are','you')
str = convertTuple(tuple)
print(str)


def convertTupleBySeparator(tup, separator):
    str = separator.join(tup)
    return str

tuple = ('Teckiy','how','are','you')
str = convertTupleBySeparator(tuple)
print(str)



