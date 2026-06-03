from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.title} {self.created_at}"

class ContactInfo(models.Model):
    name = models.CharField(max_length=200)
    secondName = models.CharField(max_length=200)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=50)
    notes = models.TextField()

    def __str__(self) -> str:
        return f"{self.name} {self.secondName} {self.email} {self.phoneNumber} {self.notes}"

class Product(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    price = models.IntegerField(default=100)
    quantity = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.title} ({self.price})"

class Buyer(models.Model):
    name = models.CharField(max_length=200, blank=False)
    secondName = models.CharField(max_length=200, blank=False)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=50)
    def __str__(self) -> str:
        return f"{self.name} {self.secondName} {self.email} {self.phoneNumber}"

class Seller(models.Model):
    ROLE_CHOICES = [
        ("seller", "Продавец"),
        ("primeSeller", "Главный продавец"),
        ("sales_manager", "Керівник відділу продажів")
    ]

    name = models.CharField(max_length=200, blank=False)
    secondName = models.CharField(max_length=200, blank=False)
    email = models.EmailField()
    phoneNumber = models.CharField(max_length=50)
    start_at = models.DateField(auto_now_add=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="seller")

    def __str__(self) -> str:
        return f"{self.name} {self.secondName} - {self.get_role_display()}"

class SellInfo(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    price = models.IntegerField(blank=False)
    quantity = models.IntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.product} - {self.buyer} - {self.seller} ({self.created_at})"

class RestauranTypes(models.Model):
    typeName = models.CharField(max_length=100)
    def __str__(self) -> str:
        return f"{self.id} {self.typeName}"

class Restauran(models.Model):
    name = models.CharField(max_length=50, blank=False)
    restauranType = models.ManyToManyField(RestauranTypes)
    adress = models.CharField(max_length=50, blank=False)
    phoneNumber = models.CharField(max_length=50)
    website = models.URLField(blank=False)
    def __str__(self) -> str:
        return f"{self.id} {self.name}"


class Review(models.Model):
    review = models.TextField(blank=False)
    created_at = models.DateField(auto_now=True)
    restauran = models.ForeignKey(Restauran, on_delete=models.CASCADE)
    isVisible = models.BooleanField(default=True)
    def __str__(self) -> str:
        return f"{self.id} {self.review}"

class RestauranPhotos(models.Model):
    photoName = models.CharField(max_length=50, blank=False)
    restauran = models.ForeignKey(Restauran, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f"{self.id} {self.photoName}"
