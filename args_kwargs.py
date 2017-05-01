def args(name : str, *args):
    """Example function for args.

    The important part of *args is the asterisk. This tells python that
    to treat the arguments as a list.

    Args:
        name (str): The name of the user.
        *args: A vector of arguments


    Returns:
        Greets the user and prints the arguments.

    """
    print(f'hello {name}')

    for arg in args:
        print(arg)

print("First we test *args...")
args('Alan','salmon','eagle','beaver')

def kwargs(name : str, **kwargs):
    """Example function for kwargs.

    The important part of **kwargs is the double asterisks. They tell
    to expect a bunch of named arguments
    (eg. f(bird='eagle, fish='salmon')).

    Args:
        name (str): The name of the user.
        **kwargs: A dict of arguments and their names

    Returns:
        Greets the user and prints the arguments.

    """
    print(f'hello {name}')

    for key, value in kwargs.items():
        print(f'{key}: {value}')


print("\nnext, we test **kwargs")
kwargs(name='Lee',fish='tuna',bird='hawk',mammal='moose')