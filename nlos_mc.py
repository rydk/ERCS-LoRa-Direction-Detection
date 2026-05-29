import numpy as np

# 参数设置
L = 0.3                 # 天线面板宽度
epsilon = 0.15          # L2和L3之间的最大间距
d = 5                   # 到墙的距离
n_trials = 1000000

def run_simulation(apply_angle_constraint=False, apply_physical_constraint=True):
    """运行模拟，可以选择是否施加角度约束"""
    success_count = 0
    valid_count = 0
    
    for _ in range(n_trials):
        # 生成随机位置
        points = np.random.uniform(3, 10, 4)
        L_1, L_2, L_temp, L_4 = np.sort(points)[::-1]
        
        # 物理约束：天线阵列总宽度
        if apply_physical_constraint and (L_1 - L_4) >= 0.6:
            continue
        
        # L2和L3接近的约束
        if apply_physical_constraint:
            max_delta = min(L_2 - L_4, epsilon)
            if max_delta <= 0:
                continue
            delta = np.random.uniform(0, max_delta)
            L_3 = L_2 - delta
        else:
            # 如果不施加物理约束，L3是L2和L4之间的随机值
            L_3 = np.random.uniform(L_4, L_2)
        
        # 计算反射角
        beta_1 = np.arctan(d / L_1)
        beta_2 = np.arctan(d / L_2)
        beta_3 = np.arctan(d / L_3)
        beta_4 = np.arctan(d / L_4)
        
        # 角度约束：β₂-β₁ < β₄-β₃
        if apply_angle_constraint and (beta_2 - beta_1) >= (beta_4 - beta_3):
            continue
        
        # 计算表达式
        expr = (L_2 - L_1) + (L_3 - L_4)
        
        valid_count += 1
        if expr > 0:
            success_count += 1
    
    probability = success_count / valid_count if valid_count > 0 else 0
    return probability, valid_count

print("=== 不同场景下的概率分析 ===")

# 场景1：只施加物理约束（无角度约束）
prob1, count1 = run_simulation(apply_angle_constraint=False, apply_physical_constraint=True)
print(f"场景1 - 只考虑物理约束（无角度约束）:")
print(f"  有效试验: {count1}")
print(f"  P(d_N1 > d_N2) = {prob1:.4f} ({prob1*100:.1f}%)")
print(f"  解释：理论上所有信号都能反射时，有{prob1*100:.1f}%的概率出现观测现象")

# 场景2：施加角度约束
prob2, count2 = run_simulation(apply_angle_constraint=True, apply_physical_constraint=True)
print(f"\n场景2 - 施加角度约束（NLOS实际条件）:")
print(f"  有效试验: {count2}")
print(f"  P(d_N1 > d_N2) = {prob2:.4f} ({prob2*100:.1f}%)")
print(f"  解释：实际NLOS反射角度约束下，概率提高到{prob2*100:.1f}%")

# 场景3：无任何约束（完全随机）
prob3, count3 = run_simulation(apply_angle_constraint=False, apply_physical_constraint=False)
print(f"\n场景3 - 完全随机（无任何约束）:")
print(f"  有效试验: {count3}")
print(f"  P(d_N1 > d_N2) = {prob3:.4f} ({prob3*100:.1f}%)")
print(f"  解释：完全随机情况下，概率为{prob3*100:.1f}%")

print(f"\n=== 综合结论 ===")
print(f"1. 理论下限（完全随机）: {prob3*100:.1f}%")
print(f"2. 中间状态（物理约束）: {prob1*100:.1f}%")
print(f"3. 实际上限（角度约束）: {prob2*100:.1f}%")
print(f"\n实际NLOS检测中，由于反射信号必须满足角度约束才能被接收，")
print(f"观测到d_N1 > d_N2的概率应在{prob1*100:.1f}%和{prob2*100:.1f}%之间，")
print(f"且由于NLOS环境的物理特性，概率更靠近{prob2*100:.1f}%。")