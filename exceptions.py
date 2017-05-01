"""
16. Exceptions
Exception handling is an art which once you master grants you immense
powers. I am going to show you some of the ways in which we can handle
exceptions.

In basic terminology we are aware of try/except clause. The code which
can cause an exception to occur is put in the try block and the
handling of the exception is implemented in the except block.
"""

try:
    file = open('test.txt', 'rb')
except IOError as e:
    print(f'16.0 An IOError occured. {e.args[-1]}')

### 16.1 HANDLING MULTIPLE EXCEPTIONS #################################
# Option A: Tuples full of exceptions
try:
    file = open('test.txt', 'rb')
except (IOError, EOFError) as e:
    print(f'16.1.A An error occured. {e.args[-1]}')

# Option B: Multiple except blocks
try:
    file = open('test.txt', 'rb')
except EOFError as e:
    print('16.1.B An EOF error occurred.')
    raise e
except IOError as e:
    print('16.1.B An error occured.')
    raise e

# Option C: Trapping all exceptions
try:
    file = open('text.txt', 'rb')
except Exception:
    # Todo: handle the error
    raise

### 16.1.1 FINALLY CLAUSE #############################################
#: The code in the finally clause will run whether or not an error has
#: occured. It is for code that **must** run, even if your procedure is
#: borked during the try clause (eg. closing a thread lock).
try:
    file = open('test.txt', 'rb')
except IOError as e:
    print('An IOError occurred. {}'.format(e.args[-1]))
finally:
    print("This would be printed whether or not an exception occurred!")

# Output: An IOError occurred. No such file or directory
# This would be printed whether or not an exception occurred!

### 16.1.2 TRY/ELSE CLAUSE
#: This code runs if no exceptions occur in the try clause, and errors
#: within it are not trapped.
try:
    # Error trapped code
    print('I am sure no exception is going to occur!')
except Exception:
    # Exception handling from the try clause
    print('exception')
else:
    # Only run this if no error occured - do not error trap.
    print('This would only run if no exception occurs. And an error here '
          'would NOT be caught.')
finally:
    # Execute this no matter what errors occured after the try/except/else.
    print('This would be printed in every case.')

# Output: I am sure no exception is going to occur!
# This would only run if no exception occurs.
# This would be printed in every case.