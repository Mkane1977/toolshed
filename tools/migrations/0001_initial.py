# Generated by Django 4.1.4 on 2022-12-20 00:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('model', models.CharField(max_length=500)),
                ('type', models.CharField(max_length=200)),
                ('charger', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Toolshed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('shed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tools.tool')),
            ],
        ),
    ]
