
import itertools as its
import pywifi
import time
from pywifi import const
from datetime import datetime

def createPassworddict():
    words = "1234567890abcdefghijklmnopqrstuvwxyz" #可选择的字符
    r =its.product(words,repeat=8)  #组成8位字符串
    #amount = list(r).count() #密码组合总数
    amount = 30260340 # c(36,8)
    #print(amount, "个密码组合")
    dic = open("d:/dev/pwd.txt","a")      #存储为wifi密码字典
    process = 1
    process_detail = 0
    #wifi密码完成换行，并写入txt文档
    for i in r:
        #print("已完成"+str(i*100%r)+"%")
        dic.write("".join(i))
        dic.write("".join("\n"))
        if process_detail/amount > process:
            print("已完成 "+ str(process)+"%, " , i, " of ", r)  
            process += 1
        process_detail += 1
    dic.close()


# WiFi扫描模块
def wifi_scan():
    # 初始化wifi
    wifi = pywifi.PyWiFi()
    # 使用第一个无线网卡
    interface = wifi.interfaces()[0]
    # 开始扫描
    interface.scan()
    for i in range(4):
        time.sleep(1)
        print('\r扫描可用 WiFi 中，请稍后。。。（' + str(3 - i), end='）')
    print('\r扫描完成！\n' + '-' * 38)
    print('\r{:4}{:6}{}'.format('编号', '信号强度', 'wifi名'))
    # 扫描结果，scan_results()返回一个集，存放的是每个wifi对象
    bss = interface.scan_results()
    # 存放wifi名的集合
    wifi_name_set = set()
    for w in bss:
        # 解决乱码问题
        wifi_name_and_signal = (100 + w.signal, w.ssid.encode('raw_unicode_escape').decode('utf-8'))
        wifi_name_set.add(wifi_name_and_signal)
    # 存入列表并按信号排序
    wifi_name_list = list(wifi_name_set)
    wifi_name_list = sorted(wifi_name_list, key=lambda a: a[0], reverse=True)
    num = 0
    # 格式化输出
    while num < len(wifi_name_list):
        print('\r{:<6d}{:<8d}{}'.format(num, wifi_name_list[num][0], wifi_name_list[num][1]))
        num += 1
    print('-' * 38)
    # 返回wifi列表
    return wifi_name_list

# WiFi连接模块
def wifi_connect(wifi_name_list):
    # 初始化wifi
    wifi = pywifi.PyWiFi()
    # 使用第一个无线网卡
    interface = wifi.interfaces()[0]
    # 断开所有wifi连接
    interface.disconnect()
    # wifi名称
    wifi_name = wifi_name_list[int(input('请输入WiFi编号：'))][1]
    # wifi密码
    wifi_pwd = input('请输入WiFi密码：')
    # 创建WiFi连接文件
    profile = pywifi.Profile()
    # 要连接WiFi的名称
    profile.ssid = wifi_name
    # 网卡的开放状态
    profile.auth = const.AUTH_ALG_OPEN
    # wifi加密算法
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    # wifi加密单元
    profile.cipher = const.CIPHER_TYPE_CCMP
    # wifi密码
    profile.key = wifi_pwd
    # 删除所有连接过的wifi文件
    interface.remove_all_network_profiles()
    # 设定新的连接文件
    new_profile = interface.add_network_profile(profile)
    # 连接wifi
    interface.connect(new_profile)
    # 等待连接
    time.sleep(3)
    # 判断是否连接成功
    if interface.status() == const.IFACE_CONNECTED:
        print('连接成功！')
    else:
        print('连接失败！')

if __name__ == '__main__':
    print('正在生成密码字典，请稍后。。。' , datetime.now())
    createPassworddict()
    print('密码字典生成完成！', datetime.now())
    wifi_name_list = wifi_scan()
    #wifi_connect(wifi_name_list)