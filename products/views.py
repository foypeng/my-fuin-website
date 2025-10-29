from django.shortcuts import render
from .models import Series

# 首页视图
def home(request):
    # 从数据库获取所有设备系列
    series_list = Series.objects.all()
    context = {
        'series_list': series_list
    }
    return render(request, 'home.html', context)

# 商品列表视图 - 支持按系列展示
def product_list(request, series_id=None):
    context = {
        'series_id': series_id
    }
    
    # 如果提供了series_id，从数据库获取对应的系列信息
    if series_id:
        try:
            series = Series.objects.get(id=series_id)
            context['title'] = f"{series.name}产品"
            context['series'] = series
        except Series.DoesNotExist:
            context['title'] = '产品列表'
    else:
        context['title'] = '产品列表'
    
    return render(request, 'products/list.html', context)

# 商品详情视图
def product_detail(request, product_id):
    # 这里将来会从数据库获取特定商品数据
    context = {
        'title': '产品详情',
        'product_id': product_id
    }
    return render(request, 'products/detail.html', context)

# 技术支持视图
def support(request):
    context = {
        'title': '技术支持'
    }
    return render(request, 'support.html', context)

# 关于我们视图
def about_us(request):
    context = {
        'title': '关于我们'
    }
    return render(request, 'about.html', context)
