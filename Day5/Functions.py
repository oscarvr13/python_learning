#Here we only define the function, we need to call it
def say_hello():
    '''
    This function returns a hello
    :return:
    '''
    print("Hola")


def say_hello_to(name):
    '''
    This functions say hello to name
    :param name: The name of the person we want to say hello
    :return:
    '''
    print(f"Hello {name}")


say_hello()
say_hello_to("Javier")


#How to define the parameters in the function
def multiply(number1, number2):
    total = number1 * number2
    return total

result = multiply(100, False)
print(result)

