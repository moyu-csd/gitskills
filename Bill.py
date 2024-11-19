'''
这个程序定义了Bill和BudgetManager两个类，Bill(账单)类用于创建账单对象并提供打印账单的方法，而BudgetManager(预算管理员)类则用于管理帐单，
包括添加账单、显示账单和按日期查询账单的功能。
'''

# 引入 datetime 模块，用于日期格式验证
from datetime import datetime

class Bill:
    # 账单的构造函数，接受日期、金额、类别、备注和是否为收入等参数
    def __init__(self, date, amount, category, note, is_income=True):
        self.date = date
        self.amount = amount
        self.category = category
        self.note = note
        self.is_income = is_income

    # 账单的 str 方法，用于打印账单信息
    def __str__(self):
        if self.is_income:
            return f"日期: {self.date}   金额: {self.amount}   类别: {self.category}   备注: {self.note}"
        else:
            return f"日期: {self.date}   金额: {self.amount}   类别: {self.category}   备注: {self.note}"


class BudgetManager:
    # 账单管理器的构造函数，初始化收入账单和支出账单列表
    def __init__(self):
        self.income_bills = []   # 收入账单列表
        self.expense_bills = []  # 支出账单列表

    # 辅助方法，用于验证日期格式是否正确
    def is_valid_date(self, date_text):
        try:
            datetime.strptime(date_text, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    # 辅助方法，用于获取有效的日期输入
    def get_valid_date_input(self, prompt):
        while True:
            date = input(prompt)
            if self.is_valid_date(date):
                return date
            else:
                print("日期格式不正确，请使用 YYYY-MM-DD 的格式。")

    # 辅助方法，用于获取有效的金额输入
    def get_valid_amount_input(self, prompt):
        while True:
            try:
                amount = float(input(prompt))
                if amount <= 0:
                    print("金额必须为正数，请重新输入。")
                else:
                    return amount
            except ValueError:
                print("无效的金额，请输入一个数字。")

    # 添加收入账单的方法
    def add_income(self, date, amount, category, note):
        if amount <= 0:
            print("收入金额必须为正数")
            return
        self.income_bills.append(Bill(date, amount, category, note, True))

    # 添加支出账单的方法
    def add_expense(self, date, amount, category, note):
        if amount <= 0:
            print("支出金额必须为正数")
            return
        self.expense_bills.append(Bill(date, amount, category, note, False))

    # 显示所有账单的方法
    def display_all(self):
        print("收入记录:")
        for bill in self.income_bills:
            print(bill)
        print("\n支出记录:")
        for bill in self.expense_bills:
            print(bill)

    # 根据日期查询账单的方法
    def query_by_date(self, date):

        def match_date(bill):
            return bill.date == date

        income_matches = [bill for bill in self.income_bills if match_date(bill)]
        expense_matches = [bill for bill in self.expense_bills if match_date(bill)]

        if income_matches:
            print(f"日期 {date} 的收入记录:")
            for bill in income_matches:
                print(bill)

        if expense_matches:
            print(f"日期 {date} 的支出记录:")
            for bill in expense_matches:
                print(bill)


    def main_menu(self):
        # 主菜单循环，允许用户选择操作
        while True:
            print("============================")
            print("   欢迎使用个人账单管理系统")
            print("============================")
            print("请选择操作:")
            print("1. 记录收入")
            print("2. 记录支出")
            print("3. 查看所有账单")
            print("4. 按日期查询账单")
            print("5. 退出系统")
            choice = input("请输入选择序号(1-5): ")

            # 根据用户的选择执行相应操作
            if choice == '1':
                print("请输入收入信息:")
                date = self.get_valid_date_input("输入日期(YYYY-MM-DD): ")
                amount = self.get_valid_amount_input("输入金额: ")
                category = input("输入类别(如工资、奖金等): ")
                note = input("输入备注(可选): ")
                self.add_income(date, amount, category, note)
                print("收入已成功记录！")
                esc = input("按回车键返回主菜单...")
            elif choice == '2':
                print("请输入支出信息:")
                date = self.get_valid_date_input("输入日期(YYYY-MM-DD): ")
                amount = self.get_valid_amount_input("输入金额: ")
                category = input("输入类别(如餐饮、交通、购物等): ")
                note = input("输入备注(可选): ")
                self.add_expense(date, amount, category, note)
                print("支出已成功记录！")
                esc = input("按回车键返回主菜单...")
            elif choice == '3':
                self.display_all()
                esc = input("按回车键返回主菜单...")
            elif choice == '4':
                date = input("输入查询日期(YYYY-MM-DD): ")
                self.query_by_date(date)
                esc = input("按回车键返回主菜单...")
            elif choice == '5':
                print("感谢使用，再见！")
                break
            else:
                print("无效输入，请重新选择。")



if __name__ == "__main__":
    manager = BudgetManager()
    manager.main_menu()
