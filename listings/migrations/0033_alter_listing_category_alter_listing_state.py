# Generated by Django 4.2 on 2023-04-27 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0032_alter_listing_category_alter_listing_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Bikes', 'Bikes'), ('Books&Sports', 'Books&Sports'), ('Fashion', 'Fashion'), ('Jobs', 'Jobs'), ('Electronics', 'Electronics'), ('Property', 'Property'), ('Cars', 'Cars'), ('Furniture', 'Furniture'), ('Mobiles', 'Mobiles')], max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='state',
            field=models.CharField(choices=[('UK', 'Uttarakhand'), ('KL', 'Kerala'), ('JH', 'Jharkhand'), ('GA', 'Goa'), ('CG', 'Chhattisgarh'), ('ML', 'Meghalaya'), ('UP', 'Uttar Pradesh'), ('KA', 'Karnataka'), ('AP', 'Andhra Pradesh'), ('TN', 'Tamil Nadu'), ('OD', 'Odisha'), ('MZ', 'Mizoram'), ('HP', 'Haryana'), ('GJ', 'Gujarat'), ('MN', 'Manipur'), ('MP', 'Madhya Pradesh'), ('AR', 'Arunachal Pradesh'), ('MI', 'Sikkim'), ('RJ', 'Rajasthan'), ('PB', 'Punjab'), ('TR', 'Tripura'), ('BR', 'Bihar'), ('WB', 'West Bengal'), ('AS', 'Assam'), ('NL', 'Nagaland'), ('TS', 'Telegana'), ('MH', 'Maharashtra')], max_length=100),
        ),
    ]
