import tkinter as tk
from tkinter.filedialog import *
import pandas as pd
from ASG8005_PythonSDK import *

# 创建画布需要的库
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from itertools import chain
# 创建工具栏需要的库
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
import numpy as np
# 快捷键需要的模块
from matplotlib.backend_bases import key_press_handler
import matplotlib.pyplot as plt

# 导入绘图需要的模块
from matplotlib.figure import Figure

global dicts
global channels
global waveformSignal
global axc
global fig

@CFUNCTYPE(None, c_int, c_char_p)  # 设置字符串回调函数，要返回固件信息和提示
def status_callback(type, c_char_buff):
    print(type)
    print(c_char_buff)
    return

@CFUNCTYPE(None, c_int, c_int, POINTER(c_uint32))  # 设置count回调函数，dll有数据时调用python处理
def count_callback(type, len, c_int_buff):
    datList = []
    for i in range(len):
        datList.append(c_int_buff[i])
    typestr:str
    if type == 0:
        if m_CountCount != len:
            print("数据错误")
        typestr = 'count计数：'
    elif type == 3:
        typestr = '连续计数 ：'
    print(typestr,"datList :",datList)
    return

dicts = {'CH1': '0.xlsx', 'CH2': '0.xlsx', 'CH3': '0.xlsx', 'CH4': '0.xlsx', 'CH5': '0.xlsx', 'CH6': '0.xlsx',
         'CH7': '0.xlsx', 'CH8': '0.xlsx'}
channels = ['CH1', 'CH2', 'CH3', 'CH4', 'CH5', 'CH6', 'CH7', 'CH8']

root = tk.Tk()
root.geometry("1400x1000")

asg_state = tk.StringVar()
fileCH1 = tk.StringVar()
fileCH1_Time1 = tk.StringVar()
fileCH1_Time2 = tk.StringVar()
fileCH1_Time3 = tk.StringVar()
fileCH1_Time4 = tk.StringVar()
fileCH1_Time5 = tk.StringVar()
fileCH1_Time6 = tk.StringVar()
fileCH1_Time7 = tk.StringVar()
fileCH1_Time8 = tk.StringVar()
fileCH1_Time9 = tk.StringVar()

fileCH1_Logic1 = tk.StringVar()
fileCH1_Logic2 = tk.StringVar()
fileCH1_Logic3 = tk.StringVar()
fileCH1_Logic4 = tk.StringVar()
fileCH1_Logic5 = tk.StringVar()
fileCH1_Logic6 = tk.StringVar()
fileCH1_Logic7 = tk.StringVar()
fileCH1_Logic8 = tk.StringVar()
fileCH1_Logic9 = tk.StringVar()

fileCH2 = tk.StringVar()
fileCH2_Time1 = tk.StringVar()
fileCH2_Time2 = tk.StringVar()
fileCH2_Time3 = tk.StringVar()
fileCH2_Time4 = tk.StringVar()
fileCH2_Time5 = tk.StringVar()
fileCH2_Time6 = tk.StringVar()
fileCH2_Time7 = tk.StringVar()
fileCH2_Time8 = tk.StringVar()
fileCH2_Time9 = tk.StringVar()

fileCH2_Logic1 = tk.StringVar()
fileCH2_Logic2 = tk.StringVar()
fileCH2_Logic3 = tk.StringVar()
fileCH2_Logic4 = tk.StringVar()
fileCH2_Logic5 = tk.StringVar()
fileCH2_Logic6 = tk.StringVar()
fileCH2_Logic7 = tk.StringVar()
fileCH2_Logic8 = tk.StringVar()
fileCH2_Logic9 = tk.StringVar()

fileCH3 = tk.StringVar()

fileCH3_Time1 = tk.StringVar()
fileCH3_Time2 = tk.StringVar()
fileCH3_Time3 = tk.StringVar()
fileCH3_Time4 = tk.StringVar()
fileCH3_Time5 = tk.StringVar()
fileCH3_Time6 = tk.StringVar()
fileCH3_Time7 = tk.StringVar()
fileCH3_Time8 = tk.StringVar()
fileCH3_Time9 = tk.StringVar()

fileCH3_Logic1 = tk.StringVar()
fileCH3_Logic2 = tk.StringVar()
fileCH3_Logic3 = tk.StringVar()
fileCH3_Logic4 = tk.StringVar()
fileCH3_Logic5 = tk.StringVar()
fileCH3_Logic6 = tk.StringVar()
fileCH3_Logic7 = tk.StringVar()
fileCH3_Logic8 = tk.StringVar()
fileCH3_Logic9 = tk.StringVar()

fileCH4 = tk.StringVar()
fileCH4_Time1 = tk.StringVar()
fileCH4_Time2 = tk.StringVar()
fileCH4_Time3 = tk.StringVar()
fileCH4_Time4 = tk.StringVar()
fileCH4_Time5 = tk.StringVar()
fileCH4_Time6 = tk.StringVar()
fileCH4_Time7 = tk.StringVar()
fileCH4_Time8 = tk.StringVar()
fileCH4_Time9 = tk.StringVar()

fileCH4_Logic1 = tk.StringVar()
fileCH4_Logic2 = tk.StringVar()
fileCH4_Logic3 = tk.StringVar()
fileCH4_Logic4 = tk.StringVar()
fileCH4_Logic5 = tk.StringVar()
fileCH4_Logic6 = tk.StringVar()
fileCH4_Logic7 = tk.StringVar()
fileCH4_Logic8 = tk.StringVar()
fileCH4_Logic9 = tk.StringVar()

fileCH5 = tk.StringVar()
fileCH5_Time1 = tk.StringVar()
fileCH5_Time2 = tk.StringVar()
fileCH5_Time3 = tk.StringVar()
fileCH5_Time4 = tk.StringVar()
fileCH5_Time5 = tk.StringVar()
fileCH5_Time6 = tk.StringVar()
fileCH5_Time7 = tk.StringVar()
fileCH5_Time8 = tk.StringVar()
fileCH5_Time9 = tk.StringVar()

fileCH5_Logic1 = tk.StringVar()
fileCH5_Logic2 = tk.StringVar()
fileCH5_Logic3 = tk.StringVar()
fileCH5_Logic4 = tk.StringVar()
fileCH5_Logic5 = tk.StringVar()
fileCH5_Logic6 = tk.StringVar()
fileCH5_Logic7 = tk.StringVar()
fileCH5_Logic8 = tk.StringVar()
fileCH5_Logic9 = tk.StringVar()

