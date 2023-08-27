# Generated by Django 4.2.4 on 2023-08-27 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('age', models.IntegerField()),
                ('dep', models.CharField(blank=True, max_length=2, verbose_name='department')),
            ],
            options={
                'db_table': 'Student Table',
                'get_latest_by': ['-age', 'name'],
            },
        ),
    ]