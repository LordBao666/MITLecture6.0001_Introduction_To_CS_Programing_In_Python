"""

@Author  : Lord_Bao
@Date    : 2021/3/3

问题描述： 1M元的房子，看能不能在36月里面给出首付，如果不能，打印不能的提示。如果能，打印
          每个月将工资的多少来存储的概率并打印二分法猜测的次数。

          注意：  根据题目：
                 所谓的最好  指的是在  portion_saved下，   36个月之后的存款肯定是要超过首付的。
                 但是又不至于超得太多，而是恰到好处，恰到好处是指超出的金额刚好在100美元以内。

                 但是这种情况是存在一定的问题的。假如我的年收入很大，即使portion_saved在最小0.0001的情况下。
                 最终的savings_after_36months - down_payment 仍然会超过 100美元。还有就是因为精度的问题，会导致
                 没有合适的portion_saved刚刚在100美元内。
                 所以在这种精度下，我们并一定不能满足 所谓的  '恰到好处'。

                 那么重新定义一下，恰到好处 ：
                    1.如果碰到savings_after_36months >= down_payment  和 (savings_after_36months - down_payment) <= 100
                      这是最好的情况，直接终止程序。
                    why_mid_plus_1(chap10.3).如果在1不能满足的情况下，
                    如果能在在某种portion_saved 下 ，刚刚超过down_payment。 举个例子
                      0.8777下，savings_after_36months 是大过 down_payment
                      0.8776下，savings_after_36months 是小于 down_payment
                    那么这个portion_saved将是满足情况的。
 思路分析：
         1.首先这个问题的月份是限死在36月的，第一件事是检测在极限清况下(portion_saved=1）。
           36个月以后的存款金额是否大于等于首付。
         why_mid_plus_1(chap10.3).根据要求，概率的精度是4位，所以二分法的猜测范围是0到10000（实际对应概率0.00%--100.00%）



"""


def savings(months, annual_salary, portion_saved,
            semi_annual_raise=0.07, r=0.04):
    """

    :param months: 月份
    :param annual_salary: 每年的工资
    :param portion_saved: 工资拿来存储的比率
    :param semi_annual_raise: 半年的涨工资的比率
    :param r: 每年的利息
    :return: 返回months之后的总存储

    """
    current_savings = 0
    monthly_salary = annual_salary / 12

    for month in range(1, months + 1):
        # 每月计算累积存款
        current_savings = (current_savings + current_savings * r / 12) + monthly_salary * portion_saved

        # 每半年的下一月就会涨薪
        if month % 6 == 0:
            monthly_salary += monthly_salary * semi_annual_raise
    return current_savings


def main():
    # semi_annual_raise = 0.07
    # r = 0.04
    total_cost = 1000000
    portion_down_payment = 0.25
    down_payment = total_cost * portion_down_payment

    annual_salary = float(input("Enter the starting  salary: "))
    if savings(months=36, annual_salary=annual_salary, portion_saved=1) >= down_payment:
        num_guesses = 0
        savings_after_36months = 0
        begin = 0
        end = 10000
        half = (begin + end) // 2  # 避免产生浮点数
        portion_saved = 0

        while begin < end - 1:
            num_guesses += 1

            portion_saved = half / 10000
            savings_after_36months = savings(36, annual_salary, portion_saved)
            # # down_payment是25 0000
            # print("guess " + str(num_guesses) + ":" + "half=" + str(half) + ",savings=" + str(
            #     savings_after_36months))
            if savings_after_36months >= down_payment and (savings_after_36months - down_payment) <= 100:
                break
            else:
                # 如果是上面最终的第2个情况,那么begin端一直小于down_payment,end端一直大于down_payment。
                # 极限是 当 begin 和 end 相差1的时候，end对应的portion_saved即为答案
                if savings_after_36months > down_payment:
                    # end = half - 1可能不太好，我们考虑上述的定义的第2个恰到好处的话
                    # 比如刚好在half这里是刚刚好超过down_payment，而half-1却小于down_payment
                    # 这就失去了我们想要的答案。也就是说我们一直能保证在end处一定是大于down_payment的
                    # end = half - 1
                    end = half
                else:
                    # begin = half + 1  也许可行。
                    # 但是为了简便思考,将begin端一直当做是小于down_payment的
                    begin = half
            half = (begin + end) // 2
            # print("begin:" + str(begin) + ",end:" + str(end))

        # 如果是上面第2种情况
        if begin >= end - 1:
            portion_saved = end / 10000
        # print("Savings: " + str(savings_after_36months))
        print("Best savings rate: " + str(portion_saved))
        print("Steps in bisection search: " + str(num_guesses))
    else:
        print("It is not possible to pay the down payment in three years")


if __name__ == '__main__':
    main()
