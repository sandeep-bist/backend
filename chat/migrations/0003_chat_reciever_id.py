# Generated by Django 3.2.6 on 2024-06-21 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_chatmodel_chatnotification_userprofilemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='reciever_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
