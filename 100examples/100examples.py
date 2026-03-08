# %% [markdown]
# # 知乎 Python 100 练习题
# %% [markdown]
# ## 数字组合
# %% [markdown]
# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# %%
total = 0

for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i!=j and j!=k and k!=i:
                print(i,j,k, " ")
                total+=1

total
# %% [markdown]
# ## 个税计算
# %% [markdown]
# 企业发放的奖金根据利润提成。利润(I):
# 1. 低于或等于10万元时，奖金可提10%；
# 2. 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 3. 20万到40万之间时，高于20万元的部分，可提成5%；
# 4. 40万到60万之间时高于40万元的部分，可提成3%；
# 5. 60万到100万之间时，高于60万元的部分，可提成1.5%;
# 6. 高于100万元时，超过100万元的部分按1%提成，
# 
# 从键盘输入当月利润I，求应发放奖金总数？
# %% [markdown]
# ### 正向计算
# %%
income = int(input("income: "))
bonus = 0
threshold = [0, 100000, 200000, 400000, 600000, 1000000]
rate = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01]

if income <= 100000:
    bonus += income * 0.1
else:
    ptr = 0
    for i in range(1, len(threshold)):
        if income > threshold[i]:
            bonus += (threshold[i] - threshold[i - 1]) * rate[i - 1]
            ptr += 1
    bonus += (income - threshold[ptr]) * rate[ptr]

bonus
# %% [markdown]
# ### 倒序计算
# %%
income = int(input("income: "))
bonus = 0
threshold = [1000000, 600000, 400000, 200000, 100000, 0]
rate = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]

for i in range(0, len(threshold)):
    if income > threshold[i]:
        available = income - threshold[i]
        bonus += available * rate[i]
        income -= available

bonus
# %% [markdown]
# ## 完全平方数
# %% [markdown]
# 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
# 
# p.s. 如果一个正整数 a 是某一个整数 b 的平方，那么这个正整数 a 叫做完全平方数。零也可称为完全平方数。
# %%
# 经由数学分析，找出 i * j = 168 的所有因子对(注意精度问题)，且 i > j
for i in range (1, 168):
    j = 168 / i
    if i > j:
        break
    if  j.is_integer() and i % 2 == 0 and j % 2 == 0:
        b = (i + j) / 2
        if b.is_integer() and (b**2 - 268 > 0):
            print(b**2 - 268)
# %%
import math

def is_perfect_square(num):
    return math.sqrt(num).is_integer()


for x in range (0, 100000):
    if is_perfect_square(x + 100) and is_perfect_square(x + 100 + 168):
        print(x)
# %%
import math

def is_perfect_square_2(num):
    return math.isqrt(num) ** 2 == num

for x in range (0, 100000):
    if is_perfect_square_2(x + 100) and is_perfect_square_2(x + 100 + 168):
        print(x)
# %%
# 经过数学证明，j 只需要在 2 到 sqrt(168) 之间的偶数中寻找
for j in range(2, 13, 2):
    if 168 % j == 0:
        i = 168 // j
        # 确保 i, j 同奇同偶（此处已知均为偶数）
        if (i + j) % 2 == 0:
            n = (i - j) // 2
            x = n**2 - 100
            print(f"找到解：x = {x}, 此时 n={n}, m={i-n}")
# %% [markdown]
# ## 这是一年中的第几天
# %% [markdown]
# 输入某年某月某日，判断这一天是这一年的第几天？
# 
# 要确定一年是否为闰年，请执行以下步骤：
# 
# 1. 公元年份非4的倍数，为365天平年。
# 2. 公元年份为4的倍数但非100的倍数，为366天闰年。
# 3. 公元年份为100的倍数但非400的倍数（1700年、1800年及1900年）为平年。
# 4. 公元年份为400的倍数（1600年及2000年）为闰年。
# %%
def is_leap_year(y):
    return y % 4 == 0 and y % 100 != 0 or y % 400 == 0

DoM = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]

year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

if is_leap_year(year):
    DoM[1] += 1

total = 0
for i in range(month):
    total += DoM[i]
total += day

total

# %% [markdown]

# ## This content is for converting test

# %%
print(list(range(10)))
