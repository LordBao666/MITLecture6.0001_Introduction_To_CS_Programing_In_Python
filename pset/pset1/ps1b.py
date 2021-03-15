"""

@Author  : Lord_Bao
@Date    : 2021/3/3

问题描述： 计算有多少个月之后，存款到达首付。相比ps1a,ps1b的变化是MIT的毕业生的工资每6个月会增薪。
           这个不难.假设月份是6月的倍数的时候，用monthly_salary照常计算当月current_savings,然后再更新monthly_salary即可
         ，这样就可以保证下个月的monthly_salary是更新后的工资。
"""
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

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
    current_savings = (current_savings + current_savings * r / 12) + monthly_salary * portion_saved
    num_of_months += 1
    if num_of_months % 6 == 0:
        monthly_salary = monthly_salary * (1+semi_annual_raise)

print("Number of months: " + str(num_of_months))
