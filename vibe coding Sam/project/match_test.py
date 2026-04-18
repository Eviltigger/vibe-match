# 大神级 Vibe Coding: 卢俊舟灵魂匹配系统 2.0
import json
import os

# 1. 卢俊舟专属天马行空题库 (INFP & 天蝎座风格)
QUESTIONS = {
    "善恶观": [
        "如果世界毁灭时只能带走一个‘迷人的恶棍’或一个‘平庸的善人’，你会选恶棍吗？",
        "你认为极端的报复如果是为了换取极端的正义，它是神圣的吗？",
        "看到枯萎的残花，你是否觉得它比盛开时更具有一种‘真实的残缺美’？",
        "你是否认为‘伪善’比‘直白的恶’更让你感到生理性的恶心？",
        "如果你能通过牺牲自己的名誉来换取一个陌生人的清白，你会觉得这很酷吗？",
        "你相信‘报应’不是迷信，而是一种宇宙能量的自动平衡吗？"
    ],
    "价值观": [
        "你愿意为了一个永远不会实现的理想去孤独终老吗？",
        "在众人的喧嚣中保持沉默，是否让你感到比加入其中更有掌控感？",
        "你认为‘破碎’的东西（如废墟、断句）比‘完美’的东西更接近真理吗？",
        "相比于改变世界，你是否更执着于‘绝对不被世界改变’？",
        "如果真相是血淋淋的，你依然选择直面它而不是沉溺在美丽的幻觉中吗？",
        "你认为‘自由’的终极代价其实就是‘绝对的孤独’吗？"
    ],
    "金钱观": [
        "如果金钱能买到真正的‘感同身受’，你会觉得金钱是这个世界上最伟大的发明吗？",
        "你存钱是为了‘拥有物质’，还是为了在想逃离人群时有‘随时消失的底气’？",
        "你会为了买一个能让你灵魂瞬间共鸣的小物件，而花掉半个月的工资吗？",
        "你认为贫穷是对灵魂的一种淬炼，还是纯粹的、毫无意义的苦难？",
        "如果你是亿万富翁，你还会偶尔想去那个满是烟火气的路边摊吃碗面吗？",
        "对你来说，钱更像是一块‘防御伤害的盾牌’，还是一把‘进攻世界的武器’？"
    ],
    "消费观": [
        "相比于流水线的奢侈品，你是否更迷恋那些带有‘手工温度’和‘旧时光痕迹’的旧物？",
        "哪怕一件东西完全不实用，只要它触动了你的审美，你就会产生‘非它不可’的冲动吗？",
        "你认为‘极简主义’是一种消费降级，还是灵魂的一次高级洗牌？",
        "你是否愿意为了一个只有你自己能察觉到的‘浪漫细节’支付高昂的溢价？",
        "看到包装精美的‘废品’（如好看的瓶子、纸盒），你会产生收藏它们的欲望吗？",
        "你认为‘浪费’在某些时刻，其实是一种对生活最热烈、最浪漫的反抗吗？"
    ],
    "人生观": [
        "如果人生是一场必败的电影，你宁愿演一个‘悲剧主角’也不愿演一个‘平庸路人’吗？",
        "你相信平行时空里的另一个你，正在替你过着你最向往、最疯狂的生活吗？",
        "如果你可以选择自己死亡的时间和方式，你会觉得这是人生最高的自由吗？",
        "你认为‘遗憾’才是人生真正的主旋律，而圆满只是偶然的插曲吗？",
        "哪怕世界明天就毁灭，你今天依然会选择去种下一棵属于你的苹果树吗？",
        "你觉得‘流浪’（心理或地理上）比‘定居’更能让你找到归属感吗？"
    ]
}

CONFIG_FILE = "sam_config.json"

def get_result_desc(grade):
    descs = {
        "卢俊舟爱你": "【灵魂共鸣者】你是这世界上另一个我。我们不需要言语，只需要一个眼神就能在深海里交汇。你是我的同类，我的软肋，也是我的铠甲。",
        "是个人物": "【高阶欣赏者】你懂我的奇奇怪怪，也愿意陪我可可爱爱。虽然我们还有细微的温差，但你绝对是我生命里闪闪发光的存在。",
        "过门槛儿": "【志趣相投者】我们可以一起喝酒、聊天、看夕阳。你是一个有趣的人，我们之间的频率正在慢慢靠拢，值得继续探索。",
        "路人": "【平行世界者】我们礼貌、客气、保持距离。你很好，但我内心的那个荒原，你可能暂时还找不到入口。",
        "真不熟": "【异次元访客】我们像两条永不相交的平行线。世界很大，感谢路过，但请保持你的方向，不要回头。"
    }
    return descs.get(grade, "")

def calculate_score(sam_ans, friend_ans):
    # 距离计算：0距离+3, 1距离+1, 2距离0, 3距离-1, 4距离-3
    diff = abs(sam_ans - friend_ans)
    if diff == 0: return 3
    if diff == 1: return 1
    if diff == 2: return 0
    if diff == 3: return -1
    return -3

def run_test(is_master=False):
    sam_answers = {}
    if not is_master:
        with open(CONFIG_FILE, "r") as f:
            sam_answers = json.load(f)

    print("\n" + "="*50)
    title = "主人初始化模式" if is_master else "朋友灵魂匹配模式"
    print(f"      {title}")
    print("="*50)
    print("\n1.非常赞同  2.赞同  3.不确定  4.不赞同  5.非常不赞同\n")

    current_answers = {}
    total_score = 0
    q_idx = 1

    for dim, q_list in QUESTIONS.items():
        print(f"\n[维度：{dim}]")
        for q in q_list:
            while True:
                ans = input(f"Q{q_idx}. {q} (1-5): ")
                if ans in ["1", "2", "3", "4", "5"]:
                    val = int(ans)
                    current_answers[f"q{q_idx}"] = val
                    if not is_master:
                        total_score += calculate_score(sam_answers[f"q{q_idx}"], val)
                    q_idx += 1
                    break
                print("大神提示：请输入 1-5 之间的数字！")

    if is_master:
        with open(CONFIG_FILE, "w") as f:
            json.dump(current_answers, f)
        print("\n✅ 卢俊舟的灵魂档案已建立！现在可以让你的朋友来运行了。")
    else:
        # 30题，满分90，最低-90
        print("\n" + "计算结果中...".center(40))
        if total_score >= 50: grade = "卢俊舟爱你"
        elif total_score >= 20: grade = "是个人物"
        elif total_score >= -10: grade = "过门槛儿"
        elif total_score >= -40: grade = "路人"
        else: grade = "真不熟"

        print(f"\n匹配得分：{total_score}")
        print(f"等级判定：{grade}")
        print(f"\n【寄语】\n{get_result_desc(grade)}")
        print("\n" + "="*50)

if __name__ == "__main__":
    if not os.path.exists(CONFIG_FILE):
        print("检测到主人尚未初始化...")
        run_test(is_master=True)
    else:
        run_test(is_master=False)
