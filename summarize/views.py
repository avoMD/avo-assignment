from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .service import summarize


@api_view(["POST"])
def summarize_view(request):
    patient_info = request.data.get("patient_info", "").strip()
    if not patient_info:
        return Response({"error": "patient_info is required"}, status=status.HTTP_400_BAD_REQUEST)
    return Response({"result": summarize(patient_info)})
