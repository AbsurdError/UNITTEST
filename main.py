def sum2(x, y):
    return x + y

def pos_or_neg(x):
    x = float(x)
    if x > 0:
        return 'positive'
    elif x < 0:
        return 'negative'
    else:
        return 'zero'


def check_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


def check_quantity(n):
    return len(str(n))


def sum_list(num):
    return sum(num)

def convert_date(date_str):
    parts = date_str.split('-')
    form_date = (parts[2], parts[1], parts[0])
    return form_date

def sum_list(str_list):
    n = 0
    for num_str in str_list:
        n += int(num_str)
    return n

def sum_of_elements(arr):
    first_sum = sum(arr[:len(arr) // 2])
    second_sum = sum(arr[len(arr) // 2:])
    return first_sum / second_sum

def combining_dictionaries(dct1, dct2):
    result = dct1.copy()
    result.update(dct2)
    return result



def dictionary_sum(dct):
    total_amount = 0
    for out_key, out_value in dct.items():
        for inner_key, inner_value in out_value.items():
            total_amount += inner_value
    return total_amount

def find_max_min(numbers):
    if not numbers:
        return None

    max_num = max(numbers)
    min_num = min(numbers)

    result = {'max': max_num, 'min': min_num}
    return result



def find_divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def found_divisors(numbers):
    result = []
    for num in numbers:
        result.append(find_divisors(num))
    return result

import random

def generate_without_repetition(N, start, end):
    if N <= 0 or start > end:
        return None

    num = [random.randint(start, end)]
    while len(num) < N:
        last_number = num[-1]
        next_number = random.randint(start, end)
        if next_number != last_number:
            num.append(next_number)

    return num



import random

def get_random_color():
    colors = ['red', 'green', 'blue', 'yellow', 'purple', 'orange', 'pink']
    return random.choice(colors)




def split_into_syllables(word):
    vowels = "aeiouyAEIOUY"
    syllables = []
    current_syllable = ""

    for char in word:
        if char in vowels:
            current_syllable += char
        else:
            current_syllable += char
            syllables.append(current_syllable)
            current_syllable = ""

    if current_syllable:
        syllables[-1] += current_syllable

    return syllables




import random
def shuffle_list(adding_values):
    shuf_list = adding_values.copy()
    random.shuffle(shuf_list)
    return shuf_list