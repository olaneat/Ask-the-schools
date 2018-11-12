# Generated by Django 2.1.1 on 2018-11-10 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=300)),
                ('title', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('message', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='parents_remark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(help_text='fill in your full name', max_length=300)),
                ('school_name', models.CharField(max_length=100)),
                ('comment', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='school_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CURRICULUM', models.CharField(choices=[('Bri', 'British'), ('Ame', 'American'), ('Bri & Ame', 'British American'), ('Ger', 'German'), ('Fre', 'French')], max_length=20)),
                ('WEBSITE', models.URLField(blank=True, max_length=100)),
                ('EXTRA_CURRICULUM', models.CharField(max_length=20)),
                ('AWARDS', models.CharField(blank=True, help_text='kindly list the schools Awards', max_length=150)),
                ('DIRECTION', models.CharField(help_text='give a brief description to your school ', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Schools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SCHOOL_NAME', models.CharField(max_length=300)),
                ('MOTTO', models.CharField(max_length=200)),
                ('BADGE', models.ImageField(blank=True, help_text='upload a jpg file ', upload_to='media/images')),
                ('LEVEL', models.CharField(blank=True, choices=[('Pri', 'Primary'), ('Sec', 'Secondary'), ('Pri and Sec', 'Primary and Secondary')], max_length=20)),
                ('ADVANTAGE', models.TextField(help_text='what do parents tend to benefit  by entrusting their children in your school not more than 1000 characters', max_length=1000, null=True)),
                ('ADDRESS', models.CharField(max_length=250)),
                ('TOWN', models.CharField(help_text='enter the Local Government Area', max_length=100)),
                ('STATE', models.CharField(choices=[('ABI', 'ABIA'), ('ADA', 'ADAMAWA'), ('AKW', 'AKWA IBOM'), ('ANA', 'ANAMBRA'), ('BAU', 'BAUCHI'), ('BAY', 'BAYELSA'), ('BEN', 'BENUE'), ('BOR', 'BORNO'), ('CRO', 'CROSS RIVER'), ('DEL', 'DELTA'), ('EBO', 'EBONYI'), ('EDO', 'EDO'), ('EKI', 'EKITI'), ('ENU', 'ENUGU'), ('GOM', 'GOMBE'), ('IMO', 'IMO'), ('JIG', 'JIGAWA'), ('KAD', 'KADUNA'), ('KAN', 'KANO'), ('KAT', 'KATSINA'), ('KEB', 'KEBBI'), ('KOG', 'KOGI'), ('KWA', 'KWARA'), ('LAG', 'LAGOS'), ('NAS', 'NASARAWA'), ('NIG', 'NIGER'), ('OGU', 'OGUN'), ('OND', 'ONDO'), ('OSU', 'OSUN'), ('OYO', 'OYO'), ('PLA', 'PLATEAU'), ('RIV', 'RIVERS'), ('SOK', 'SOKOTO'), ('TAR', 'TARABA'), ('YOB', 'YOBE'), ('ZAM', 'ZAMFARA'), ('FCT', 'FEDERAL CAPITAL TERRITORY')], max_length=4)),
                ('VIDEO', models.FileField(blank=True, help_text='upload a video file, mp4, ', upload_to='media/video')),
                ('SCHOOL_TYPE', models.CharField(blank=True, choices=[('Day', 'Day'), ('Boarding', 'Boarding'), ('Boarding and Day', 'Boarding and Day')], max_length=20)),
                ('FEES_RANGE', models.CharField(choices=[('#51,000.00 - #100,000.00', '#51,000.00 - #100,000.00'), ('#101,000.00 - 200,000.00', '#101,000.00 - 200,000.00'), ('#201,000.00  - 300,000.00', '#201,000.00  - 300,000.00'), ('#301,000.00  - 400,000.00', '#301,000.00  - 400,000.00'), ('#401,000.00  - 500,000.00', '#401,000.00  - 500,000.00'), ('#501,000.00  - 600,000.00', '#501,000.00  - 600,000.00'), ('#601,000.00  - 700,000.00', '#601,000.00  - 700,000.00'), ('#701,000.00  - 800,000.00', '#701,000.00  - 800,000.00'), ('#801,000.00  - 900,000.00', '#801,000.00  - 900,000.00'), ('#901,000.00  - 1,000,000.00', '#901,000.00  - 1,000,000.00')], max_length=70, null=True)),
                ('EMAIL', models.EmailField(blank=True, max_length=50)),
                ('PHONE', models.CharField(max_length=15)),
            ],
        ),
    ]