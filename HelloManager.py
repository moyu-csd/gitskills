//this is a test
class HelloManager:
    def __init__(self, date, money, category, note):
        self.date = date
        self.money = money
        self.category = category
        self.note = note

bill = []

while True:
    print("=================================")
    print("欢迎使用个人账单管理系统")
    print("=================================")
    print("请选择操作：")
    print("1. 记录收入")
    #print("3. 查看所有账单（第三周任务添加）")
    #print("4. 查询账单（第三周任务添加）")
    print("2. 记录支出")
    print("5. 退出系统")

    a = input("请输入选项序号：")

    if a == "1":
        date = input("日期（Year-Month-Date）：")
        money = float(input("金额："))
        if money <= 0:
            print("收入金额必须为正数。")
            continue
        category = input("类别（如工资、奖金等）：")
        note = input("备注：")
        bill.append(HelloManager(date, money, category, note))
        print("收入已成功记录！")
    elif a == "2":
        date = input("日期（Year-Month-Date）：")
        money = float(input("金额："))
        if money <= 0:
            print("支出金额必须为正数。")
            continue
        category = input("类别（如餐饮、交通、购物等）：")
        note = input("备注：")
        bill.append(HelloManager(date, -money, category, note))
        print("支出已成功记录！")
    #elif a == "3":
        #print("所有账单信息如下：")
        #for bill in bills:
            #sign = "收入" if bill.money > 0 else "支出"
            #print(f"{bill.date}，{sign}，金额：{bill.money}，类别：{bill.category}，备注：{bill.note}")
    #elif choice == "4":
        # 第三周任务添加，暂不实现查询功能
        #print("查询功能暂未实现。")
    elif a == "5":
        print("再见！")
        break
    else:
        print("无效选项，请重新输入。")
