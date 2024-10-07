from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

def homepage(request):
    data = {
        "name" : "Nick",
        "age" : 25,
        "role": "Admin",
        "numbers": [1,2,3,4,5],
        "marks":{
            "Tamil":97,
            "English":92
        }
    }
    return render(request, 'home.html',data)

def about(request):
    info = {
        "company_name": "E2 Infosystems",
        "description": "A customer driven technology company",
        "team": ["John","Ram","Raju","Nick"]
    }
    return render(request,'about.html',info)

class service(View):
    def get(self,request):
        service_data = {
            "services": [{"name": "Web Development", "description": "Building modern websites"},
                {"name": "App Development", "description": "Creating mobile applications"},
                {"name": "SEO Services", "description": "Optimizing your site for search engines"}]
        }
        return render (request,'services.html',service_data)
    
class contact(View):
    def get(self,request):
        contact_info = {
            "email": "support@e2infosystems.com",
            "phone": 9087654321,
            "Address": "123 Tech Park, Silicon Valley"
        }    
        return render (request,'contact.html',contact_info)