fileCH6 = tk.StringVar()
fileCH6_Time1 = tk.StringVar()
fileCH6_Time2 = tk.StringVar()
fileCH6_Time3 = tk.StringVar()
fileCH6_Time4 = tk.StringVar()
fileCH6_Time5 = tk.StringVar()
fileCH6_Time6 = tk.StringVar()
fileCH6_Time7 = tk.StringVar()
fileCH6_Time8 = tk.StringVar()
fileCH6_Time9 = tk.StringVar()

fileCH6_Logic1 = tk.StringVar()
fileCH6_Logic2 = tk.StringVar()
fileCH6_Logic3 = tk.StringVar()
fileCH6_Logic4 = tk.StringVar()
fileCH6_Logic5 = tk.StringVar()
fileCH6_Logic6 = tk.StringVar()
fileCH6_Logic7 = tk.StringVar()
fileCH6_Logic8 = tk.StringVar()
fileCH6_Logic9 = tk.StringVar()

fileCH7 = tk.StringVar()
fileCH7_Time1 = tk.StringVar()
fileCH7_Time2 = tk.StringVar()
fileCH7_Time3 = tk.StringVar()
fileCH7_Time4 = tk.StringVar()
fileCH7_Time5 = tk.StringVar()
fileCH7_Time6 = tk.StringVar()
fileCH7_Time7 = tk.StringVar()
fileCH7_Time8 = tk.StringVar()
fileCH7_Time9 = tk.StringVar()

fileCH7_Logic1 = tk.StringVar()
fileCH7_Logic2 = tk.StringVar()
fileCH7_Logic3 = tk.StringVar()
fileCH7_Logic4 = tk.StringVar()
fileCH7_Logic5 = tk.StringVar()
fileCH7_Logic6 = tk.StringVar()
fileCH7_Logic7 = tk.StringVar()
fileCH7_Logic8 = tk.StringVar()
fileCH7_Logic9 = tk.StringVar()

fileCH8 = tk.StringVar()
fileCH8_Time1 = tk.StringVar()
fileCH8_Time2 = tk.StringVar()
fileCH8_Time3 = tk.StringVar()
fileCH8_Time4 = tk.StringVar()
fileCH8_Time5 = tk.StringVar()
fileCH8_Time6 = tk.StringVar()
fileCH8_Time7 = tk.StringVar()
fileCH8_Time8 = tk.StringVar()
fileCH8_Time9 = tk.StringVar()

fileCH8_Logic1 = tk.StringVar()
fileCH8_Logic2 = tk.StringVar()
fileCH8_Logic3 = tk.StringVar()
fileCH8_Logic4 = tk.StringVar()
fileCH8_Logic5 = tk.StringVar()
fileCH8_Logic6 = tk.StringVar()
fileCH8_Logic7 = tk.StringVar()
fileCH8_Logic8 = tk.StringVar()
fileCH8_Logic9 = tk.StringVar()


def selectCH1():
    filepath = askopenfilename()
    fileCH1.set(filepath)
    dicts['CH1'] = filepath
    CH1_High1, CH1_High2, CH1_High3, CH1_High4, CH1_High5, CH1_High6, CH1_High7, CH1_High8, CH1_High9 = High_low(
        filepath)
    CH1_Low1, CH1_Low2, CH1_Low3, CH1_Low4, CH1_Low5, CH1_Low6, CH1_Low7, CH1_Low8, CH1_Low9 = ["     1", "     0", "     1", "     0", "     1", "     0", "     1", "     0", "     1"]
    fileCH1_Time1.set(CH1_High1)
    fileCH1_Logic1.set(CH1_Low1)
    fileCH1_Time2.set(CH1_High2)
    fileCH1_Logic2.set(CH1_Low2)
    fileCH1_Time3.set(CH1_High3)
    fileCH1_Logic3.set(CH1_Low3)
    fileCH1_Time4.set(CH1_High4)
    fileCH1_Logic4.set(CH1_Low4)
    fileCH1_Time5.set(CH1_High5)
    fileCH1_Logic5.set(CH1_Low5)
    fileCH1_Time6.set(CH1_High6)
    fileCH1_Logic6.set(CH1_Low6)
    fileCH1_Time7.set(CH1_High7)
    fileCH1_Logic7.set(CH1_Low7)
    fileCH1_Time8.set(CH1_High8)
    fileCH1_Logic8.set(CH1_Low8)
    fileCH1_Time9.set(CH1_High9)
    fileCH1_Logic9.set(CH1_Low9)


def selectCH2():
    filepath = askopenfilename()
    fileCH2.set(filepath)
    dicts['CH2'] = filepath
    CH1_High1, CH1_High2, CH1_High3, CH1_High4, CH1_High5, CH1_High6, CH1_High7, CH1_High8, CH1_High9 = High_low(
        filepath)
    CH1_Low1, CH1_Low2, CH1_Low3, CH1_Low4, CH1_Low5, CH1_Low6, CH1_Low7, CH1_Low8, CH1_Low9 = ["     1", "     0", "     1", "     0", "     1", "     0", "     1", "     0", "     1"]
    fileCH2_Time1.set(CH1_High1)
    fileCH2_Logic1.set(CH1_Low1)
    fileCH2_Time2.set(CH1_High2)
    fileCH2_Logic2.set(CH1_Low2)
    fileCH2_Time3.set(CH1_High3)
    fileCH2_Logic3.set(CH1_Low3)
    fileCH2_Time4.set(CH1_High4)
    fileCH2_Logic4.set(CH1_Low4)
    fileCH2_Time5.set(CH1_High5)
    fileCH2_Logic5.set(CH1_Low5)
    fileCH2_Time6.set(CH1_High6)
    fileCH2_Logic6.set(CH1_Low6)
    fileCH2_Time7.set(CH1_High7)
    fileCH2_Logic7.set(CH1_Low7)
    fileCH2_Time8.set(CH1_High8)
    fileCH2_Logic8.set(CH1_Low8)
    fileCH2_Time9.set(CH1_High9)
    fileCH2_Logic9.set(CH1_Low9)

