from django.db import models

# Create your models here.
# 一个类 = 一个数据模型 = 一个数据表
# django的数据表，是从models往数据库中推，自动生成的数据表。而不是我们在数据库中自己创建的表
# 创建数据模型的类，继承models.Model，
# 其他属性：
"""
db_index 如果为True，设置添加数据库索引，默认是False
UNique  如果为True，该字段会被设置成唯一属性，默认是False
db_column  设置数据库中的字段名称
"""
# 根据models文件，生成相对应的迁移数据库脚本
# python manage.py makemigrations
# 使用数据库迁移脚本，把模型迁移到数据库中——创建表
# python manage.py migrate


class ResourceForProduct(models.Model):
    """
    产品信息表
    """
    # 添加一个自增的字段AutoField，默认类型是int,primary_key=True是否是主键
    id = models.AutoField('id', primary_key=True, db_column='产品id')
    # 添加一个字符串类型的字段，最大长度是50
    product_name = models.CharField(max_length=50, db_column='产品名称')
    # 添加一个datetime类型的时间字段，auto_now_add=True代表了只在数据添加的时候添加，数据更新之后，此字段不可修改
    created_at = models.DateTimeField(auto_now_add=True, db_column='创建时间')
    # auto_now=True代表每次更新数据，都会更新这个时间字段，那就是单条数据更新
    updated_at = models.DateTimeField(auto_now=True, db_column='更新时间')
    # 添加一个文本类型的字段，长度为200，null=True字段内容可以为空，默认值False
    description = models.TextField(max_length=200, null=True, db_column='描述')
    # 添加一个逻辑删除字段，int类型，default=1默认值为1
    abandon_flag = models.IntegerField(default=1, db_column='是否删除')

    # 缺省排序方式
    class Meta:
        ordering = ['-id']


class ResourceForModule(models.Model):
    """
    模块信息表
    """
    id  = models.AutoField('id', primary_key=True, db_column='模块id')
    # ForeignKey定义一个外键字段，关联表名，一对多的外键，
    # ResourceForProduct表中的id为一，
    # ResourceForModule表中的对应数据为多
    product = models.ForeignKey(ResourceForProduct, on_delete=models.CASCADE)
    module_name = models.CharField(max_length=50, db_column='模块名称')
    created_at = models.DateTimeField(auto_now_add=True, db_column='创建时间')
    updated_at = models.DateTimeField(auto_now=True, db_column='更新时间')
    description = models.TextField(max_length=200, null=True, db_column='描述')
    abandon_flag = models.IntegerField(default=1, db_column='是否删除')


