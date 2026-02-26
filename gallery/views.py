from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, EventImage


def event_list(request):
    events = Event.objects.all()
    return render(request, "gallery/event_list.html", {"events": events})


def event_detail(request, id):
    event = get_object_or_404(Event, id=id)

    if request.method == "POST":
        image_file = request.FILES.get("image")
        if image_file:
            EventImage.objects.create(
                event=event,
                image=image_file
            )
            return redirect("event_detail", id=event.id)

    return render(request, "gallery/event_detail.html", {"event": event})