from notion.celery_app import celery
from .models import CropImage

@celery.task(bind=True)
def cropimage_task(self, cropimage_id):
    cropimage = CropImage.objects.get(id=cropimage_id)

    cropimage.save()