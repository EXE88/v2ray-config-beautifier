from django.shortcuts import render , redirect
from django.views import View
from . import forms

class InputCodePageView(View):
    form_class = forms.InputCodePageForm
    template_input = 'main/InputCodePageTemplate.html'
    template_output = 'main/OutPutCodePageTemplate.html'
    
    def get(self,request):
        form = self.form_class()
        return render(request , self.template_input , {'form':form})

    def post(self,request):
        config_code = request.POST['big_field']
        config_code = config_code.split('\n')
        for i in range(len(config_code)):
            try:
                config_code[i] = config_code[i].replace('\n','')
            except Exception as e:
                print(e)
        data = {
            'days_left':config_code[0],
            'irancel_germany':config_code[1],
            'irancel_netherland':config_code[2],
            'irancel_australia':config_code[4],
            'hamrahaval_finland':config_code[3],
            'hamrahaval_germany':config_code[5]
        }
        return render(request,self.template_output,{'data':data})