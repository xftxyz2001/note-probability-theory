import numpy as np
from scipy.stats import binom, poisson

# 模拟实验参数
n_trials = 1000  # 实验次数
p = 0.5  # 硬币正面朝上的概率

# 抛硬币实验
outcomes = np.random.binomial(n=1, p=p, size=n_trials)

# 统计正面朝上的次数
n_heads = np.sum(outcomes)
print("正面朝上的次数：", n_heads)

# 使用二项分布计算概率
prob_binom = binom.pmf(k=n_heads, n=n_trials, p=p)
print("二项分布概率：", prob_binom)

# 使用泊松分布计算概率
lam = n_trials * p  # 平均事件发生次数
prob_poisson = poisson.pmf(k=n_heads, mu=lam)
print("泊松分布概率：", prob_poisson)

# 误差分析


def rel_error(x, y): return abs(x-y)/y  # 相对误差函数


params = [(0.1, 1000), (0.3, 100), (0.5, 50), (0.7, 20), (0.9, 10)]  # 模型参数

# 打印相对误差
for p, n_trials in params:
    outcomes = np.random.binomial(n=1, p=p, size=n_trials)
    n_heads = np.sum(outcomes)
    lam = n_trials * p
    prob_binom = binom.pmf(k=n_heads, n=n_trials, p=p)
    prob_poisson = poisson.pmf(k=n_heads, mu=lam)
    print(f"p={p}, n_trials={n_trials}")
    print("二项分布相对误差：", rel_error(prob_binom, outcomes.mean()))
    print("泊松分布相对误差：", rel_error(prob_poisson, outcomes.mean()))
    print("--------------------")

