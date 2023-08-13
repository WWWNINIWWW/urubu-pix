from django.urls import path
from values.views import ValuesList,ValuesDetail

urlpatterns = [
    path('',ValuesList.as_view()),
    path('<int:user_id>/',ValuesDetail.as_view()),
]