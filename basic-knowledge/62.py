# error2


def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')

try:
    foo(2)
except ValueError as e:
    print('ValueError')
except UnicodeError as e:
    print('UnicodeError')



