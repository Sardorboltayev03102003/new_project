from django.db import models

# """cool_author"""


class Services(models.Model):
    name = models.CharField(max_length=100, verbose_name="Services nomi")
    title = models.TextField(verbose_name="Services haqida ")
    image = models.ImageField(upload_to="image/")
    created_at = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "serverlar"


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategoriya nomlari")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Mahsulot  nomi")
    title = models.TextField(verbose_name="Mahsulot haqida ")
    image = models.ImageField(upload_to="media/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Mahsulot"


class About(models.Model):
    year = models.CharField(max_length=50, verbose_name="Ochilgan yili")
    name = models.CharField(max_length=100, verbose_name="companiya nomi")
    body = models.TextField(verbose_name="Jamoa haqida")
    image = models.ImageField(upload_to="year/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Guruh"


class Team(models.Model):
    name = models.CharField(max_length=30, verbose_name="M name")
    job = models.CharField(max_length=200, verbose_name="Kasbi")
    image = models.ImageField(upload_to="team/")
    tw_link = models.URLField(max_length=4000, verbose_name="link")
    fb_link = models.URLField(max_length=4000, verbose_name="link")
    in_link = models.URLField(max_length=4000, verbose_name="link")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Jamoa"


class Contact(models.Model):
    name = models.CharField(max_length=200, verbose_name="f nomi")
    email = models.EmailField(max_length=200, unique=True)
    number = models.CharField(max_length=30, verbose_name="f nomeri")
    subject = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "kontack"


