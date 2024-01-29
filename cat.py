import sys

def cat():
    print('Meow!')
def dog():
    print('Woof!')
def default():
    print('Hello',sys.argv[1])

def main():
    if sys.argv[1] == 'cat': 
        cat()
    else if:
        sys.argv[1] == 'dag'：
        dog()
    else:
        default()
if __name__ == '__main__':
    main()
