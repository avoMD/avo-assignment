from django.http import JsonResponse

from .models import Seed


def health(request):
    seed = Seed.objects.get(key="status")
    return JsonResponse({"status": seed.value})
