
from lawapi.viewsets import LawViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('laws', LawViewset)
