# Generated by Django 3.2.4 on 2021-06-16 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Frameworks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('framework_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_university', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('phone_number', models.CharField(max_length=20)),
                ('email_address', models.EmailField(max_length=254, unique=True)),
                ('year', models.CharField(max_length=5)),
                ('course', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('framework_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Interns.frameworks')),
                ('language_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Interns.languages')),
                ('name_of_school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Interns.schoolname')),
            ],
        ),
        migrations.AddField(
            model_name='frameworks',
            name='language_of_framework',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Interns.languages'),
        ),
    ]
