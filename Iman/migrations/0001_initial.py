# Generated by Django 3.0.4 on 2020-04-20 08:51

import Iman.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=200)),
            ],
            options={
                'permissions': (('can_addbank', 'Can Add Bank'),),
            },
        ),
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Iman.Companies')),
            ],
            options={
                'permissions': (('can_addcompany', 'Can Add Company'),),
            },
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('cash', models.CharField(default='0', max_length=100)),
                ('date_time', models.DateTimeField()),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=Iman.models.upload_to)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Iman.Bank')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Iman.Companies')),
            ],
            options={
                'permissions': (('can_addtranscation', 'Can Add Transactions'), ('can_viewtransacctions', 'Can View All Transactions')),
            },
        ),
    ]