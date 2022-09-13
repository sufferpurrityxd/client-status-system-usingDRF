# Generated by Django 4.1.1 on 2022-09-13 14:14

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_alter_clientpromocode_secret_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientpromocode',
            name='expiration_date',
            field=models.DateField(default=datetime.date(2022, 9, 20), verbose_name='Expiration Date'),
        ),
        migrations.AlterField(
            model_name='clientpromocode',
            name='secret_number',
            field=models.CharField(default='XK6ZdL', max_length=6, verbose_name='Client promocode'),
        ),
        migrations.CreateModel(
            name='ClientReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(blank=True, max_length=250, null=True, verbose_name='Review')),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)], verbose_name='Rating')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='The date the review was created')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clients.client')),
            ],
        ),
    ]
