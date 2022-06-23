from django.db import router
from rest_framework import routers
from.api import VoxViewSet

router=routers.DefaultRouter()
router.register('api/vox',VoxViewSet,'vox')



urlpatterns = router.urls