def selectCH3():
    filepath = askopenfilename()
    fileCH3.set(filepath)
    dicts['CH3'] = filepath
    CH1_High1, CH1_High2, CH1_High3, CH1_High4, CH1_High5, CH1_High6, CH1_High7, CH1_High8, CH1_High9 = High_low(
        filepath)
    CH1_Low1, CH1_Low2, CH1_Low3, CH1_Low4, CH1_Low5, CH1_Low6, CH1_Low7, CH1_Low8, CH1_Low9 = ["     1", "     0", "     1", "     0", "     1", "     0", "     1", "     0", "     1"]
    fileCH3_Time1.set(CH1_High1)
    fileCH3_Logic1.set(CH1_Low1)
    fileCH3_Time2.set(CH1_High2)
    fileCH3_Logic2.set(CH1_Low2)
    fileCH3_Time3.set(CH1_High3)
    fileCH3_Logic3.set(CH1_Low3)
    fileCH3_Time4.set(CH1_High4)
    fileCH3_Logic4.set(CH1_Low4)
    fileCH3_Time5.set(CH1_High5)
    fileCH3_Logic5.set(CH1_Low5)
    fileCH3_Time6.set(CH1_High6)
    fileCH3_Logic6.set(CH1_Low6)
    fileCH3_Time7.set(CH1_High7)
    fileCH3_Logic7.set(CH1_Low7)
    fileCH3_Time8.set(CH1_High8)
    fileCH3_Logic8.set(CH1_Low8)
    fileCH3_Time9.set(CH1_High9)
    fileCH3_Logic9.set(CH1_Low9)



def selectCH4():
    filepath = askopenfilename()
    fileCH4.set(filepath)
    dicts['CH4'] = filepath
    CH1_High1, CH1_High2, CH1_High3, CH1_High4, CH1_High5, CH1_High6, CH1_High7, CH1_High8, CH1_High9 = High_low(
        filepath)
    CH1_Low1, CH1_Low2, CH1_Low3, CH1_Low4, CH1_Low5, CH1_Low6, CH1_Low7, CH1_Low8, CH1_Low9 = ["     1", "     0", "     1", "     0", "     1", "     0", "     1", "     0", "     1"]
    fileCH4_Time1.set(CH1_High1)
    fileCH4_Logic1.set(CH1_Low1)
    fileCH4_Time2.set(CH1_High2)
    fileCH4_Logic2.set(CH1_Low2)
    fileCH4_Time3.set(CH1_High3)
    fileCH4_Logic3.set(CH1_Low3)
    fileCH4_Time4.set(CH1_High4)
    fileCH4_Logic4.set(CH1_Low4)
    fileCH4_Time5.set(CH1_High5)
    fileCH4_Logic5.set(CH1_Low5)
    fileCH4_Time6.set(CH1_High6)
    fileCH4_Logic6.set(CH1_Low6)
    fileCH4_Time7.set(CH1_High7)
    fileCH4_Logic7.set(CH1_Low7)
    fileCH4_Time8.set(CH1_High8)
    fileCH4_Logic8.set(CH1_Low8)
    fileCH4_Time9.set(CH1_High9)
    fileCH4_Logic9.set(CH1_Low9)



def selectCH5():
    filepath = askopenfilename()
    fileCH5.set(filepath)
    dicts['CH5'] = filepath
    CH1_High1, CH1_High2, CH1_High3, CH1_High4, CH1_High5, CH1_High6, CH1_High7, CH1_High8, CH1_High9 = High_low(
        filepath)
    CH1_Low1, CH1_Low2, CH1_Low3, CH1_Low4, CH1_Low5, CH1_Low6, CH1_Low7, CH1_Low8, CH1_Low9 = ["     1", "     0", "     1", "     0", "     1", "     0", "     1", "     0", "     1"]
    fileCH5_Time1.set(CH1_High1)
    fileCH5_Logic1.set(CH1_Low1)
    fileCH5_Time2.set(CH1_High2)
    fileCH5_Logic2.set(CH1_Low2)
    fileCH5_Time3.set(CH1_High3)
    fileCH5_Logic3.set(CH1_Low3)
    fileCH5_Time4.set(CH1_High4)
    fileCH5_Logic4.set(CH1_Low4)
    fileCH5_Time5.set(CH1_High5)
    fileCH5_Logic5.set(CH1_Low5)
    fileCH5_Time6.set(CH1_High6)
    fileCH5_Logic6.set(CH1_Low6)
    fileCH5_Time7.set(CH1_High7)
    fileCH5_Logic7.set(CH1_Low7)
    fileCH5_Time8.set(CH1_High8)
    fileCH5_Logic8.set(CH1_Low8)
    fileCH5_Time9.set(CH1_High9)
    fileCH5_Logic9.set(CH1_Low9)


def selectCH6():
    filepath = askopenfilename()
    fileCH6.set(filepath)
    dicts['CH6'] = filepath
    CH1_High1, CH1_High2, CH1_High3, CH1_High4, CH1_High5, CH1_High6, CH1_High7, CH1_High8, CH1_High9 = High_low(
        filepath)
    CH1_Low1, CH1_Low2, CH1_Low3, CH1_Low4, CH1_Low5, CH1_Low6, CH1_Low7, CH1_Low8, CH1_Low9 = ["     1", "     0", "     1", "     0", "     1", "     0", "     1", "     0", "     1"]
    fileCH6_Time1.set(CH1_High1)
    fileCH6_Logic1.set(CH1_Low1)
    fileCH6_Time2.set(CH1_High2)
    fileCH6_Logic2.set(CH1_Low2)
    fileCH6_Time3.set(CH1_High3)
    fileCH6_Logic3.set(CH1_Low3)
    fileCH6_Time4.set(CH1_High4)
    fileCH6_Logic4.set(CH1_Low4)
    fileCH6_Time5.set(CH1_High5)
    fileCH6_Logic5.set(CH1_Low5)
    fileCH6_Time6.set(CH1_High6)
    fileCH6_Logic6.set(CH1_Low6)
    fileCH6_Time7.set(CH1_High7)
    fileCH6_Logic7.set(CH1_Low7)
    fileCH6_Time8.set(CH1_High8)
    fileCH6_Logic8.set(CH1_Low8)
    fileCH6_Time9.set(CH1_High9)
    fileCH6_Logic9.set(CH1_Low9)


