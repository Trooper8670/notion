from django.contrib import admin
from .models import CropImage
from users.models import ExtendUser
from image_cropping import ImageCroppingMixin

class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(CropImage, MyModelAdmin)
admin.site.register(ExtendUser)
