import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from scipy.optimize import curve_fit


# seir 模型
# 一般把传染病流行范围内的人群分成如下几类：
# 1、S 类，Healther 易感者 (Susceptible)，指未得病者，但缺乏免疫能力，与感染者接触后容易受到感染；
# 2、E 类，暴露者 (Exposed)，指接触过感染者，但暂无能力传染给其他人的人，对潜伏期长的传染病适用；
# 3、I 类，感病者 (Infectious)，指染上传染病的人，可以传播给 S 类成员，将其变为 E 类或 I 类成员；
# 4、R 类，康复者 (Recovered)，指被隔离或因病愈而具有免疫力的人。如免疫期有限，R 类成员可以重新变为 S 类。

def getChineseFont():
    return FontProperties(fname='/System/Library/Fonts/PingFang.ttc', size=15)


plt.rcParams['axes.unicode_minus'] = False
from sys import platform

if platform == "linux" or platform == "linux2":
    plt.rcParams[u'font.sans-serif'] = ['simhei']
    # plt.use('qt4agg')
    # 指定默认字体
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['font.family'] = 'sans-serif'
    # 解决负号'-'显示为方块的问题
    plt.rcParams['axes.unicode_minus'] = False

elif platform == "darwin":
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
elif platform == "win32":
    plt.rcParams[u'font.sans-serif'] = ['simhei']


def calcReal(T):
    for i in range(0, len(T) - 1):
        r_x = r
        if i > quarantine_day:
            r_x = quarantine_r
        S.append(S[i] - r_x * b * S[i] * I[i] / N - B2 * E[i] * S[i] / N)
        data = E[i] + r_x * b * S[i] * I[i] / N - a * E[i]
        if (data < 0):
            data = 0
        E.append(data)
        NI.append(a * E[i + 1])
        data_recovered = 0
        data_dead = 0
        if i > recover_day:
            data_recovered = NI[i - recover_day] * (1 - d)
            data_dead = NI[i - recover_day] * d
        D.append(data_dead)
        total_dead = TD[i]+data_dead
        TD.append(total_dead)
        data_infected = I[i] + a * E[i] - data_recovered
        if (data_infected < 0):
            data_infected = 0
        I.append(data_infected)

        R.append(R[i] + data_recovered)


def calcChina(r, b, B2, a, y):
    for i in range(0, len(T) - 1):
        S.append(S[i] - r * b * S[i] * I[i] / N - B2 * E[i] * S[i] / N)

        E.append(E[i] + r * b * S[i] * I[i] / N - a * E[i])

        I.append(I[i] + a * E[i] - y * I[i])

        R.append(R[i] + y * I[i])


def calc(T):
    for i in range(0, len(T) - 1):
        S.append(S[i] - r * b * S[i] * I[i] / N)

        E.append(E[i] + r * b * S[i] * I[i] / N - a * E[i])

        I.append(I[i] + a * E[i] - y * I[i])

        R.append(R[i] + y * I[i])


def plot(T):
    plt.figure()

    plt.title("SEIR-Virus-Time-Trend")

    # plt.plot(T, S, color='r', label='Susceptible')

    # plt.plot(T, E, color='k', label='Exposed')

    # plt.plot(T, I, color='b', label='Infectious')
    #
    # plt.plot(T, R, color='g', label='Recovered')
    #
    # plt.plot(T, NI, color='c', label='New Infectious')
    plt.plot(T, D, color='m', label='New Dead')
    # plt.plot(T, TD, color='m', label='Total Dead')

    plt.grid(False)

    plt.legend()

    plt.xlabel("Time(Day)")

    plt.ylabel("People Count")

    plt.show()


if __name__ == '__main__':

    N = 10000 * 800  # Total People

    E = [0]  # Exposed

    I = [1]  # Infectious

    S = [N - I[0]]  # Susceptible

    R = [0]  # Recovered

    NI = [0]  # New Infectious

    D = [0]  # new dead

    TD = [0] # total dead

    r = 20  # People Infectious Reached

    b = 0.29  # People infected ratio

    a = 0.03  # Exposed infection ratio

    d = 0.0338  # death rate: dead/Infectious

    B2 = 0.0  # infection ratio in Exposed status

    recover_day = 14  # everage recover day

    quarantine_day = 33  # quarantine day

    quarantine_r = 0.01  # quarantine Infectious ratio

    y = 1 / recover_day  # recover ratio

    observe_day = 60

    T = [i for i in range(0, observe_day)]  # time

    calcReal(T)

    plot(T)
    total = 0
    for i in range(0, len(D)):
        total = total + D[i]
    print(total)
    plt.show()