def selectCH7():
    filepath = askopenfilename()
    fileCH7.set(filepath)
    dicts['CH7'] = filepath
    CH1_High1, CH1_High2, CH1_High3, CH1_High4, CH1_High5, CH1_High6, CH1_High7, CH1_High8, CH1_High9 = High_low(
        filepath)
    CH1_Low1, CH1_Low2, CH1_Low3, CH1_Low4, CH1_Low5, CH1_Low6, CH1_Low7, CH1_Low8, CH1_Low9 = ["     1", "     0", "     1", "     0", "     1", "     0", "     1", "     0", "     1"]
    fileCH7_Time1.set(CH1_High1)
    fileCH7_Logic1.set(CH1_Low1)
    fileCH7_Time2.set(CH1_High2)
    fileCH7_Logic2.set(CH1_Low2)
    fileCH7_Time3.set(CH1_High3)
    fileCH7_Logic3.set(CH1_Low3)
    fileCH7_Time4.set(CH1_High4)
    fileCH7_Logic4.set(CH1_Low4)
    fileCH7_Time5.set(CH1_High5)
    fileCH7_Logic5.set(CH1_Low5)
    fileCH7_Time6.set(CH1_High6)
    fileCH7_Logic6.set(CH1_Low6)
    fileCH7_Time7.set(CH1_High7)
    fileCH7_Logic7.set(CH1_Low7)
    fileCH7_Time8.set(CH1_High8)
    fileCH7_Logic8.set(CH1_Low8)
    fileCH7_Time9.set(CH1_High9)
    fileCH7_Logic9.set(CH1_Low9)


def selectCH8():
    filepath = askopenfilename()
    fileCH8.set(filepath)
    dicts['CH8'] = filepath
    CH1_High1, CH1_High2, CH1_High3, CH1_High4, CH1_High5, CH1_High6, CH1_High7, CH1_High8, CH1_High9 = High_low(
        filepath)
    CH1_Low1, CH1_Low2, CH1_Low3, CH1_Low4, CH1_Low5, CH1_Low6, CH1_Low7, CH1_Low8, CH1_Low9 = ["     1", "     0", "     1", "     0", "     1", "     0", "     1", "     0", "     1"]
    fileCH8_Time1.set(CH1_High1)
    fileCH8_Logic1.set(CH1_Low1)
    fileCH8_Time2.set(CH1_High2)
    fileCH8_Logic2.set(CH1_Low2)
    fileCH8_Time3.set(CH1_High3)
    fileCH8_Logic3.set(CH1_Low3)
    fileCH8_Time4.set(CH1_High4)
    fileCH8_Logic4.set(CH1_Low4)
    fileCH8_Time5.set(CH1_High5)
    fileCH8_Logic5.set(CH1_Low5)
    fileCH8_Time6.set(CH1_High6)
    fileCH8_Logic6.set(CH1_Low6)
    fileCH8_Time7.set(CH1_High7)
    fileCH8_Logic7.set(CH1_Low7)
    fileCH8_Time8.set(CH1_High8)
    fileCH8_Logic8.set(CH1_Low8)
    fileCH8_Time9.set(CH1_High9)
    fileCH8_Logic9.set(CH1_Low9)


def dataProcessing():
    waveformSignal = documentMerge(dicts, channels)
    print(waveformSignal)
    Download(waveformSignal)

def connects():
    #print("asg.connect() ", asg.connect())
    a = asg.connect()
    b = "connect success"
    if (a == 1):
        asg_state.set("connect success")
    if(a == 0):
        asg_state.set("connect fail")

def Download(asg_data1):
    # 连接


    length1 = [len(seq) for seq in asg_data1]

    #input("press Enter to download_ASG_pulse_data")
    #print("asg.download_ASG_pulse_data: ", asg.download_ASG_pulse_data(asg_data1, length1))

    download_ASGs = asg.download_ASG_pulse_data(asg_data1, length1)

    # COUNT
    count_data = [20, 20, 20, 20, 20, 20, 20, 1500]
    length_count = len(count_data)
    m_CountCount = length_count / 2

    # 下载count数据
    #print("asg.ASG_counter_download : ", asg.ASG_counter_download(count_data, length_count))
    ASG_counter_downloads = asg.ASG_counter_download(count_data, length_count)

    # 配置循环次数
    counter_repeat = 4  # 1x2 = 4
    #print("asg.ASG_set_counter_repeat ：", asg.ASG_set_counter_repeat(counter_repeat))
    ASG_set_counter_repeats = asg.ASG_set_counter_repeat(counter_repeat)


    # 配置连续采集时间间隔
    count_timeStep = 50000000  # 50000000 x 20 = 1000000000ns = 1s
    ASG_countTimeSteps = asg.ASG_countTimeStep(count_timeStep)

    # 开启连续计数功能
    bIsContinue = 1
    #print("asg.ASG_isCountContinue：", asg.ASG_isCountContinue(bIsContinue))
    ASG_isCountContinues = asg.ASG_isCountContinue(bIsContinue)
    # 配置asg和count功能 有两个参数第一个是开启count功能，第二个是开启asg功能，第二个默认asg全开
    #print("asg.ASG_countConfig：", asg.ASG_countConfig(bIsContinue))
    ASG_countConfigs = asg.ASG_countConfig(bIsContinue)

    if(ASG_countConfigs & ASG_isCountContinues & ASG_countTimeSteps & ASG_set_counter_repeats & ASG_counter_downloads & download_ASGs):
        asg_state.set("download success")
    elif (download_ASGs == 0):
        asg_state.set("download_asg fail")
    elif (ASG_counter_downloads == 0):
        asg_state.set("download_counter fail")
    elif (ASG_set_counter_repeats == 0):
        asg_state.set("download_counter_repeats fail")
    elif (ASG_countTimeSteps == 0):
        asg_state.set("countTimeSteps fail")
    elif (ASG_isCountContinues == 0):
        asg_state.set("CountContinues fail")
    elif (ASG_countConfigs == 0):
        asg_state.set("countConfigs fail")

def running():
    #print("asg.start(): ", asg.start())
    a = asg.start()
    if (a == 1):
        asg_state.set("start success")
    elif(a == 0):
        asg_state.set("start fail")

def stopping():
    #print("asg.stop(): ", asg.stop())
    a = asg.stop()
    if (a == 1):
        asg_state.set("stop success")
    elif(a == 0):
        asg_state.set("stop fail")

def closed():
    print("asg.close_device(): ", asg.close_device())
    a =  asg.close_device()
    if (a == 1):
        asg_state.set("close_device success")
    elif(a == 0):
        asg_state.set("close_device fail")

