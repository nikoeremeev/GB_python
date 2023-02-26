any_str = input("Введите текст или число: ")
if any_str.isdecimal():
    any_str = int(any_str)
    print(bin(any_str), oct(any_str), hex(any_str))
else:
    print(any_str.isascii())
