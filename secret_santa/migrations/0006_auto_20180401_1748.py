# Generated by Django 2.0.1 on 2018-04-01 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secret_santa', '0005_giftpair'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='giftlistpairing',
            name='gift_pair_original_list',
        ),
        migrations.DeleteModel(
            name='GiftListPairing',
        ),
    ]