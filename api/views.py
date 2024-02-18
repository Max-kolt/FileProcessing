from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from .serializers import FileSerializer
from base.models import File
from base import tasks


@api_view(['POST'])
@parser_classes([FileUploadParser])
def load_file(request, filename):
    print(request.data.get('file'))
    serialized_data = FileSgit
    erializer(data={'file': request.data.get('file')})
    serialized_data.is_valid(raise_exception=True)
    serialized_data.save()
    print(serialized_data.data)
    tasks.file_process.delay(File(**serialized_data.validated_data))
    return Response(status=status.HTTP_201_CREATED, data=serialized_data.data)


@api_view(['GET'])
def get_files(request):
    data_output = File.objects.all()
    if not data_output:
        return Response(status=status.HTTP_404_NOT_FOUND, data={"message": "Files not found"})

    serialized_data = FileSerializer(data=data_output, many=True)
    if serialized_data.is_valid():
        return Response(status=status.HTTP_200_OK, data=serialized_data.data)

    return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
