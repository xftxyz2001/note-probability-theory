p_jia = 0.8
p_yi_given_jia = 0.2
p_yi_given_not_jia = 0.9

# 计算 P(乙出差)
p_yi = p_jia * p_yi_given_jia + (1 - p_jia) * p_yi_given_not_jia

print("乙出差的概率为：", p_yi)

# 计算 P(甲出差|乙出差)
p_jia_given_yi = p_yi_given_jia * p_jia / p_yi

print("甲出差的概率为：", p_jia_given_yi)

'''
乙出差的概率为： 0.33999999999999997
甲出差的概率为： 0.4705882352941178
'''
