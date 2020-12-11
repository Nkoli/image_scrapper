from .models import Image
from .serializers import ImageSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class ImageList(APIView):
    def get(self, request):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)
