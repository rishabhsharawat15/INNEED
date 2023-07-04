# Generated by Django 4.2 on 2023-04-25 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0017_alter_listing_category_alter_listing_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Mobiles', 'Mobiles'), ('Jobs', 'Jobs'), ('Cars', 'Cars'), ('Electronics', 'Electronics'), ('Property', 'Property'), ('Books&Sports', 'Books&Sports'), ('Furniture', 'Furniture'), ('Bikes', 'Bikes'), ('Fashion', 'Fashion')], max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='state',
            field=models.CharField(choices=[('WB', 'West Bengal'), ('MN', 'Manipur'), ('AR', 'Arunachal Pradesh'), ('KA', 'Karnataka'), ('MZ', 'Mizoram'), ('GA', 'Goa'), ('TS', 'Telegana'), ('UK', 'Uttarakhand'), ('MH', 'Maharashtra'), ('AP', 'Andhra Pradesh'), ('JH', 'Jharkhand'), ('CG', 'Chhattisgarh'), ('ML', 'Meghalaya'), ('AS', 'Assam'), ('RJ', 'Rajasthan'), ('TR', 'Tripura'), ('HP', 'Haryana'), ('UP', 'Uttar Pradesh'), ('KL', 'Kerala'), ('TN', 'Tamil Nadu'), ('OD', 'Odisha'), ('BR', 'Bihar'), ('MI', 'Sikkim'), ('PB', 'Punjab'), ('GJ', 'Gujarat'), ('NL', 'Nagaland'), ('MP', 'Madhya Pradesh')], max_length=100),
        ),
    ]
