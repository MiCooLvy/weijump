# -*- coding:utf-8 -*-
"""
关于Android设备的ADB命令操作
by Kenn
01/16/2018
"""
import os
import time
import sys


def init():
    serialNum = get_device_serialNum()
    print("Serial Number: " + serialNum)
    get_device_info(serialNum)
    # 截图
    screencap(serialNum)


def get_device_info(serialNum):
    """
    获取设备信息
    :param serialNum: 设备序列号
    """
    out1 = os.popen("adb -s " + serialNum + " version")
    out2 = os.popen("adb -s " + serialNum + " shell wm size")
    out3 = os.popen("adb -s " + serialNum + " shell wm density")
    out4 = os.popen("adb -s " + serialNum + " shell getprop ro.build.version.release")
    print(out1.readline().strip())
    print(out2.readline().strip())
    print(out3.readline().strip())
    print("Android Version：" + out4.readline().strip())


def screencap(serialNum, debug=False):
    """
    截屏上传到电脑
    :param serialNum: 设备序列号
    :param debug: 是否是调试模式
    """
    os.system("adb -s " + serialNum + " shell screencap -p /sdcard/sc.png")
    if debug:
        ts = str(int(time.time()))
        ts = serialNum + "_" + ts
        os.system("adb -s " + serialNum + " pull /sdcard/sc.png ./img/" + ts + ".png")
        os.system("copy img\\" + ts + ".png sc.png")
    else:
        os.system("adb -s " + serialNum + " pull /sdcard/sc.png sc.png")
    print("ScreenCap OK!")


def get_device_serialNum():
    """
    获取设备信息
    :return: 选中的设备序列号
    """
    out = os.popen("adb devices")
    dvs = []
    for dv in out.readlines():
        t = str.strip(dv).split('\t')
        if len(t) == 2 and t[1] == 'device':
            dvs.append(t[0])
    if len(dvs) > 1:
        print("已连接设备数超过一台，请选择其中一个连接：")
        idx = 0
        for dv in dvs:
            print(str(idx) + ":\t" + dv)
            idx += 1
        ch = int(input("请选择："))
        return dvs[ch]
    elif len(dvs) == 1:
        return dvs[0]
    else:
        print("设备尚未连接，请打开设备调试")
        sys.exit()
