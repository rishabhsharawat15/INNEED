# Generated by Django 4.2 on 2023-04-27 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0027_alter_listing_category_alter_listing_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Electronics', 'Electronics'), ('Fashion', 'Fashion'), ('Furniture', 'Furniture'), ('Cars', 'Cars'), ('Property', 'Property'), ('Books&Sports', 'Books&Sports'), ('Bikes', 'Bikes'), ('Mobiles', 'Mobiles'), ('Jobs', 'Jobs')], max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='state',
            field=models.CharField(choices=[('GJ', 'Gujarat'), ('UK', 'Uttarakhand'), ('TR', 'Tripura'), ('UP', 'Uttar Pradesh'), ('TS', 'Telegana'), ('AP', 'Andhra Pradesh'), ('RJ', 'Rajasthan'), ('MH', 'Maharashtra'), ('AR', 'Arunachal Pradesh'), ('MP', 'Madhya Pradesh'), ('NL', 'Nagaland'), ('PB', 'Punjab'), ('KL', 'Kerala'), ('WB', 'West Bengal'), ('GA', 'Goa'), ('MZ', 'Mizoram'), ('BR', 'Bihar'), ('KA', 'Karnataka'), ('HP', 'Haryana'), ('JH', 'Jharkhand'), ('MN', 'Manipur'), ('CG', 'Chhattisgarh'), ('ML', 'Meghalaya'), ('TN', 'Tamil Nadu'), ('MI', 'Sikkim'), ('OD', 'Odisha'), ('AS', 'Assam')], max_length=100),
        ),
    ]
