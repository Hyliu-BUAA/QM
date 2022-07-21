from cProfile import label
from unittest import signals
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square
from scipy.integrate import simps



# 1. Sample at 1000 Hz/second
def get_ts_lst(time_start:float,
               time_end:float,
               num_samples:int):
    '''
    Parameters
    ----------
        1. time_start: float
            采样开始时间点
        2. time_end: float
            采样结束时间点
        3. num_samples: int
            采样点的数目
    '''
    return np.linspace(time_start, time_end, num_samples,
                        endpoint=False)


# 2. Calculate signals_lst of 方波
def get_signals_lst(ts_lst:list,
                    freq:float,
                    ):
    '''
    Parameters
    ----------
        1. ts_lst: list
            时间采样点
        2. freq: float
            方波的频率
    '''
    # 参数为 2 * pi * 频率 * 时间点集合
    return square(2 * np.pi * freq * ts_lst,
                duty=0.5)


# 3. Calculate Fourier coefficients
def get_a_0(ts_lst:list,
            signals_lst:list,
            L:float):
    a_0 = 2 / L * simps(signals_lst, ts_lst)
    return a_0


def get_a_n(ts_lst:list,
            signals_lst:list,
            freq:float,
            L:float,
            n:int):
    cos_nwt = np.cos(n * 2*np.pi * freq / L * ts_lst)
    a_n = 2 / L * \
        simps(cos_nwt * signals_lst, ts_lst)
    return a_n


def get_b_n(ts_lst:list,
            signals_lst:list,
            freq:float,
            L:float,
            n:int):
    sin_nwt = np.sin(n * 2*np.pi * freq / L * ts_lst)
    a_n = 2 / L * \
        simps(sin_nwt * signals_lst, ts_lst)
    return a_n


# 4. 
def get_simulation_signals_lst(num_terms:int,
                            ts_lst:list,
                            signals_lst:list,
                            freq:float,
                            L:float):
    a_0 = get_a_0(ts_lst=ts_lst,
                signals_lst=signals_lst,
                L=L)
    ssignals_lst = a_0

    for k in range(1, 1+num_terms):
        a_k = get_a_n(ts_lst=ts_lst,
                    signals_lst=signals_lst,
                    freq=freq,
                    L=L,
                    n=k)
        cos_kwt = np.cos(k * 2*np.pi * freq / L * ts_lst)

        b_k = get_b_n(ts_lst=ts_lst,
                    signals_lst=signals_lst,
                    freq=freq,
                    L=L,
                    n=k)
        sin_kwt = np.sin(k * 2*np.pi * freq / L * ts_lst)

        ssignals_lst += a_k * cos_kwt + b_k * sin_kwt
    
    return ssignals_lst


# 5. Main code
if __name__ == "__main__":
    # 正弦/余弦函数的数目
    num_terms = 100
    # 时间区间：[0, 2]
    time_start = 0
    time_end = 2
    L = time_end - time_start
    # 平波的频率
    freq = 5
    # 时间点的样本数
    num_samples = 1000


    ts_lst = get_ts_lst(time_start=time_start,
                        time_end=time_end,
                        num_samples=num_samples)
    signals_lst = get_signals_lst(ts_lst=ts_lst,
                                freq=freq)

    ssignals_lst = get_simulation_signals_lst(num_terms=num_terms,
                                            ts_lst=ts_lst,
                                            signals_lst=signals_lst,
                                            freq=freq,
                                            L=L)    
    
    plt.plot(ts_lst, signals_lst, 
            color="steelblue",
            lw="8",
            label="signals")
    plt.plot(ts_lst, ssignals_lst,
            color="pink",
            label="ssignals")
    plt.legend()
    plt.show()