a = 0b0010101
b = 0b1011011

# 按位与运算
c = a & b
print(bin(c))
print("-" * 20)
# 按位或运算
d = a | b
print(bin(d))
print("-" * 20)
# 按位非运算
e = ~b
print(bin(e))
print("-" * 20)
# 按位抑或运算
f = a ^ b
print(bin(f))
print("-" * 20)
# 位左移运算
g = a << 2
print(bin(g))
print("-" * 20)
# 位右移运算
h = b >> 3
print(bin(h))