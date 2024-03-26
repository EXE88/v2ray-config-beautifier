from django.shortcuts import render
from django.views import View

class InputCodePageView(View):
    def get(self,request):
        return render(request , 'main/InputCodePageTemplate.html')
