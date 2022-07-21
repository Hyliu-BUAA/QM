import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square
from scipy.integrate import simps


class FourierSeries(object):
    '''
    Description
    -----------
        1. 用于拟合`平波`的傅里叶级数
    
    Aims
    ----
        1. 输出真正的`平波`
        2. 输出`傅里叶级数拟合的波形`

    Attributes
    ----------
        1. self.times_lst: list
            在采样区间（时间维度）上所有取值
        2. self.time_length: float
            采样时间区间的长度
        3. self.freq_tot: int
            在采样区间内的频率，而不是在单位周期内的频率
        4. 

    Note
    ----
        1. 我们的采样区间不一定只是一个周期：
            - `self.freq_tot`: 是采样区间内的频率，而不是单位周期内的频率
    '''
    def __init__(self,
                time_start:float,
                time_end:float,
                freq_tot:float,
                num_samples:int,
                num_terms:int):
        '''
        Parameters
        ----------
            1. time_start: float
                采样时间区间的起点
            2. time_end: float
                采样时间区间的终点
            3. freq_tot: float
                在采样区间内的频率，而不是在单位周期内的频率
            4. num_samples: int
                样本的数目（在时间维度上采样）
            5. num_terms: int
                傅里叶级数的项数
        '''
        self.times_lst = np.linspace(time_start,
                                    time_end,
                                    num_samples,
                                    endpoint=False)
        self.time_length = time_end - time_start
        self.freq_tot = freq_tot

        self.real_signals_lst = self.get_real_signals_lst()

        self.num_terms = num_terms
    

    def get_real_signals_lst(self):
        '''
        Description
        -----------
            1. 得到真正的平波的信号数值
        '''
        # 参数为：2*pi * 周期内的总频率 * 时间点
        real_signals_lst = square(2*np.pi * self.freq_tot * self.times_lst,
                                duty=0.5)
        return real_signals_lst
    

    def get_simu_signals_lst(self):
        '''
        Description
        -----------
            1. 得到傅里叶级数模拟的信号数值
        '''
        a_0 = self.get_a_0()
        simu_signals_lst = a_0 / 2
        
        for idx_term in range(1, 1+self.num_terms):
            a_k = self.get_a_n(idx_term)
            cos_kwt = self.get_cos_nwt(idx_term)
            b_k = self.get_b_n(idx_term)
            sin_kwt = self.get_sin_nwt(idx_term)
            simu_signals_lst += (a_k * cos_kwt + b_k * sin_kwt)
        
        return simu_signals_lst
        

    def get_a_0(self):
        a_0 = 2 / self.time_length * simps(
                                        self.real_signals_lst,
                                        self.times_lst)
        return a_0


    def get_a_n(self, n):
        a_n = 2 / self.time_length * simps(
                                        self.get_cos_nwt(n) * self.real_signals_lst,
                                        self.times_lst)
        return a_n


    def get_b_n(self, n):
        b_n = 2 / self.time_length * simps(
                                        self.get_sin_nwt(n) * self.real_signals_lst,
                                        self.times_lst)
        return b_n


    def get_cos_nwt(self, n:int):
        '''
        Description
        -----------
            1. 计算 `cos(nwt)`
        '''
        return np.cos( n * 2*np.pi*self.freq_tot/self.time_length * self.times_lst )


    def get_sin_nwt(self, n:int):
        '''
        Description
        -----------
            1. 计算 `sin(nwt)`
        '''
        return np.sin( n * 2*np.pi*self.freq_tot/self.time_length * self.times_lst )



def plot_difference(times_lst:list,
                real_signals_lst:list,
                simu_signals_lst:list,
                output_png_path:str):
    plt.figure(figsize=(12, 8)) 

    plt.plot(times_lst, real_signals_lst,
            color="steelblue",
            lw="3")
    plt.plot(times_lst, simu_signals_lst,
            color="deeppink",
            alpha=0.5,
            lw="3")


    # 1. Set the title for figure
    plt.title("num_terms={0}".format(num_terms),
            fontsize=28,
            fontweight="bold")


    # 2. Retouch the xlabel, ylabel
    plt.xlabel("Time (s)", 
                fontsize=28, 
                fontweight="bold"
    )
    plt.ylabel("Ampitude", 
                fontsize=28, 
                fontweight="bold"
    )

    # 3. Retouch the ticks of x-axis/y-axis
    plt.xticks(fontsize=20, 
            fontweight="bold"
            )
    plt.yticks(fontsize=20, 
            fontweight="bold"
            )
    
    # 4. 保存图片
    plt.savefig(output_png_path)



### Driver Code
if __name__ == "__main__":
    # Calculate Fourier Series
    time_start = 0
    time_end = 1
    freq_tot = 5
    num_samples = 500
    num_terms = 50
    output_png_path = "./fs_{0}.png".format(num_terms)

    fourier_series = FourierSeries(
                            time_start=time_start,
                            time_end=time_end,
                            freq_tot=freq_tot,
                            num_samples=num_samples,
                            num_terms=num_terms)
    
    ### Plot
    times_lst = fourier_series.times_lst
    real_signals_lst = fourier_series.get_real_signals_lst()
    simu_signals_lst = fourier_series.get_simu_signals_lst()

    plot_difference(times_lst=times_lst,
                    real_signals_lst=real_signals_lst,
                    simu_signals_lst=simu_signals_lst,
                    output_png_path=output_png_path)