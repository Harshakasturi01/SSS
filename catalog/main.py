import json
from decimal import Decimal

def convert_to_base10(value, base):
    result = Decimal(0)
    power = Decimal(1)
    for digit in reversed(value):
        if digit.isdigit():
            digit_value = int(digit)
        else:
            digit_value = int(digit, 16)
        result += Decimal(digit_value) * power
        power *= Decimal(base)
    return result

def lagrange_interpolation_constant_term(x, y, k):
    constant_term = Decimal(0)
    for i in range(k):
        li = Decimal(1)
        for j in range(k):
            if i != j:
                li *= -x[j]
                li /= (x[i] - x[j])
        constant_term += y[i] * li
    return constant_term

def process_input(file_name):
    with open(file_name, 'r') as file:
        input_json = json.load(file)

    n = input_json["keys"]["n"]
    k = input_json["keys"]["k"]

    x = []
    y = []

    for key, value in input_json.items():
        if key != "keys":
            base = int(value["base"])
            value_str = value["value"]
            x.append(int(key))
            y.append(convert_to_base10(value_str, base))

    constant_term = lagrange_interpolation_constant_term(x, y, k)

    print(f"Constant term of the polynomial for {file_name}:", constant_term)

def main():
    process_input('input1.json')
    process_input('input2.json')

if __name__ == "__main__":
    main()
