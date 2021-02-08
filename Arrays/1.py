# Reverse the array or string
# Write a program to reverse an array or string

def reverse_input(inp):
    if not inp: return

    return inp[::-1]

if __name__ == '__main__':
    given_input = [1,2,3,4,5,6]
    reversed_input = reverse_input(given_input)
    print(reversed_input)