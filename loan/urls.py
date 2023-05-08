from django.conf.urls import url
from . import views 


app_name='Loan Manager'

urlpatterns = [
url('', views.loanList, name='loan_list'),
]
