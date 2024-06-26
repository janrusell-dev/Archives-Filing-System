# Generated by Django 4.2.2 on 2024-04-26 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('file_app', '0023_facultyarchives_staffarchives_staffarchivesfile_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addstaffdocument',
            name='campus',
        ),
        migrations.RemoveField(
            model_name='addstaffdocument',
            name='department',
        ),
        migrations.RemoveField(
            model_name='addstaffdocument',
            name='staff',
        ),
        migrations.RemoveField(
            model_name='archives',
            name='campus',
        ),
        migrations.RemoveField(
            model_name='archives',
            name='department',
        ),
        migrations.RemoveField(
            model_name='archives',
            name='staff',
        ),
        migrations.RemoveField(
            model_name='archivesfile',
            name='archives',
        ),
        migrations.DeleteModel(
            name='AddFacultyDocument',
        ),
        migrations.DeleteModel(
            name='AddStaffDocument',
        ),
        migrations.DeleteModel(
            name='Archives',
        ),
        migrations.DeleteModel(
            name='ArchivesFile',
        ),
    ]
