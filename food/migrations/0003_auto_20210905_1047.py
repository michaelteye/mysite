# Generated by Django 3.1.7 on 2021-09-05 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_item_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='Item_image',
            field=models.CharField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSQxBwsiy_mCHZ6dHERdZlKhYGL3Gw5QlOUiw&usqp=CAU', max_length=500),
        ),
    ]