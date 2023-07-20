def tensDigit(number):
    number //= 10
    return number % 10


def tenDigitSorting(array):
    array.sort(key=lambda x: (tensDigit(x), -x))

    return array


if __name__ == "__main__":
    A = list(map(int, input().strip('[').strip(']').split(',')))

    print(tenDigitSorting(A))
