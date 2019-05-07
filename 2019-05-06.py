# 2019-05-06
# Python Data Types
print(123456789012345678901234567890123456789012345678 + 1)
print(type(123456789012345678901234567890123456789012345678))
# octal 
print(0o10)
print(0O10)
print(type(0o10))
# hexadecimal 
print(0x10)
print(0X10)
print(type(0x10))
# binary
print(0b10)
print(0B10)
print(type(0b10))
# float 
print(type(9.9))
print(type(9e9))
print(4.2e-4)
print(1.79e308)
print(1.8e308)   # positive infinity 
print(5e-324)
print(1e-325)    # negative infinity 
# complex numbers
print(1+1j)
print(type(1+1j))
# strings 
print("this is a string")
print('this is also a string')
print("This string contains a single quote (') character.")
print('This string contains a double quote (") character.')
# escape sequences in strings 
print('This string contains a single quote (\') character.')
print("This string contains a double quote (\") character.")
print('foo\\bar')   # including a backslash 
# special escape sequences 
print('foo\tbar')
print("a\141\x61")
print("a\nb")
print('\u2192 \N{rightwards arrow}')
# raw strings 
print(R'foo\\bar')
# triple-quoted strings 
print('''This string has a single (') and a double (") quote.''')
# Boolean Type, Boolean Context, and “Truthiness”
print(type(True))
print(type(False))
