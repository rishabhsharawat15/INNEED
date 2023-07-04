# Generated by Django 4.2 on 2023-04-27 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0028_alter_listing_category_alter_listing_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Electronics', 'Electronics'), ('Mobiles', 'Mobiles'), ('Cars', 'Cars'), ('Property', 'Property'), ('Furniture', 'Furniture'), ('Bikes', 'Bikes'), ('Fashion', 'Fashion'), ('Books&Sports', 'Books&Sports'), ('Jobs', 'Jobs')], max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='state',
            field=models.CharField(choices=[('MH', 'Maharashtra'), ('AR', 'Arunachal Pradesh'), ('NL', 'Nagaland'), ('UP', 'Uttar Pradesh'), ('RJ', 'Rajasthan'), ('KA', 'Karnataka'), ('MN', 'Manipur'), ('HP', 'Haryana'), ('CG', 'Chhattisgarh'), ('AS', 'Assam'), ('PB', 'Punjab'), ('KL', 'Kerala'), ('TR', 'Tripura'), ('UK', 'Uttarakhand'), ('MZ', 'Mizoram'), ('TS', 'Telegana'), ('WB', 'West Bengal'), ('MP', 'Madhya Pradesh'), ('GJ', 'Gujarat'), ('ML', 'Meghalaya'), ('GA', 'Goa'), ('JH', 'Jharkhand'), ('AP', 'Andhra Pradesh'), ('OD', 'Odisha'), ('MI', 'Sikkim'), ('BR', 'Bihar'), ('TN', 'Tamil Nadu')], max_length=100),
        ),
    ]
