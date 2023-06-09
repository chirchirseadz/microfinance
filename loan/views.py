from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from .models import Loan

# Create your views here.

@login_required(login_url='login')
def loanList(request):
    # data = Loan.objects.filter(is_staff=False, person__company= request.user.person.company)
    loanList = Loan.objects.all()
    context = {
        'data': loanList
    }
    return render(request, 'loan/template_list.html', context)
    
    
# class loanList(LoginRequiredMixin,ListView):
# 	template='loan/template_list'
# 	model=Loan

# 	def get_context_data(self, **kwargs):
# 		context = super(loanList, self).get_context_data(**kwargs)
# 		context['loan_list']=Loan.objects.filter(Q(is_staff=False), person__company= self.request.user.person.company)
# 		return context

	