def High_low(localAddress):  # 地址和高低电平，0为高，1为低
    ch1 = pd.read_excel(localAddress, header=None)
    #ch1_high = ch1[ch1.index % 2 == ele].astype(str)
    ch1 = ch1.astype(str)
    ch1_high = (ch1.values).tolist()
    ch1_high = [str(i) for i in ch1_high]
    ch1_high = ''.join(ch1_high)
    ch1_high = ch1_high.replace("['", "")
    ch1_high = ch1_high.replace("']", ", ")
    ch1_high = ch1_high.split(",")
    return ch1_high[0], ch1_high[1], ch1_high[2], ch1_high[3], ch1_high[4], ch1_high[5], ch1_high[6], ch1_high[7], \
           ch1_high[8]


def documentMerge(localDicts, localChannel):  # 输入值：储存的路径，channel的字符串组
    Maxnumber = 0
    for x in localChannel:
        globals()[x] = pd.read_excel(localDicts[x], header=None)  # 读入Dateframe
        globals()[x + 'number'] = globals()[x].shape[0]  # 找到每个的行数
        Maxnumber = max(Maxnumber, globals()[x + 'number'])  # 找到Dateframe最大值
    # for x in channel:
    # if Maxnumber - globals()[x + 'number'] > 0:
    # globals()[x] = pd.concat([globals()[x], pd.DataFrame(np.zeros(Maxnumber - globals()[x + 'number'],dtype=np.int8))]) #补零
    # print(globals()[x])
    Points = pd.concat(
        [globals()[localChannel[0]], globals()[localChannel[1]], globals()[localChannel[2]], globals()[localChannel[3]],
         globals()[localChannel[4]], globals()[localChannel[5]], globals()[localChannel[6]],
         globals()[localChannel[7]]], axis=1)
    Points = Points.fillna(10)
    Points = Points.astype(int)
    Points = pd.DataFrame(Points.values.T, index=Points.columns, columns=Points.index)
    Points = Points.values.tolist()
    #print(type(globals()[localChannel[0]]))
    return Points

def draws(Channels):
    axc.clear()
    x = pd.read_excel(dicts[Channels], header=None)
    x = np.array(x)
     #然后转化为list形式
    x = x.tolist()
    x = list(chain.from_iterable(x))
    ch1 = [0 for i in range(len(x))]
    for i in range(len(x)):
        if (i % 2) == 0:
            ch1[i] = 1
    for i in range(1, len(x) - 1):
        x[i] = x[i - 1] + x[i]
    axc.grid(axis="y", c='r')
    axc.plot(x, ch1, drawstyle='steps-pre')
    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    canvas.draw()
    # 显示画布控件
    canvas.get_tk_widget().place(x=244 + 450, y=120)

    # 创建工具条控件
    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()
    # 显示工具条控件
    canvas.get_tk_widget()


tk.Label(root, text='CHANNEL 1').grid(row=1, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=fileCH1).grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text='OPEN CHANNEL 1 PATH', command=selectCH1).grid(row=1, column=2, padx=5, pady=5)

tk.Label(root, text='             通道1电平持续时间：').grid(row=2, column=0, padx=2, pady=3)
tk.Entry(root, textvariable=fileCH1_Time1).place(x=194, y=40, width=50, height=25)
tk.Entry(root, textvariable=fileCH1_Time2).place(x=244, y=40, width=50, height=25)
tk.Entry(root, textvariable=fileCH1_Time3).place(x=244 + 50, y=40, width=50, height=25)
tk.Entry(root, textvariable=fileCH1_Time4).place(x=244 + 100, y=40, width=50, height=25)
tk.Entry(root, textvariable=fileCH1_Time5).place(x=244 + 150, y=40, width=50, height=25)
tk.Entry(root, textvariable=fileCH1_Time6).place(x=244 + 200, y=40, width=50, height=25)
tk.Entry(root, textvariable=fileCH1_Time7).place(x=244 + 250, y=40, width=50, height=25)
tk.Entry(root, textvariable=fileCH1_Time8).place(x=244 + 300, y=40, width=50, height=25)
tk.Entry(root, textvariable=fileCH1_Time9).place(x=244 + 350, y=40, width=50, height=25)



tk.Label(root, text='             通道1电平：').grid(row=3, column=0, padx=2, pady=3)
tk.Entry(root, textvariable=fileCH1_Logic1).place(x=194, y=70, width=50, height=25)
tk.Entry(root, textvariable=fileCH1_Logic2).place(x=244, y=70, width=50, height=25)
tk.Entry(root, textvariable=fileCH1_Logic3).place(x=244 + 50, y=70, width=50, height=25)
tk.Entry(root, textvariable=fileCH1_Logic4).place(x=244 + 100, y=70, width=50, height=25)
tk.Entry(root, textvariable=fileCH1_Logic5).place(x=244 + 150, y=70, width=50, height=25)
tk.Entry(root, textvariable=fileCH1_Logic6).place(x=244 + 200, y=70, width=50, height=25)
tk.Entry(root, textvariable=fileCH1_Logic7).place(x=244 + 250, y=70, width=50, height=25)
tk.Entry(root, textvariable=fileCH1_Logic8).place(x=244 + 300, y=70, width=50, height=25)
tk.Entry(root, textvariable=fileCH1_Logic9).place(x=244 + 350, y=70, width=50, height=25)


tk.Label(root, text='CHANNEL 2').grid(row=4, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=fileCH2).grid(row=4, column=1, padx=5, pady=5)
tk.Button(root, text='OPEN CHANNEL 2 PATH', command=selectCH2).grid(row=4, column=2, padx=5, pady=5)

tk.Label(root, text='             通道2电平持续时间：').grid(row=5, column=0, padx=2, pady=3)
tk.Entry(root, textvariable=fileCH2_Time1).place(x=194, y=140, width=50, height=25)
tk.Entry(root, textvariable=fileCH2_Time2).place(x=244, y=140, width=50, height=25)
tk.Entry(root, textvariable=fileCH2_Time3).place(x=244 + 50, y=140, width=50, height=25)
tk.Entry(root, textvariable=fileCH2_Time4).place(x=244 + 100, y=140, width=50, height=25)
tk.Entry(root, textvariable=fileCH2_Time5).place(x=244 + 150, y=140, width=50, height=25)
tk.Entry(root, textvariable=fileCH2_Time6).place(x=244 + 200, y=140, width=50, height=25)
tk.Entry(root, textvariable=fileCH2_Time7).place(x=244 + 250, y=140, width=50, height=25)
tk.Entry(root, textvariable=fileCH2_Time8).place(x=244 + 300, y=140, width=50, height=25)
tk.Entry(root, textvariable=fileCH2_Time9).place(x=244 + 350, y=140, width=50, height=25)



