a, b, c = 1, 2, 3
print("a = ", a)
print("b = ", b)
print("c = ", c)
#
print("")
a, b, c = [1, 2, 3]
print("a = ", a)
print("b = ", b)
print("c = ", c)
#
print("")
a, b, c = (2 * i + 1 for i in range(3))
print("a = ", a)
print("b = ", b)
print("c = ", c)
#
print("")
a, (b, c), d = [1, (2, 3), 4]
print("a = ", a)
print("b = ", b)
print("c = ", c)
print("d = ", d)
#
print("")
a, b = 1, 2
a, b = b, a  # swapping
print("a = ", a)
print("b = ", b)
#
print("")
a, *b, c = [1, 2, 3, 4, 5]
print("a = ", a)
print("b = ", b)
print("c = ", c)
#
print("")
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("a        = ", a)
print("a[-1]    = ", a[-1])
print("a[-3]    = ", a[-3])
print("a[2:8]   = ", a[2:8])
print("a[-4:-2] = ", a[-4:-2])
print("a[::2]   = ", a[::2])
print("a[::3]   = ", a[::3])
print("a[2:8:2] = ", a[2:8:2])
#
print("")
#eof
