# Generated by Django 4.0 on 2022-05-06 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Import',
            fields=[
                ('ship', models.CharField(blank=True, max_length=100, null=True)),
                ('import_id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateField(blank=True, null=True)),
                ('terminal', models.CharField(blank=True, max_length=20, null=True)),
                ('container_number', models.CharField(blank=True, max_length=20, null=True)),
                ('container_size', models.IntegerField(blank=True, null=True)),
                ('container_type', models.CharField(blank=True, max_length=10, null=True)),
                ('goods_name_rus', models.CharField(blank=True, max_length=1500, null=True)),
                ('consignment', models.CharField(blank=True, max_length=100, null=True)),
                ('shipper', models.CharField(blank=True, max_length=500, null=True)),
                ('consignee', models.CharField(blank=True, max_length=500, null=True)),
                ('line', models.CharField(blank=True, max_length=500, null=True)),
                ('count', models.CharField(blank=True, max_length=1500, null=True)),
                ('teu', models.IntegerField(blank=True, null=True)),
                ('voyage', models.CharField(blank=True, max_length=1500, null=True)),
                ('shipper_country', models.CharField(blank=True, max_length=50, null=True)),
                ('goods_weight', models.FloatField(blank=True, null=True)),
                ('package_number', models.CharField(blank=True, max_length=10, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('shipper_seaport', models.CharField(blank=True, max_length=50, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('month', models.IntegerField(blank=True, null=True)),
                ('goods_tnved', models.CharField(blank=True, max_length=20, null=True)),
                ('parsed_on', models.DateField(blank=True, null=True)),
                ('month_parsed_on', models.IntegerField(blank=True, null=True)),
                ('year_parsed_on', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'import',
                'managed': False,
            },
        ),
    ]