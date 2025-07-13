from rest_framework.viewsets import ModelViewSet
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer
from .tasks import send_booking_confirmation_email


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

    def perform_create(self, serializer):
        booking = serializer.save()
        user_email = booking.customer.email
        info = f"ID: {booking.id}, Date: {booking.date}, Total: {booking.total}"
        send_booking_confirmation_email.delay(user_email, info)
