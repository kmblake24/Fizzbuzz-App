def fizzbuzz(a):
    a = int(a)
# do this b/c fizzbuzz.py will be a string input - this
# will change it to an int which is needed for the function

    if (a % 3 == 0) and (a % 5 == 0):
        print('fizzbuzz')
    elif a % 5 == 0:
        print('buzz')
    elif (a % 3 == 0):
        print('fizz')
    else:
        print(a)
