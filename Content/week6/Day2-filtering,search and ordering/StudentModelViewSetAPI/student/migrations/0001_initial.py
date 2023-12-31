# Generated by Django 4.2.4 on 2023-08-28 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('age', models.IntegerField()),
                ('dep', models.CharField(blank=True, max_length=2, verbose_name='department')),
                ('borrowed_book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Books.book')),
            ],
            options={
                'db_table': 'Student Table',
                'get_latest_by': ['-age', 'name'],
            },
        ),
    ]
