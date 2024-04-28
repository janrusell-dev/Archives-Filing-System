# Generated by Django 4.2.2 on 2024-04-25 00:34

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('file_app', '0013_facultydocument_facultyimage_staffdocument_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SfDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField()),
                ('date_added', models.DateField(default=django.utils.timezone.now)),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='file_app.campus')),
                ('department', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='file_app.department')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='file_app.staff')),
            ],
        ),
        migrations.CreateModel(
            name='SfFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_files', models.FileField(upload_to='staff_files/')),
                ('staff_docs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='file_app.sfdocument')),
            ],
        ),
    ]