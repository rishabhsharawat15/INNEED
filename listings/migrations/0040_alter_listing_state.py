# Generated by Django 4.2 on 2023-07-04 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0039_alter_listing_category_alter_listing_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='state',
            field=models.CharField(choices=[('CG', 'Chhattisgarh'), ('TR', 'Tripura'), ('TS', 'Telegana'), ('AP', 'Andhra Pradesh'), ('UK', 'Uttarakhand'), ('GJ', 'Gujarat'), ('WB', 'West Bengal'), ('TN', 'Tamil Nadu'), ('BR', 'Bihar'), ('MH', 'Maharashtra'), ('AS', 'Assam'), ('AR', 'Arunachal Pradesh'), ('MZ', 'Mizoram'), ('NL', 'Nagaland'), ('GA', 'Goa'), ('PB', 'Punjab'), ('RJ', 'Rajasthan'), ('MI', 'Sikkim'), ('KA', 'Karnataka'), ('MP', 'Madhya Pradesh'), ('JH', 'Jharkhand'), ('MN', 'Manipur'), ('UP', 'Uttar Pradesh'), ('OD', 'Odisha'), ('ML', 'Meghalaya'), ('KL', 'Kerala'), ('HP', 'Haryana')], max_length=100),
        ),
    ]
