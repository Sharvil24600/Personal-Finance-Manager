# Generated by Django 3.1.7 on 2021-03-26 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='temp',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'temp_details',
            },
        ),
    ]
