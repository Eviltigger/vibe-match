# 大神级 Vibe Coding: Sam 的 Python 加密日记本

# 1. 设置登录密码
PASSWORD = "123"

# 2. 验证
print("--- 欢迎来到 Sam 的秘密 Vibe 空间 ---")
input_pass = input("请输入你的密码：")

if input_pass == PASSWORD:
    print(f"\n验证成功！今天有什么好玩的 Vibe 吗，Sam？")
    
    # 3. 记录 Vibe
    content = input("记录你的想法：")
    
    # 4. 自动保存（大神级：文件操作初探）
    with open("my_vibe.txt", "a") as f:
        f.write(f"Vibe: {content}\n")
    
    print("\n--- 记录已加密保存到 my_vibe.txt ---")
else:
    print("密码不对，你不是 Sam，撤退！")
