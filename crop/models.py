from django.db import models
from image_cropping import ImageRatioField

class CropImage(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(blank=True, upload_to='uploaded_images')
    # size is "width x height"
    crop = ImageRatioField('logo', '430x360', free_crop=True)