tk.Label(root, text='             通道2电平：').grid(row=6, column=0, padx=2, pady=3)

tk.Entry(root, textvariable=fileCH2_Logic1).place(x=194, y=170, width=50, height=25)
tk.Entry(root, textvariable=fileCH2_Logic2).place(x=244, y=170, width=50, height=25)
tk.Entry(root, textvariable=fileCH2_Logic3).place(x=244 + 50, y=170, width=50, height=25)
tk.Entry(root, textvariable=fileCH2_Logic4).place(x=244 + 100, y=170, width=50, height=25)
tk.Entry(root, textvariable=fileCH2_Logic5).place(x=244 + 150, y=170, width=50, height=25)
tk.Entry(root, textvariable=fileCH2_Logic6).place(x=244 + 200, y=170, width=50, height=25)
tk.Entry(root, textvariable=fileCH2_Logic7).place(x=244 + 250, y=170, width=50, height=25)
tk.Entry(root, textvariable=fileCH2_Logic8).place(x=244 + 300, y=170, width=50, height=25)
tk.Entry(root, textvariable=fileCH2_Logic9).place(x=244 + 350, y=170, width=50, height=25)

tk.Label(root, text='CHANNEL 3').grid(row=7, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=fileCH3).grid(row=7, column=1, padx=5, pady=5)
tk.Button(root, text='OPEN CHANNEL 3 PATH', command=selectCH3).grid(row=7, column=2, padx=5, pady=5)


tk.Label(root, text='             通道3电平持续时间：').grid(row=8, column=0, padx=2, pady=3)
tk.Entry(root, textvariable=fileCH3_Time1).place(x=194, y=240, width=50, height=25)
tk.Entry(root, textvariable=fileCH3_Time2).place(x=244, y=240, width=50, height=25)
tk.Entry(root, textvariable=fileCH3_Time3).place(x=244 + 50, y=240, width=50, height=25)
tk.Entry(root, textvariable=fileCH3_Time4).place(x=244 + 100, y=240, width=50, height=25)
tk.Entry(root, textvariable=fileCH3_Time5).place(x=244 + 150, y=240, width=50, height=25)
tk.Entry(root, textvariable=fileCH3_Time6).place(x=244 + 200, y=240, width=50, height=25)
tk.Entry(root, textvariable=fileCH3_Time7).place(x=244 + 250, y=240, width=50, height=25)
tk.Entry(root, textvariable=fileCH3_Time8).place(x=244 + 300, y=240, width=50, height=25)
tk.Entry(root, textvariable=fileCH3_Time9).place(x=244 + 350, y=240, width=50, height=25)



tk.Label(root, text='             通道3电平：').grid(row=9, column=0, padx=2, pady=3)
tk.Entry(root, textvariable=fileCH3_Logic1).place(x=194, y=270, width=50, height=25)
tk.Entry(root, textvariable=fileCH3_Logic2).place(x=244, y=270, width=50, height=25)
tk.Entry(root, textvariable=fileCH3_Logic3).place(x=244 + 50, y=270, width=50, height=25)
tk.Entry(root, textvariable=fileCH3_Logic4).place(x=244 + 100, y=270, width=50, height=25)
tk.Entry(root, textvariable=fileCH3_Logic5).place(x=244 + 150, y=270, width=50, height=25)
tk.Entry(root, textvariable=fileCH3_Logic6).place(x=244 + 200, y=270, width=50, height=25)
tk.Entry(root, textvariable=fileCH3_Logic7).place(x=244 + 250, y=270, width=50, height=25)
tk.Entry(root, textvariable=fileCH3_Logic8).place(x=244 + 300, y=270, width=50, height=25)
tk.Entry(root, textvariable=fileCH3_Logic9).place(x=244 + 350, y=270, width=50, height=25)

tk.Label(root, text='CHANNEL 4').grid(row=10, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=fileCH4).grid(row=10, column=1, padx=5, pady=5)
tk.Button(root, text='OPEN CHANNEL 4 PATH', command=selectCH4).grid(row=10, column=2, padx=5, pady=5)

tk.Label(root, text='             通道4电平持续时间：').grid(row=11, column=0, padx=2, pady=3)
tk.Entry(root, textvariable=fileCH4_Time1).place(x=194, y=340, width=50, height=25)
tk.Entry(root, textvariable=fileCH4_Time2).place(x=244, y=340, width=50, height=25)
tk.Entry(root, textvariable=fileCH4_Time3).place(x=244 + 50, y=340, width=50, height=25)
tk.Entry(root, textvariable=fileCH4_Time4).place(x=244 + 100, y=340, width=50, height=25)
tk.Entry(root, textvariable=fileCH4_Time5).place(x=244 + 150, y=340, width=50, height=25)
tk.Entry(root, textvariable=fileCH4_Time6).place(x=244 + 200, y=340, width=50, height=25)
tk.Entry(root, textvariable=fileCH4_Time7).place(x=244 + 250, y=340, width=50, height=25)
tk.Entry(root, textvariable=fileCH4_Time8).place(x=244 + 300, y=340, width=50, height=25)
tk.Entry(root, textvariable=fileCH4_Time9).place(x=244 + 350, y=340, width=50, height=25)

tk.Label(root, text='             通道4电平：').grid(row=12, column=0, padx=2, pady=3)
tk.Entry(root, textvariable=fileCH4_Logic1).place(x=194, y=370, width=50, height=25)
tk.Entry(root, textvariable=fileCH4_Logic2).place(x=244, y=370, width=50, height=25)
tk.Entry(root, textvariable=fileCH4_Logic3).place(x=244 + 50, y=370, width=50, height=25)
tk.Entry(root, textvariable=fileCH4_Logic4).place(x=244 + 100, y=370, width=50, height=25)
tk.Entry(root, textvariable=fileCH4_Logic5).place(x=244 + 150, y=370, width=50, height=25)
tk.Entry(root, textvariable=fileCH4_Logic6).place(x=244 + 200, y=370, width=50, height=25)
tk.Entry(root, textvariable=fileCH4_Logic7).place(x=244 + 250, y=370, width=50, height=25)
tk.Entry(root, textvariable=fileCH4_Logic8).place(x=244 + 300, y=370, width=50, height=25)
tk.Entry(root, textvariable=fileCH4_Logic9).place(x=244 + 350, y=370, width=50, height=25)

