# Generated by Django 4.2.3 on 2023-08-09 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_cart_watchlist_watchitems_review_cartitems_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='username',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
