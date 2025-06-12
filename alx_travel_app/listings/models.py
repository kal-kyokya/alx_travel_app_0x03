from django.db import models
from uuid import uuid4


class Listing(models.Model):
    """Python representation of the 'Listing' DB table
    Inheritance:
    	models.Model: Built-in class enabling Django's ORM to 'convert' Listing
    """

    listing_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=255)
    pricepernight = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'My Listing'
        verbose_name_plural = 'My Listings'
        order = ['created_at', 'pricepernight']

    def __str__(self):
        return self.name


class Booking(models.Model):
    """Python representation of the 'Booking' DB table
    Inheritance:
    	models.Model: Built-in class enabling Django's ORM to 'convert' Booking
    """

    STATUS = [
        ('⏰', 'pending'),
        ('✅', 'confirmed'), 
        ('❌', 'cancelled'),
    ]

    booking_id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.FloatField()
    status = models.CharField(max_length=255, choices=STATUS)
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE)


class Review(models.Model):
    """Python representation of the 'Review' DB table
    Inheritance:
    	models.Model: Built-in class enabling Django's ORM to 'convert' Review
    """

    review_id = models.UUIDField(primary_key=True, default=True, editable=False)
    rating = models.FloatField()
    comment = models.TextField(blank=True, null=True)
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE)
