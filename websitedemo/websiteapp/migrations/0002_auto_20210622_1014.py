# Generated by Django 3.2.4 on 2021-06-22 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websiteapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aboutus',
            old_name='adesc',
            new_name='desc1',
        ),
        migrations.RenameField(
            model_name='aboutus',
            old_name='aheading',
            new_name='heading',
        ),
        migrations.RenameField(
            model_name='aboutus',
            old_name='aimg',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='clients',
            old_name='cheading',
            new_name='heading',
        ),
        migrations.RenameField(
            model_name='clients',
            old_name='cimg',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='features',
            old_name='fdesc',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='features',
            old_name='fheading',
            new_name='heading',
        ),
        migrations.RenameField(
            model_name='features',
            old_name='fimg',
            new_name='img',
        ),
        migrations.AddField(
            model_name='aboutus',
            name='desc2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='aboutus',
            name='desc3',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
