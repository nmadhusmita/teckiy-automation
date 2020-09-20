# # my_str = 'madam'
# #
# # my_str = my_str.casefold()
# #
# # # reverse the string
# # rev_str = reversed(my_str)
# #
# # # check if the string is equal to its reverse
# # if list(my_str) == list(rev_str):
# #  print ("The string is a palindrome.")
#
# # function which return reverse of a string
# # def isPalindrome(s):
# #   return s == s[::-1]
# # s = "madam"
#
#
# def is_leap_year(year):
#   if (year % 4) == 0:
#     if (year % 100) == 0:
#       if (year % 400) == 0:
#         print("It is a leap year")
#       else:
#         print("It is not a leap year")
#     else:
#       print("It is a leap year")
#   else:
#     print("It is not a leap year")
#
# is_leap_year(2016)
# is_leap_year(2019)


# def hello(attr1, attr2, attr3, attr4):
#   print(attr1 + attr2 + attr3 + attr4)
#
#
# hello('Teckiy','how','are','you')


# def read_a_test_file(file_name):
#     f = open(file_name, "r")
#     f = open(file_name, "w")
#     print(f.read())
#     print(f.write())
#
#
# read_a_test_file("C:\Code\Demo.txt")


# def read_a_test_file(file_name):
#     f = open(file_name, "r")
#     print(f.read())
#
# read_a_test_file("C:\Code\Demo.txt")


# def write_a_test_file(file_name):
#     f = open("file_name", "w")
#     f.write("proud to be Indian")
#     print(f.write())


def highest(arr):
  if arr is None:
      print("Invalid Input Array")
      return

  largest_value = arr[0] #
  for i in arr:
    if i > largest_value: # 2 > 1
        largest_value = i
  print (largest_value)

highest(None)

highest([1,2,3,10,5])





