# Generated by Django 2.1.7 on 2019-04-11 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resourceforproduct',
            options={'ordering': ['-id']},
        ),
        migrations.RenameField(
            model_name='resourceformodule',
            old_name='product_id',
            new_name='product',
        ),
        migrations.AlterField(
            model_name='resourceformodule',
            name='module_name',
            field=models.CharField(db_column='模块名称', max_length=50),
        ),
    ]
