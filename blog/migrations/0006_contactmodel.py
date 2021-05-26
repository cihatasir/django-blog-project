# Generated by Django 3.2 on 2021-05-26 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_commentmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=250)),
                ('name_surname', models.CharField(max_length=150)),
                ('message', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contact',
                'db_table': 'Contact',
            },
        ),
    ]
