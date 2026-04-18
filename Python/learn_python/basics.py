# 基础变量和数据类型

# 1. 整数 (Integer)
age = 25
# 在插槽 {} 里甚至可以做加减法！
print(f"明年我就 {age + 1} 岁了，十年后是 {age + 10} 岁。")

# 2. 浮点数 (Float)
height = 1.75
print(f"身高: {height}, 类型: {type(height)}")

# 3. 字符串 (String)
name = "Python 学习者"
print(f"名字: {name}, 类型: {type(name)}")

# 4. 布尔值 (Boolean)
is_learning = True
print(f"是否正在学习: {is_learning}, 类型: {type(is_learning)}")

# 5. 列表 (List) - 可以存放多个数据
skills = ["Python", "Java", "C++"]
print(f"技能列表: {skills}, 类型: {type(skills)}")

# 练习：修改上面的变量，或者添加你自己的变量
age = 72
print(f"小珍有{age + (age-40)}个男朋友")
a = (1, 2)  # 圆：元组
b = [1, 2]  # 方：列表
c = {"a": 1} # 花：字典