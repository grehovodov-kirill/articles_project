# Generated by Django 4.0 on 2022-01-26 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0014_rename_type_article_type_old'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='type_old',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles_old', to='webapp.type', verbose_name='Тип'),
        ),
    ]