tk.Label(root, text='CHANNEL 5').grid(row=13, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=fileCH5).grid(row=13, column=1, padx=5, pady=5)
tk.Button(root, text='OPEN CHANNEL 5 PATH', command=selectCH5).grid(row=13, column=2, padx=5, pady=5)

tk.Label(root, text='             通道5电平持续时间：').grid(row=14, column=0, padx=2, pady=3)
tk.Entry(root, textvariable=fileCH5_Time1).place(x=194, y=440, width=50, height=25)
tk.Entry(root, textvariable=fileCH5_Time2).place(x=244, y=440, width=50, height=25)
tk.Entry(root, textvariable=fileCH5_Time3).place(x=244 + 50, y=440, width=50, height=25)
tk.Entry(root, textvariable=fileCH5_Time4).place(x=244 + 100, y=440, width=50, height=25)
tk.Entry(root, textvariable=fileCH5_Time5).place(x=244 + 150, y=440, width=50, height=25)
tk.Entry(root, textvariable=fileCH5_Time6).place(x=244 + 200, y=440, width=50, height=25)
tk.Entry(root, textvariable=fileCH5_Time7).place(x=244 + 250, y=440, width=50, height=25)
tk.Entry(root, textvariable=fileCH5_Time8).place(x=244 + 300, y=440, width=50, height=25)
tk.Entry(root, textvariable=fileCH5_Time9).place(x=244 + 350, y=440, width=50, height=25)



tk.Label(root, text='             通道5电平：').grid(row=15, column=0, padx=2, pady=3)
tk.Entry(root, textvariable=fileCH5_Logic1).place(x=194, y=470, width=50, height=25)
tk.Entry(root, textvariable=fileCH5_Logic2).place(x=244, y=470, width=50, height=25)
tk.Entry(root, textvariable=fileCH5_Logic3).place(x=244 + 50, y=470, width=50, height=25)
tk.Entry(root, textvariable=fileCH5_Logic4).place(x=244 + 100, y=470, width=50, height=25)
tk.Entry(root, textvariable=fileCH5_Logic5).place(x=244 + 150, y=470, width=50, height=25)
tk.Entry(root, textvariable=fileCH5_Logic6).place(x=244 + 200, y=470, width=50, height=25)
tk.Entry(root, textvariable=fileCH5_Logic7).place(x=244 + 250, y=470, width=50, height=25)
tk.Entry(root, textvariable=fileCH5_Logic8).place(x=244 + 300, y=470, width=50, height=25)
tk.Entry(root, textvariable=fileCH5_Logic9).place(x=244 + 350, y=470, width=50, height=25)

tk.Label(root, text='CHANNEL 6').grid(row=16, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=fileCH6).grid(row=16, column=1, padx=5, pady=5)
tk.Button(root, text='OPEN CHANNEL 6 PATH', command=selectCH6).grid(row=16, column=2, padx=5, pady=5)

tk.Label(root, text='             通道6电平持续时间：').grid(row=17, column=0, padx=2, pady=3)
tk.Entry(root, textvariable=fileCH6_Time1).place(x=194, y=540, width=50, height=25)
tk.Entry(root, textvariable=fileCH6_Time2).place(x=244, y=540, width=50, height=25)
tk.Entry(root, textvariable=fileCH6_Time3).place(x=244 + 50, y=540, width=50, height=25)
tk.Entry(root, textvariable=fileCH6_Time4).place(x=244 + 100, y=540, width=50, height=25)
tk.Entry(root, textvariable=fileCH6_Time5).place(x=244 + 150, y=540, width=50, height=25)
tk.Entry(root, textvariable=fileCH6_Time6).place(x=244 + 200, y=540, width=50, height=25)
tk.Entry(root, textvariable=fileCH6_Time7).place(x=244 + 250, y=540, width=50, height=25)
tk.Entry(root, textvariable=fileCH6_Time8).place(x=244 + 300, y=540, width=50, height=25)
tk.Entry(root, textvariable=fileCH6_Time9).place(x=244 + 350, y=540, width=50, height=25)



tk.Label(root, text='             通道6电平：').grid(row=18, column=0, padx=2, pady=3)
tk.Entry(root, textvariable=fileCH6_Logic1).place(x=194, y=570, width=50, height=25)
tk.Entry(root, textvariable=fileCH6_Logic2).place(x=244, y=570, width=50, height=25)
tk.Entry(root, textvariable=fileCH6_Logic3).place(x=244 + 50, y=570, width=50, height=25)
tk.Entry(root, textvariable=fileCH6_Logic4).place(x=244 + 100, y=570, width=50, height=25)
tk.Entry(root, textvariable=fileCH6_Logic5).place(x=244 + 150, y=570, width=50, height=25)
tk.Entry(root, textvariable=fileCH6_Logic6).place(x=244 + 200, y=570, width=50, height=25)
tk.Entry(root, textvariable=fileCH6_Logic7).place(x=244 + 250, y=570, width=50, height=25)
tk.Entry(root, textvariable=fileCH6_Logic8).place(x=244 + 300, y=570, width=50, height=25)
tk.Entry(root, textvariable=fileCH6_Logic9).place(x=244 + 350, y=570, width=50, height=25)

tk.Label(root, text='CHANNEL 7').grid(row=19, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=fileCH7).grid(row=19, column=1, padx=5, pady=5)
tk.Button(root, text='OPEN CHANNEL 7 PATH', command=selectCH7).grid(row=19, column=2, padx=5, pady=5)

tk.Label(root, text='             通道7电平持续时间：').grid(row=20, column=0, padx=2, pady=3)
tk.Entry(root, textvariable=fileCH7_Time1).place(x=194, y=640, width=50, height=25)
tk.Entry(root, textvariable=fileCH7_Time2).place(x=244, y=640, width=50, height=25)
tk.Entry(root, textvariable=fileCH7_Time3).place(x=244 + 50, y=640, width=50, height=25)
tk.Entry(root, textvariable=fileCH7_Time4).place(x=244 + 100, y=640, width=50, height=25)
tk.Entry(root, textvariable=fileCH7_Time5).place(x=244 + 150, y=640, width=50, height=25)
tk.Entry(root, textvariable=fileCH7_Time6).place(x=244 + 200, y=640, width=50, height=25)
tk.Entry(root, textvariable=fileCH7_Time7).place(x=244 + 250, y=640, width=50, height=25)
tk.Entry(root, textvariable=fileCH7_Time8).place(x=244 + 300, y=640, width=50, height=25)
tk.Entry(root, textvariable=fileCH7_Time9).place(x=244 + 350, y=640, width=50, height=25)



