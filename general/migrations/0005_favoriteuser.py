# Generated by Django 3.0.6 on 2020-05-22 11:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('general', '0004_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='substituted', to='general.Product')),
                ('substitute_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='substitute', to='general.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Favorites User',
            },
        ),
    ]
