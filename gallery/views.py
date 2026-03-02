from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Event


def event_list(request):
    events = Event.objects.all()
    return render(request, "gallery/event_list.html", {"events": events})


def event_detail(request, id):
    event = get_object_or_404(Event, id=id)

    if request.method == "POST":
        image = request.FILES.get("image")
        if image:
            event.images.create(image=image)

    return render(request, "gallery/event_detail.html", {"event": event})


def create_admin(request):
    if not User.objects.filter(username="kishore").exists():
        User.objects.create_superuser(
            "kishore",
            "pavandhandru587@gmail.com",
            "kishore@123"
        )
        return HttpResponse("Admin created successfully")
    return HttpResponse("Admin already exists")


