from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def its_alive(request):
    return Response({'message': 'its_alive'})
