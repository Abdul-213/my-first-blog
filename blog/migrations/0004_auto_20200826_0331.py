# Generated by Django 2.2.15 on 2020-08-26 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_person'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='Posty',
        ),
    ]