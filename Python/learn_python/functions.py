# 函数的使用和定义

# 1. 定义一个简单的函数
def greet(name):
    """向指定的人打招呼"""
    return f"你好, {name}！欢迎学习 Python。"

# 调用函数
message = greet("同学")
print(message)

# 2. 带有默认参数的函数
def power(base, exponent=2):
    """计算幂运算，默认为平方"""
    return base ** exponent

print(f"5 的平方: {power(5)}")
print(f"2 的 3 次方: {power(2, 3)}")

# 3. 返回多个值的函数
def get_rectangle_info(length, width):
    """计算矩形的周长和面积"""
    perimeter = 2 * (length + width)
    area = length * width
    return perimeter, area

p, a = get_rectangle_info(10, 5)
print(f"矩形周长: {p}, 面积: {a}")
