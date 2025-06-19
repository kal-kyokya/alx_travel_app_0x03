from rest_framework.viewsets import ModelViewSet
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer


# --------------------------------------------------
# Full CRUD for 'Listing' model out of the box.
# --------------------------------------------------
class ListingViewSet(ModelViewSet):
    """Handles API calls to '/listings'.
    Inheritance:
    	ModelViewSet: Collection of Django predefined CRUD executing methods and required attributes.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


# --------------------------------------------------
# Full CRUD for 'Booking' model out of the box.
# --------------------------------------------------
class BookingViewSet(ModelViewSet):
    """Handles API calls to '/bookings'.
    Inheritance:
    	ModelViewSet: Collection of Django predefined CRUD executing methods and required attributes.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
