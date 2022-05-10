# Generated by Django 3.2.1 on 2022-05-10 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('aadhar', models.FileField(upload_to='media')),
                ('pancard', models.FileField(upload_to='media')),
                ('salary', models.FileField(upload_to='media')),
                ('photo', models.FileField(upload_to='media')),
                ('bank', models.TextField()),
                ('ctc', models.IntegerField()),
                ('loan', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_amt', models.IntegerField()),
                ('acc_rej', models.BooleanField()),
            ],
        ),
    ]
