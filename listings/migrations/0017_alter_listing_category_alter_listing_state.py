# Generated by Django 4.2 on 2023-04-25 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0016_alter_listing_category_alter_listing_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Cars', 'Cars'), ('Mobiles', 'Mobiles'), ('Furniture', 'Furniture'), ('Jobs', 'Jobs'), ('Electronics', 'Electronics'), ('Bikes', 'Bikes'), ('Books&Sports', 'Books&Sports'), ('Fashion', 'Fashion'), ('Property', 'Property')], max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='state',
            field=models.CharField(choices=[('UP', 'Uttar Pradesh'), ('AS', 'Assam'), ('WB', 'West Bengal'), ('AP', 'Andhra Pradesh'), ('HP', 'Haryana'), ('OD', 'Odisha'), ('UK', 'Uttarakhand'), ('RJ', 'Rajasthan'), ('JH', 'Jharkhand'), ('MN', 'Manipur'), ('KA', 'Karnataka'), ('AR', 'Arunachal Pradesh'), ('BR', 'Bihar'), ('MH', 'Maharashtra'), ('KL', 'Kerala'), ('TR', 'Tripura'), ('MZ', 'Mizoram'), ('NL', 'Nagaland'), ('GJ', 'Gujarat'), ('TS', 'Telegana'), ('MP', 'Madhya Pradesh'), ('GA', 'Goa'), ('ML', 'Meghalaya'), ('PB', 'Punjab'), ('CG', 'Chhattisgarh'), ('MI', 'Sikkim'), ('TN', 'Tamil Nadu')], max_length=100),
        ),
    ]
