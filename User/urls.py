from django.urls import path
from User.views import UserListAndCreate,UserDetailChangeAndDelete#, UserViewSet
#from rest_framework.routers import DefaultRouter

"""router = DefaultRouter()
router.register(r'', UserViewSet)

urlpatterns = router.urls
"""
urlpatterns = [
    path('',UserListAndCreate.as_view()),
    path('<int:pk>/',UserDetailChangeAndDelete.as_view()),
]
