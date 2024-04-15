# Generated by Django 4.2.2 on 2024-04-07 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(default='', max_length=100)),
                ('suffix_name', models.CharField(blank=True, max_length=50, null=True)),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='file_app.campus')),
                ('department', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='file_app.department')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(default='', max_length=100)),
                ('suffix_name', models.CharField(blank=True, max_length=50, null=True)),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='file_app.campus')),
                ('department', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='file_app.department')),
            ],
        ),
        migrations.CreateModel(
            name='AddStaffDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_file', models.FileField(upload_to='')),
                ('date_added', models.DateField()),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='file_app.campus')),
                ('department', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='file_app.department')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='file_app.staff')),
            ],
        ),
        migrations.CreateModel(
            name='AddFacultyDocument',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_file', models.FileField(upload_to='')),
                ('date_added', models.DateField()),
                ('campus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='file_app.campus')),
                ('department', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='file_app.department')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='file_app.faculty')),
            ],
        ),
    ]
