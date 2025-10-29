from django.db import models


class Series(models.Model):
    """设备系列模型"""
    name = models.CharField(max_length=100, verbose_name='系列名称', unique=True)
    description = models.TextField(verbose_name='系列描述')
    image = models.ImageField(upload_to='series_images/', verbose_name='系列图片', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    
    class Meta:
        verbose_name = '设备系列'
        verbose_name_plural = '设备系列'
        ordering = ['created_at']
    
    def __str__(self):
        return self.name
