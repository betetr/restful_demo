# coding:utf-8
import os

if __name__ == '__main__':
    # 获取CPU剩余百分比
    get_cpuinfo = 'top -n 1|grep Cpu|cut -d "," -f 4'
    rest_cpu = os.popen(get_cpuinfo).read().split('%')[0]
    print('获取CPU剩余百分比', rest_cpu)

    # 获取内存信息
    get_mem_total = 'top -n 1 |grep Mem | cut -d "," -f 1 | cut -d ":" -f 2'
    get_mem_used = 'top -n 1 |grep Mem | cut -d "," -f 2'
    total = os.popen(get_mem_total).read().split('')[0]
    used = os.popen(get_mem_used).read().split('')[0]
    rate_mem = used//total
    print('获取内存信息', rate_mem)
