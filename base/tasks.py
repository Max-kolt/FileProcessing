from .models import File
from celery import shared_task


@shared_task
def file_process(file_instance: File):
    #  TODO: some process for the file
    file_instance.processed = True
    file_instance.save()
