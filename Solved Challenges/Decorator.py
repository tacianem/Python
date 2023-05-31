def make_pretty(func):
    def inner():
        # add some additional behavior to decorated function
        print("I got decorated")

        # call original function
        #func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")
    
ordinary()
# decorate the ordinary function
# decorated_func = make_pretty(ordinary)

# call the decorated function
# decorated_func()