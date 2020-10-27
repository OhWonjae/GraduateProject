# Generated by Django 3.1 on 2020-09-03 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MaskCCTV', '0002_maskinfo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='maskinfo',
            options={'ordering': ['date']},
        ),
        migrations.AddField(
            model_name='maskinfo',
            name='adress',
            field=models.CharField(choices=[('a', '강원도 춘천시 효자동 남춘천역'), ('b', '서울시 강남구 강남역'), ('c', '경기도 남양주시 사릉역')], default='a', help_text='CCTV 주소', max_length=1),
        ),
    ]
