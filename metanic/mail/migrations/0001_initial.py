# Generated by Django 2.1b1 on 2018-07-01 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MailEventLogModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('token', models.CharField(db_index=True, max_length=64)),
                ('raw_data', models.TextField()),
            ],
            options={
                'ordering': ('-last_modified', '-created'),
                'abstract': False,
            },
        ),
    ]
