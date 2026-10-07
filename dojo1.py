<<<<<<< HEAD
import sys

def main():
    # Read space-separated integers from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    a, b, c, d = map(int, input_data)
    
    # Python's // truncates towards negative infinity, so int(d / a) is used 
    # to truncate towards zero (standard integer division for negative numbers)
    result = a + (b * c) - int(d / a)
    
    print(result)

if __name__ == '__main__':
=======
import sys

def main():
    # Read space-separated integers from standard input
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    a, b, c, d = map(int, input_data)
    
    # Python's // truncates towards negative infinity, so int(d / a) is used 
    # to truncate towards zero (standard integer division for negative numbers)
    result = a + (b * c) - int(d / a)
    
    print(result)

if __name__ == '__main__':
>>>>>>> 0981ad8685c870ca7bf0ce4be72d496e180f8ead
    main()