# Generated by Django 2.0.5 on 2019-04-10 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceForModule',
            fields=[
                ('id', models.AutoField(db_column='模块id', primary_key=True, serialize=False, verbose_name='id')),
                ('module_name', models.CharField(db_column='产品名称', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, db_column='更新时间')),
                ('description', models.TextField(db_column='描述', max_length=200, null=True)),
                ('abandon_flag', models.IntegerField(db_column='是否删除', default=1)),
            ],
        ),
        migrations.CreateModel(
            name='ResourceForProduct',
            fields=[
                ('id', models.AutoField(db_column='产品id', primary_key=True, serialize=False, verbose_name='id')),
                ('product_name', models.CharField(db_column='产品名称', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, db_column='更新时间')),
                ('description', models.TextField(db_column='描述', max_length=200, null=True)),
                ('abandon_flag', models.IntegerField(db_column='是否删除', default=1)),
            ],
        ),
        migrations.AddField(
            model_name='resourceformodule',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='study.ResourceForProduct'),
        ),
    ]
