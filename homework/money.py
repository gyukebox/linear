import numpy as np


class Money:
    """
    # 연습문제 1 - 환율계산하기
    """
    pass


if __name__ == '__main__':
    # 1원은 얼마다
    us_dollar = 0.0008745
    euro = 0.0007458
    yen = 0.09863
    pound = 0.0006531
    australia_dollar = 0.001112

    money = np.array([10000, 50000, 100000, 1000000])
    print(money)
    print(money * us_dollar)
    print(money * euro)
    print(money * pound)
    print(money * australia_dollar)