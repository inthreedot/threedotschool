# Generated by Django 4.1.7 on 2023-03-22 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admittedStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=255)),
                ('father_name', models.CharField(max_length=255)),
                ('mother_name', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('sex', models.CharField(max_length=17)),
                ('mobile_number', models.CharField(max_length=15)),
                ('alternate_mobile_number', models.CharField(max_length=15)),
                ('aadhaar_number', models.CharField(max_length=15)),
                ('village_town', models.CharField(max_length=255)),
                ('post_office', models.CharField(max_length=255)),
                ('police_station', models.CharField(max_length=255)),
                ('gaon_panchayat', models.CharField(max_length=255)),
                ('educational_block', models.CharField(max_length=255)),
                ('cluster', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('pin', models.CharField(max_length=6)),
                ('class_admitted', models.CharField(max_length=20)),
                ('bank_name', models.CharField(max_length=255)),
                ('account_number', models.CharField(max_length=30)),
                ('bank_branch_name', models.CharField(max_length=255)),
                ('ifsc_code', models.CharField(max_length=11)),
                ('student_photo', models.ImageField(upload_to='student_photos')),
                ('student_document', models.FileField(upload_to='student_documents')),
            ],
        ),
    ]