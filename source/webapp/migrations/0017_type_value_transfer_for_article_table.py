# Generated by Django 4.0 on 2022-01-26 13:18

from django.db import migrations


def transfer_types(apps, schema_editor):
    Article = apps.get_model('webapp.Article')

    for article in Article.objects.all():
        article.types.add(article.type_old)


def rollback_transfer(apps, schema_editor):
    Article = apps.get_model('webapp.Article')
    Type = apps.get_model('webapp.Type')

    for article in Article.objects.all():
        if article.types.all().exists():
            article.type_old = article.types.first()
        else:
            article.type_old = Type.objects.first()



class Migration(migrations.Migration):
    dependencies = [
        ('webapp', '0016_article_types'),
    ]

    operations = [
        migrations.RunPython(transfer_types, rollback_transfer)
    ]