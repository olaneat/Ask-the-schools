# Generated by Django 2.1.1 on 2018-12-03 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('askschools', '0004_auto_20181120_0510'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sport', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='schools',
            name='GENDER',
            field=models.BooleanField(default='True', verbose_name='complete'),
        ),
        migrations.AddField(
            model_name='schools',
            name='SPORTS',
            field=models.ManyToManyField(to='askschools.Sports'),
        ),
        migrations.AddField(
            model_name='schools',
            name='extra_activities',
            field=models.ManyToManyField(to='askschools.Club'),
        ),
    ]
