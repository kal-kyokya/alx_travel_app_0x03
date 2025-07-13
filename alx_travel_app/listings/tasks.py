#!/usr/bin/env python
"""
'tasks' creates 'Celery' Email Task
"""
from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_booking_confirmation_email(to_email, booking_info):
    subject = "Booking Confirmation"
    message = f"Your booking was successful!\n\nDetails:\n{booking_info}"
    send_mail(subject, message, 'no-reply@example.com', [to_email])
