import time 

def cache(func):
    cache_value={}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result=func(*args)
        cache_value[args]=result
        return result
    return wrapper

@cache
def time_taking_function(a,b):
    time.sleep(3)
    return a*b

print(time_taking_function(5,6))
print(time_taking_function(5,7))
print(time_taking_function(5,6))
print(time_taking_function(5,7))