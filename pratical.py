'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2023-05-17 21:30:20
LastEditors: Loeyxxx
LastEditTime: 2023-05-28 13:33:55
FilePath: \code\pratical.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import random
import matplotlib.pyplot as plt

def simulate_gambling(rounds):
    wins = 0
    for _ in range(rounds):
        outcome = random.random()  # 生成0到1之间的随机数
        if outcome < 0.5:
            wins += 1  # 赢得赌注的两倍
    return wins 

# rounds = 100000
# actual_wins = simulate_gambling(rounds)
# odd = 2.0
# practical_winrate = actual_wins / rounds
# bidding_fraction = (practical_winrate*(1+odd)-1)/odd

# 模拟40次赌博并记次的获胜次数
num_trials = 100000
rounds = 500
odd = 2.0
results = []
for _ in range(num_trials):
    wins = simulate_gambling(rounds)
    practical_winrate = wins / rounds
    bidding_fraction = (practical_winrate*(1+odd)-1)/odd
    results.append(bidding_fraction)

import matplotlib.pyplot as plt

def gen_segments(num):
    t = 1.0/num
    segments= []
    i=0
    while(i<1 and i+t<=1.0):
        segments.append((i,i+t))
        i=i+t
    return segments

# segments = [(0, 0.05), (0.05, 0.1), (0.1, 0.15), (0.15, 0.2),(0.2,0.25),(0.25,0.3),\
#             (0.3,0.35),(0.35,0.4),(0.4,0.45),(0.45,0.5),(0.5,0.55),(0.55,0.6),(0.6,0.65),(0.65,0.7),\
#                 (0.7,0.75),(0.75,0.8),(0.8,0.85),(0.85,0.9),(0.9,0.95),(0.95,1)]
segments=gen_segments(100)

# 初始化分段计数器
segment_counts = [0] * (len(segments)+1)

# 统计每个分段中结果的数量
for result in results:
    for i, segment in enumerate(segments):
        if segment[0] <= result <= segment[1]:
            segment_counts[i] += 1
            break

# 提取分段边界和计数器的数据
segment_edges = [segment[0] for segment in segments] + [segments[-1][1]]
counts = segment_counts

# 绘制矩形统计图
plt.bar(segment_edges, counts, width=0.05)
plt.axvline(x=0.25,color='green',linestyle='-')
plt.xlabel('Best betting fraction')
plt.ylabel('Counts')
plt.title('Distribution of Probabilities')
#plt.xlim(0.1,0.4)
plt.show()


