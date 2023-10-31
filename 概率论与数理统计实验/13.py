p_c = 0.005  # P(C)
p_not_c = 1 - p_c  # P(not C)
p_not_a_given_c = 0.05  # P(not A | C)
p_a_given_not_c = 0.05  # P(A | not C)

p_a = (1 - p_not_a_given_c) * p_c + p_a_given_not_c * p_not_c
print("某人检测结果为阳性是真正阳性的概率为：", p_a)

'''
某人检测结果为阳性是真正阳性的概率为： 0.0545
'''
