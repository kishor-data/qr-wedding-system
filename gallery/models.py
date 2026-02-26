from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File


class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    qr_code = models.ImageField(upload_to="qr_codes/", blank=True)

    def __str__(self):
        return self.event_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.qr_code:
            qr = qrcode.make(f"http://127.0.0.1:8000/event/{self.id}/")
            buffer = BytesIO()
            qr.save(buffer, format='PNG')
            file_name = f"event_{self.id}_qr.png"
            self.qr_code.save(file_name, File(buffer), save=False)

        super().save(*args, **kwargs)


class EventImage(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="event_images/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.event.event_name}"