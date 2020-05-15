from helpers import fizzbuzz

exit_status = ''
# will give the option to exit the loop or continue
while exit_status != 'q':
    ans = input("What is your input: ") #ans is a string
    fizzbuzz(ans)
    # or do 
    # fizzbuzz(int(ans))
    # and you wouldn't have to do a = int(a) in helpers
    exit_status = input("Type any key to continue. Type q to quit: ")