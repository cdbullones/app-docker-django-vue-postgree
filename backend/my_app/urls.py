from rest_framework import routers
from my_app import viewsets


router = routers.DefaultRouter()
router.register('games', viewsets.GameViewSet)

app_name = 'my_app'

urlpatterns = router.urls
