# Generated by Django 4.2.5 on 2024-11-21 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db_train', '0002_alter_author_options_alter_author_bio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.IntegerField(blank=True, default=0, help_text='Стаж в годах', verbose_name='Стаж')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='db_train.author')),
            ],
        ),
    ]
