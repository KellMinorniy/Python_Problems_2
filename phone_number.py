def wrapper(f):
    def fun(l):
        formatted_numbers = []
        for number in l:
            digits = ''.join(filter(str.isdigit, number))
            if digits.startswith('8'):
                digits = '7' + digits[1:]
            if digits.startswith('0'):
                digits = digits[1:]
            formatted_number = f"+7({digits[:3]}){digits[3:6]}-{digits[6:8]}-{digits[8:]}"
            formatted_numbers.append(formatted_number)
        return sorted(formatted_numbers)
    return fun

@wrapper
def sort_phone(l):
    return l

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    print(*sort_phone(l), sep='\n')