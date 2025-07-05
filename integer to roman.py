class IntegerToRoman:
    def __init__(self):
        self.val_to_roman = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]

    def convert(self, num: int) -> str:
        if not isinstance(num, int) or num < 1 or num > 3999:
            raise ValueError("Input must be an integer between 1 and 3999")

        roman_numeral = ''
        for value, symbol in self.val_to_roman:
            while num >= value:
                roman_numeral += symbol
                num -= value
        return roman_numeral

# Example usage
if __name__ == "__main__":
    converter = IntegerToRoman()
    try:
        number = int(input("Enter an integer (1-3999): "))
        roman_numeral = converter.convert(number)
        print(f"The Roman numeral for {number} is: {roman_numeral}")
    except ValueError as e:
        print(e)