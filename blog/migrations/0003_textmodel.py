# Generated by Django 3.2 on 2021-05-26 15:12

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_alter_categorymodel_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='texts_images')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_edit', models.DateTimeField(auto_now=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='texts', to=settings.AUTH_USER_MODEL)),
                ('categories', models.ManyToManyField(related_name='text', to='blog.CategoryModel')),
            ],
            options={
                'verbose_name': 'Text',
                'verbose_name_plural': 'Texts',
                'db_table': 'Text',
            },
        ),
    ]
