#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
初始数据导入脚本
用于向数据库中添加设备系列的初始数据
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import django

# 设置Django设置模块环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'product_site.settings')

# 初始化Django环境
django.setup()

from products.models import Series

def add_initial_series():
    """添加初始设备系列数据"""
    
    # 定义初始设备系列数据
    series_data = [
        {
            'name': '验配箱系列',
            'description': '全面的视光功能检查设备'
        },
        {
            'name': '视光检查系列',
            'description': '专业的视力验配工具集合'
        },
        {
            'name': '视觉训练系列',
            'description': '专业视觉康复训练设备'
        },
        {
            'name': '视光设备系列',
            'description': '先进的综合视光诊疗设备'
        },
        {
            'name': '低视力助视器',
            'description': '为视力障碍人士提供辅助设备'
        },
        {
            'name': '视力表系列',
            'description': '标准视力检测设备'
        }
    ]
    
    added_count = 0
    for data in series_data:
        # 检查是否已存在同名的系列
        series, created = Series.objects.get_or_create(
            name=data['name'],
            defaults={'description': data['description']}
        )
        if created:
            print(f"添加设备系列: {data['name']}")
            added_count += 1
        else:
            print(f"设备系列已存在: {data['name']}")
    
    print(f"\n初始数据导入完成，新增 {added_count} 个设备系列。")
    print(f"当前数据库中共有 {Series.objects.count()} 个设备系列。")

if __name__ == '__main__':
    print("开始导入初始设备系列数据...\n")
    add_initial_series()
    print("\n您可以通过以下方式管理设备系列数据：")
    print("1. Django管理后台: http://127.0.0.1:8000/admin/")
    print("2. 运行此脚本可再次添加或更新数据")