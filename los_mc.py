import numpy as np

def monte_carlo_probability(d, L1, num_samples=100000):
    count = 0

    for _ in range(num_samples):
        # 随机生成 theta_1 和 theta_2 满足 0 < theta_1 < theta_2 < pi/2 且 theta_2 - theta_1 < pi/18
        theta_1 = np.random.uniform(0, np.pi/3 - np.pi/18)
        theta_2 = np.random.uniform(theta_1, min(theta_1 + np.pi/18, np.pi/3))

        # 计算 d1 - d2
        d_diff = np.tan(theta_1) * (L1 + 0.8) - 2 * np.tan(theta_2) * (L1 + 0.4) + d

        if d_diff > 0:
            count += 1

    return count / num_samples

# 示例：输出多个 d 和 L1 值下的概率
d_list = [2]
#d_list = [3.9, 3.3, 2.7, 2.1]
#L1_list = [1.2, 1.8, 2.4, 3.0, 3.6, 4.2]
L1_list = [1]

for L1 in L1_list:
    for d_val in d_list:
        if L1 == 1 and d_val > 3:
            continue  # 表中未显示此组合
        prob = monte_carlo_probability(d_val, L1)
        print(f"d={d_val}, L1={L1}, P(L_RX1 > L_RX2) ≈ {prob:.5f}")
