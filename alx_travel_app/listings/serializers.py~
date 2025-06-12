from rest_framework import serializers
from .models import Listing, Booking, Review


class ListingSerializer(serializers.Serializer):
    """Enables 'translation' of Python objects to/from JSON
    Inheritance:
    	serializers.Serializer: Handle the actual conversations
    """

    class Meta:
        model = Listing
        fields = ['id', 'name', 'description',
                  'location', 'pricepernight',
                  ]
        read_only_fields = ['created_at', 'updated_at']


class BookingSerializer(serializers.Serializer):
    """Enables 'translation' of Python objects to/from JSON
    Inheritance:
    	serializers.Serializer: Handle the actual conversations
    """

    number_of_nights = serializers.SerializerMethodField()

    class Meta:
        model = Booking
        fields = ['id', 'listing_id',
                  'start_end', 'end_date',
                  'status', 'total_price'
                  ]

    def get_number_of_nights(self, booking_obj):
        """Dynamically computes the number of sessions booked for
        Args:
        	self: A representation of the Booking Serializer instance
        	booking_obj: The current currently processed booking
        Return:
        	The total number of nights booked for
        """
        datetime_obj = booking_obj.end_date - booking_obj.start_date
        nights = (datetime_obj.seconds / 60 / 60 / 24) - 1

        return nights
