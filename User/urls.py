from django.urls import path
from User.views import UserListAndCreate,UserDetailChangeAndDelete


urlpatterns = [
    path('',UserListAndCreate.as_view()),
    path('<int:user_id>/',UserDetailChangeAndDelete.as_view()),
]
