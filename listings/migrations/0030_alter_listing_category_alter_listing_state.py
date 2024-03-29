# Generated by Django 4.2 on 2023-04-27 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0029_alter_listing_category_alter_listing_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Books&Sports', 'Books&Sports'), ('Property', 'Property'), ('Fashion', 'Fashion'), ('Bikes', 'Bikes'), ('Electronics', 'Electronics'), ('Jobs', 'Jobs'), ('Mobiles', 'Mobiles'), ('Furniture', 'Furniture'), ('Cars', 'Cars')], max_length=100),
        ),
        migrations.AlterField(
            model_name='listing',
            name='state',
            field=models.CharField(choices=[('MI', 'Sikkim'), ('WB', 'West Bengal'), ('GA', 'Goa'), ('AS', 'Assam'), ('GJ', 'Gujarat'), ('PB', 'Punjab'), ('MN', 'Manipur'), ('NL', 'Nagaland'), ('KA', 'Karnataka'), ('UK', 'Uttarakhand'), ('CG', 'Chhattisgarh'), ('AP', 'Andhra Pradesh'), ('AR', 'Arunachal Pradesh'), ('RJ', 'Rajasthan'), ('MZ', 'Mizoram'), ('OD', 'Odisha'), ('TR', 'Tripura'), ('MP', 'Madhya Pradesh'), ('ML', 'Meghalaya'), ('JH', 'Jharkhand'), ('HP', 'Haryana'), ('UP', 'Uttar Pradesh'), ('TN', 'Tamil Nadu'), ('TS', 'Telegana'), ('KL', 'Kerala'), ('BR', 'Bihar'), ('MH', 'Maharashtra')], max_length=100),
        ),
    ]
