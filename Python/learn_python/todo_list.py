# 综合小项目：简易待办事项管理器 (Todo List)

def show_menu():
    print("\n--- 简易待办事项管理器 ---")
    print("1. 查看任务")
    print("2. 添加任务")
    print("3. 删除任务")
    print("4. 退出")

def main():
    todos = []
    while True:
        show_menu()
        choice = input("请选择操作 (1-4): ")

        if choice == '1':
            print("\n你的任务列表:")
            if not todos:
                print("目前没有任务。")
            else:
                for idx, task in enumerate(todos, 1):
                    print(f"{idx}. {task}")
        
        elif choice == '2':
            task = input("请输入要添加的任务: ")
            todos.append(task)
            print("任务添加成功！")
        
        elif choice == '3':
            if not todos:
                print("没有任务可以删除。")
                continue
            try:
                idx = int(input("请输入要删除的任务编号: "))
                if 1 <= idx <= len(todos):
                    removed = todos.pop(idx - 1)
                    print(f"已删除任务: {removed}")
                else:
                    print("无效的编号。")
            except ValueError:
                print("请输入有效的数字。")
        
        elif choice == '4':
            print("再见！祝你学习进步。")
            break
        
        else:
            print("无效选择，请重新输入。")

if __name__ == "__main__":
    # 注意：由于是在非交互式环境下，我们这里不直接运行主循环，
    # 而是作为示例代码展示。你可以尝试在本地终端运行这个文件。
    print("这是一个待办事项管理器的示例代码。")
    print("你可以通过运行 `python3 todo_list.py` 来体验它。")
    # main() # 在实际交互式终端中取消注释以运行
