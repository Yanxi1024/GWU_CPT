X =  [0, 0.52, 0.55,  0.68,  0.91,  0.9,  0.97, 1.23,  1.04,  1.2,  1.3,  1.35,  1.4,  1.47, 1.6,  1.7,  1.85,  1.95,  1.99,  2.2,  2.3, 2.45,  2.48,  2.56,  2.43,  2.67,  2.85,  3, 3.39,  3.65,  3.86,  3.99]

def optimal_MaxLloyd_quantizer(X):
    X = sorted(X)

    d_lis = []
    for i in range(5):
        d_lis.append(i * 4 / 4)

    r_lis = [0] * 4

    # r_lis[0] = (d_lis[1] - d_lis[0]) / 2
    # r_lis[1] = (d_lis[2] - d_lis[1]) / 2
    # r_lis[2] = (d_lis[3] - d_lis[2]) / 2
    # r_lis[3] = (d_lis[4] - d_lis[3]) / 2

    def split(d_lis, X):
        split_lis = [[] for i in range(4)]
        for e in X:
            if e < d_lis[1]:
                split_lis[0].append(e)
            elif e < d_lis[2]:
                split_lis[1].append(e)
            elif e < d_lis[3]:
                split_lis[2].append(e)
            elif e < d_lis[4]:
                split_lis[3].append(e)

        return split_lis
    
    split_lis = split(d_lis, X)
    pre_split_lis = []

    index = 0
    print(f"=========iteration{index}==================================================================")
    print(f"d_i (i from 1 to 3) : {d_lis[1: 4]}")
    print(f"r_i (i from 0 to 3) : {r_lis}")
    print()

    while pre_split_lis != split_lis:
        index += 1

        for i in range(4):
            r_lis[i] = sum(split_lis[i]) / len(split_lis[i])
        
        d_lis[1] = (r_lis[1] + r_lis[0]) / 2
        d_lis[2] = (r_lis[2] + r_lis[1]) / 2
        d_lis[3] = (r_lis[3] + r_lis[2]) / 2

        pre_split_lis = split_lis
        split_lis = split(d_lis, X)

        print(f"=========iteration{index}==================================================================")
        print(f"d_i (i from 1 to 3) : {d_lis[1: 4]}")
        print(f"r_i (i from 0 to 3) : {r_lis}")
        print()
    
    index += 1

    print(f"=========iteration{index}==================================================================")
    print(f"d_i (i from 1 to 3) : {d_lis[1: 4]}")
    print(f"r_i (i from 0 to 3) : {r_lis}")
    print("Stop!")

    print(split_lis)

    import pandas as pd

    pd.set_option('display.max_columns', None)

    # 定义原始列表
    original_list = split_lis

    # 展平列表以获得第一行
    first_row = [element for sublist in original_list for element in sublist]

    # 根据条件生成第二行和第三行
    second_row = []
    third_row = []

    for i, sublist in enumerate(original_list):
        second_row.extend([int(i)] * len(sublist))
        third_row.extend([r_lis[i]] * len(sublist))

    # 创建表格以表示结果
    table = pd.DataFrame([first_row, second_row, third_row], index=["X", "Quantize X", "Dequantize X"])

    # 打印表格
    print(table)
    # print(table.to_string(header=False))

    mse = 0
    count = 0
    for i, e in enumerate(split_lis):
        for num in e:
            count += 1
            mse += (num - r_lis[i]) ** 2
    mse = mse / count
    print()
    print(f"MSE: {mse}")
    print()


if __name__ == '__main__':
    optimal_MaxLloyd_quantizer(X)

