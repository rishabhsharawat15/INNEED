# Generated by Django 4.2 on 2023-04-25 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0018_alter_listing_category_alter_listing_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Fashion', 'Fashion'), ('Mobiles', 'Mobiles'), ('Books&Sports', 'Books&Sports'), ('Electronics', 'Electronics'), ('Furniture', 'Furniture'), ('Cars', 'Cars'), ('Property', 'Property'), ('Jobs', 'Jobs'), ('Bikes', 'Bikes')], max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='state',
            field=models.CharField(choices=[('AP', 'Andhra Pradesh'), ('NL', 'Nagaland'), ('MP', 'Madhya Pradesh'), ('OD', 'Odisha'), ('MH', 'Maharashtra'), ('TR', 'Tripura'), ('TS', 'Telegana'), ('CG', 'Chhattisgarh'), ('GA', 'Goa'), ('GJ', 'Gujarat'), ('AR', 'Arunachal Pradesh'), ('AS', 'Assam'), ('MN', 'Manipur'), ('RJ', 'Rajasthan'), ('KL', 'Kerala'), ('MI', 'Sikkim'), ('JH', 'Jharkhand'), ('WB', 'West Bengal'), ('UP', 'Uttar Pradesh'), ('MZ', 'Mizoram'), ('TN', 'Tamil Nadu'), ('ML', 'Meghalaya'), ('BR', 'Bihar'), ('UK', 'Uttarakhand'), ('PB', 'Punjab'), ('HP', 'Haryana'), ('KA', 'Karnataka')], max_length=100),
        ),
    ]
