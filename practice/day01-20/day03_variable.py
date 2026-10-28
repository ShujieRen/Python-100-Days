"""
Learning Python Variables

Author: Rich
Date: 2026-10-24

"""

#%% 变量种类：int, float, str, bool
print(0b100)
print(0o100)
print(100)
print(0x100)

print(123.456)
print(1.23456e2)

print('100')

#%% 变量的创建和使用
a = 45
b = 12

print(a + b)
print(a - b)
print(a * b)

# %% 使用type()函数检查变量类型
a = 100
b = 100.1
c = 'hello'
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# %% 变量转换
a = 100
b = 123.85
c = '123'
d = '100'
e = '123.45'
f = 'hello'
g = True

print(float(a))
print(int(b))
print(int(c))
print(int(c, base=16))
print(int(d, base=2))
print(float(e))
print(bool(f))
print(int(g))
print(chr(a))
print(ord('d'))

# %%
