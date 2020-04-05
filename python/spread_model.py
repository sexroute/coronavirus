import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


# seir 模型
# 一般把传染病流行范围内的人群分成如下几类：
# 1、S 类，易感者 (Susceptible)，指未得病者，但缺乏免疫能力，与感染者接触后容易受到感染；
# 2、E 类，暴露者 (Exposed)，指接触过感染者，但暂无能力传染给其他人的人，对潜伏期长的传染病适用；
# 3、I 类，感病者 (Infectious)，指染上传染病的人，可以传播给 S 类成员，将其变为 E 类或 I 类成员；
# 4、R 类，康复者 (Recovered)，指被隔离或因病愈而具有免疫力的人。如免疫期有限，R 类成员可以重新变为 S 类。

def getChineseFont():
    return FontProperties(fname='/System/Library/Fonts/PingFang.ttc', size=15)


plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']


def calcReal(T):
    for i in range(0, len(T) - 1):
        S.append(S[i] - r * b * S[i] * I[i] / N)
        data = E[i] + r * b * S[i] * I[i] / N - a * E[i]
        if (data < 0):
            data = 0
        E.append(data)

        data_recovered = 0
        if i > recover_day:
            data_recovered = I[i - data_recovered]
            for j in range(i - recover_day, i):
                data_x =  I[j] - data_recovered
                if(data_x<0):
                    data_x = 0
                    I[j] = data_x
        data_infected = I[i] + a * E[i] - data_recovered
        if (data_infected < 0):
            data_infected = 0
        I.append(data_infected)

        R.append(R[i] + data_recovered)


def calc(T):
    for i in range(0, len(T) - 1):
        S.append(S[i] - r * b * S[i] * I[i] / N)

        E.append(E[i] + r * b * S[i] * I[i] / N - a * E[i])

        I.append(I[i] + a * E[i] - y * I[i])

        R.append(R[i] + y * I[i])


def plot(T, S, E, I, R):
    plt.figure()

    plt.title("SEIR-病毒传播时间曲线", fontproperties=getChineseFont())

    plt.plot(T, S, color='r', label='易感者')

    plt.plot(T, E, color='k', label='潜伏者')

    plt.plot(T, I, color='b', label='传染者')

    plt.plot(T, R, color='g', label='康复者')

    plt.grid(False)

    plt.legend()

    plt.xlabel("时间(天)", fontproperties=getChineseFont())

    plt.ylabel("人数", fontproperties=getChineseFont())

    plt.show()


if __name__ == '__main__':
    # 首先还是设置一下参数,之后方便修改
    N = 10000  # 人口总数

    E = []  # 潜伏携带者

    E.append(0)

    I = []  # 传染者

    I.append(1)

    S = []  # 易感者

    S.append(N - I[0])

    R = []  # 康复者

    R.append(0)

    r = 20  # 传染者接触人数

    b = 0.29  # 传染者传染概率

    a = 0.01  # 潜伏者患病概率

    recover_day = 14

    y = 1 / recover_day  # 康复概率

    T = [i for i in range(0, 160)]  # 时间

    calcReal(T)

    plot(T, E, S, I, R)
    plt.show()
