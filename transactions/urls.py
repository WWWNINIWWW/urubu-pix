from django.urls import path
from transactions.views import TransactionsList,TransactionsDetail

urlpatterns = [
    path('',TransactionsList.as_view()),
    path('<int:user_id>/',TransactionsDetail.as_view()),
]