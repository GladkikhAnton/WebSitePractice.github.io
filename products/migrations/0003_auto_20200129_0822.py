# Generated by Django 3.0.2 on 2020-01-29 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeOfProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=32, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Тип товара',
                'verbose_name_plural': 'Типы товаров',
            },
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='product_images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='products.TypeOfProduct'),
        ),
    ]