from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    class Meta:
        abstract = True


class Article(BaseModel):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name="Заголовок")
    author = models.CharField(max_length=200, null=False, blank=False, verbose_name="Автор", default="Unknown",
                              validators=(MinLengthValidator(5),))
    content = models.TextField(max_length=2000, null=False, blank=False, verbose_name="Контент")
    tags = models.ManyToManyField("webapp.Tag", related_name="articles")

    types = models.ManyToManyField("webapp.Type", related_name="articles")
    status = models.ForeignKey("webapp.Status", related_name="articles", on_delete=models.CASCADE, verbose_name="Статус")

    def __str__(self):
        return f"{self.pk}. {self.author}: {self.title}"

    class Meta:
        db_table = 'articles'
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Type(models.Model):
    name = models.CharField(max_length=50, verbose_name="Тип")

    def __str__(self):
        return f"{self.name}"


class Status(models.Model):
    name = models.CharField(max_length=50, verbose_name="Статус")

    def __str__(self):
        return f"{self.name}"


class Tag(BaseModel):
    name = models.CharField(max_length=30, verbose_name="Тег")

    def __str__(self):
        return f"{self.pk} - {self.name}"

    class Meta:
        db_table = 'tags'
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Comment(BaseModel):
    content = models.TextField(max_length=2000, verbose_name="Контент")
    author = models.CharField(max_length=200, null=True, blank=True, verbose_name="Автор", default="Аноним")
    article = models.ForeignKey("webapp.Article", on_delete=models.CASCADE,
                                related_name="comments",
                                verbose_name="Статья",
                                )

    class Meta:
        db_table = 'comments'
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
