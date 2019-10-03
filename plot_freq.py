# coding = utf-8

'''
绘制信号数据频谱图.
'''

import numpy as np
import os
import scipy.fftpack
import matplotlib.pyplot as plt

def read_data(filename, dtype, dim=1, count=-1, offset=0):
    ''' 读取数据.
    @param dim 数据维度，1表示实数，2表示复数.
    @param offset 跳过的数据量，以字节为单位.
    '''
    if not os.path.exists(filename) or os.path.getsize(filename) <= 0:
        return None

    data = np.fromfile(filename, dtype=dtype, count=count, offset=offset)

    if dim == 2:
        s = np.ndarray((int(len(data) / 2), ), dtype=np.complex)
        s.real, s.imag = data[0::2], data[1::2]
        return s
    elif dim == 1:
        s = np.ndarray((len(data), ), dtype=np.float)
        s = data
        return s
    else:
        return None


def plot_freq(data, fs=1):
    ''' 绘制频谱.
    '''
    if np.iscomplexobj(data):
        data_f = scipy.fft(data)
    else:
        data_f = scipy.fftpack.rfft(data)

    data_f = np.abs(data_f)
    data_f = np.log10(data_f) * 10

    plt.plot(data_f)
    plt.show()


def plot_specgram(data, fs=1):
    ''' 绘制瀑布图.
    '''
    plt.specgram(data, Fs=fs)    
    plt.show()

if __name__ == '__main__':
    filename = "c:/data/gpssim.bin"
    data = read_data(filename, np.int16, count=1024*1024)

    if data is not None:
        # plot_freq(data)
        plot_specgram(data)
