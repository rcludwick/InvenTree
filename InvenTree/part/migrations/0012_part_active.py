# Generated by Django 2.2 on 2019-04-28 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part', '0011_auto_20190428_0841'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='active',
            field=models.BooleanField(default=True, help_text='Is this part active?'),
        ),
    ]