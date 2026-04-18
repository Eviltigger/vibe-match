# 控制流程示例

# 1. if-elif-else 条件判断
score = 85
if score >= 90:
    print("优秀！")
elif score >= 60:
    print("及格了！")
else:
    print("加油，下次会更好！")

# 2. for 循环 (遍历列表)
fruits = ["苹果", "香蕉", "樱桃"]
print("\n遍历水果列表:")
for fruit in fruits:
    print(f"我喜欢吃 {fruit}")

# 3. while 循环 (计数器)
print("\n使用 while 循环计数:")
count = 1
while count <= 3:
    print(f"当前计数: {count}")
    count += 1

# 4. range() 函数
print("\n使用 range() 打印 0 到 4:")
for i in range(5):
    print(i)
