

def greet(message):
    if type(message) not in [str]:
        raise TypeError('Message must be in string format')
    return "Hello world!"



