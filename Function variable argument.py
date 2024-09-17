#create a function with variable length of argument
def my_function(* args):
    for arg in args:
        print(arg)


my_function('hello','welcome','to','python')