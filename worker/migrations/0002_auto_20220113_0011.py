# Generated by Django 3.2.4 on 2022-01-12 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NAME', models.CharField(max_length=100)),
                ('COUNTRY', models.CharField(max_length=50)),
                ('RATING', models.CharField(max_length=3)),
                ('IMGURL', models.URLField(max_length=500)),
                ('TEXT', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]