tk.Label(root, text='             通道7电平：').grid(row=21, column=0, padx=2, pady=3)
tk.Entry(root, textvariable=fileCH7_Logic1).place(x=194, y=670, width=50, height=25)
tk.Entry(root, textvariable=fileCH7_Logic2).place(x=244, y=670, width=50, height=25)
tk.Entry(root, textvariable=fileCH7_Logic3).place(x=244 + 50, y=670, width=50, height=25)
tk.Entry(root, textvariable=fileCH7_Logic4).place(x=244 + 100, y=670, width=50, height=25)
tk.Entry(root, textvariable=fileCH7_Logic5).place(x=244 + 150, y=670, width=50, height=25)
tk.Entry(root, textvariable=fileCH7_Logic6).place(x=244 + 200, y=670, width=50, height=25)
tk.Entry(root, textvariable=fileCH7_Logic7).place(x=244 + 250, y=670, width=50, height=25)
tk.Entry(root, textvariable=fileCH7_Logic8).place(x=244 + 300, y=670, width=50, height=25)
tk.Entry(root, textvariable=fileCH7_Logic9).place(x=244 + 350, y=670, width=50, height=25)

tk.Label(root, text='CHANNEL 8').grid(row=22, column=0, padx=5, pady=5)
tk.Entry(root, textvariable=fileCH8).grid(row=22, column=1, padx=5, pady=5)
tk.Button(root, text='OPEN CHANNEL 8 PATH', command=selectCH8).grid(row=22, column=2, padx=5, pady=5)

tk.Label(root, text='             通道8电平持续时间：').grid(row=23, column=0, padx=2, pady=3)
tk.Entry(root, textvariable=fileCH8_Time1).place(x=194, y=730, width=50, height=25)
tk.Entry(root, textvariable=fileCH8_Time2).place(x=244, y=730, width=50, height=25)
tk.Entry(root, textvariable=fileCH8_Time3).place(x=244 + 50, y=730, width=50, height=25)
tk.Entry(root, textvariable=fileCH8_Time4).place(x=244 + 100, y=730, width=50, height=25)
tk.Entry(root, textvariable=fileCH8_Time5).place(x=244 + 150, y=730, width=50, height=25)
tk.Entry(root, textvariable=fileCH8_Time6).place(x=244 + 200, y=730, width=50, height=25)
tk.Entry(root, textvariable=fileCH8_Time7).place(x=244 + 250, y=730, width=50, height=25)
tk.Entry(root, textvariable=fileCH8_Time8).place(x=244 + 300, y=730, width=50, height=25)
tk.Entry(root, textvariable=fileCH8_Time9).place(x=244 + 350, y=730, width=50, height=25)



tk.Label(root, text='             通道8电平：').grid(row=24, column=0, padx=2, pady=3)
tk.Entry(root, textvariable=fileCH8_Logic1).place(x=194, y=760, width=50, height=25)
tk.Entry(root, textvariable=fileCH8_Logic2).place(x=244, y=760, width=50, height=25)
tk.Entry(root, textvariable=fileCH8_Logic3).place(x=244 + 50, y=760, width=50, height=25)
tk.Entry(root, textvariable=fileCH8_Logic4).place(x=244 + 100, y=760, width=50, height=25)
tk.Entry(root, textvariable=fileCH8_Logic5).place(x=244 + 150, y=760, width=50, height=25)
tk.Entry(root, textvariable=fileCH8_Logic6).place(x=244 + 200, y=760, width=50, height=25)
tk.Entry(root, textvariable=fileCH8_Logic7).place(x=244 + 250, y=760, width=50, height=25)
tk.Entry(root, textvariable=fileCH8_Logic8).place(x=244 + 300, y=760, width=50, height=25)
tk.Entry(root, textvariable=fileCH8_Logic9).place(x=244 + 350, y=760, width=50, height=25)

tk.Button(root, text='连接', command=connects).place(x=194, y=790, width=50, height=25)
tk.Button(root, text='下载', command=dataProcessing).place(x=244 + 50, y=790, width=50, height=25)
tk.Button(root, text='运行', command=running).place(x=244 + 150, y=790, width=50, height=25)
tk.Button(root, text='停止', command=stopping).place(x=244 + 250, y=790, width=50, height=25)
tk.Entry(root, textvariable=asg_state).place(x=244 + 350, y=790, width=150, height=25)
asg = ASG8005()

#绘图
###############################################################

fig = Figure(figsize=(8, 6), dpi=100, constrained_layout=True, facecolor="pink", edgecolor='green', frameon=True)

axc = fig.add_subplot(111)

var=tk.StringVar()
var.set('Channel 1 waveform')
tk.Label(root,
    textvariable=var,    # 标签的文字
    font=('Arial', 20)    # 字体和字体大
    ).place(x=244 + 470 + 120, y=50, width=500, height=25)

tk.Button(root, text='CH1', command=lambda :draws('CH1')).place(x=244 + 470 + 80, y=90, width=70, height=25)
tk.Button(root, text='CH2', command=lambda :draws('CH2')).place(x=244 + 470 + 80 + 80, y=90, width=70, height=25)
tk.Button(root, text='CH3', command=lambda :draws('CH3')).place(x=244 + 470 + 160 + 80, y=90, width=70, height=25)
tk.Button(root, text='CH4', command=lambda :draws('CH4')).place(x=244 + 470 + 240 + 80, y=90, width=70, height=25)
tk.Button(root, text='CH5', command=lambda :draws('CH5')).place(x=244 + 470 + 320 + 80, y=90, width=70, height=25)
tk.Button(root, text='CH6', command=lambda :draws('CH6')).place(x=244 + 470 + 400 + 80, y=90, width=70, height=25)
tk.Button(root, text='CH7', command=lambda :draws('CH7')).place(x=244 + 470 + 480 + 80, y=90, width=70, height=25)
tk.Button(root, text='CH8', command=lambda :draws('CH8')).place(x=244 + 470 + 560 + 80, y=90, width=70, height=25)
###############################################################################

# 设置回调函数
asg.set_callback(status_callback)
asg.set_callback_count(count_callback)
root.mainloop()