"""

@Author  : Lord_Bao
@Date    : 2021/3/3

问题描述： 计算有多少个月之后，存款到达首付
"""
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

portion_down_payment = 0.25
current_savings = 0

#  an annual return
#  in other words,at the end of each month, you receive an additional
#  current_savings*r/12 funds to put into your savings
r = 0.04

down_payment = total_cost * portion_down_payment
num_of_months = 0
monthly_salary = annual_salary / 12

while current_savings < down_payment:
    # 当月的存款 = 上个月的存款+上个月的存款产生的额外利润 + 当前月工资用于首付的部分金额
    current_savings = (current_savings + current_savings*r/12) + monthly_salary * portion_saved
    num_of_months += 1

print("Number of months: " + str(num_of_months))
