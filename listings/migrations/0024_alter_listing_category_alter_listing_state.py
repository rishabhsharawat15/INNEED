# Generated by Django 4.2 on 2023-04-26 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0023_alter_listing_category_alter_listing_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Bikes', 'Bikes'), ('Jobs', 'Jobs'), ('Cars', 'Cars'), ('Mobiles', 'Mobiles'), ('Fashion', 'Fashion'), ('Property', 'Property'), ('Books&Sports', 'Books&Sports'), ('Furniture', 'Furniture'), ('Electronics', 'Electronics')], max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='state',
            field=models.CharField(choices=[('WB', 'West Bengal'), ('PB', 'Punjab'), ('NL', 'Nagaland'), ('MN', 'Manipur'), ('TS', 'Telegana'), ('BR', 'Bihar'), ('JH', 'Jharkhand'), ('ML', 'Meghalaya'), ('AS', 'Assam'), ('KL', 'Kerala'), ('UP', 'Uttar Pradesh'), ('TN', 'Tamil Nadu'), ('AP', 'Andhra Pradesh'), ('GJ', 'Gujarat'), ('MI', 'Sikkim'), ('AR', 'Arunachal Pradesh'), ('KA', 'Karnataka'), ('MZ', 'Mizoram'), ('HP', 'Haryana'), ('MH', 'Maharashtra'), ('TR', 'Tripura'), ('UK', 'Uttarakhand'), ('OD', 'Odisha'), ('MP', 'Madhya Pradesh'), ('RJ', 'Rajasthan'), ('GA', 'Goa'), ('CG', 'Chhattisgarh')], max_length=100),
        ),
    ]
