from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseNotFound, HttpResponseRedirect
# Create your views here.
from django.urls import reverse 
from django.http import HttpResponseNotFound
#from django.template.loader import render_to_string



def options(request):
    lists = ["demo", "contact"]
    return render(request, "welcome/welcome.html", {
        "options": lists  # must match template name
    }

    )



def demo(request):
    # You’ll implement later
    #return HttpResponse("Demo Page (to be implemented)")
    return render(request, "welcome/index.html", {
      })


    

def contact(request, contactu):
    allowed = ["contact", "con"]   # only allow these

    if contactu not in allowed:
        return render(request, "welcome/404.html", status=404)

    # otherwise, show contact info
    TEXT = "contact us on demo@yahoo.com"
    response_data = f"<h1>{TEXT}</h1>"
    return HttpResponse(response_data)






#def contact_info(request, contactu):


 #   return HttpResponse(f"contact us on demo@yahoo.com ")




"""<!-- 
Django processes welcome.html:
- It sees {% extends "base.html" %}.
- It loads base.html.
- Replaces {% block page_title %} with "Food Management System".
- Replaces {% block content %} with the <h2>Options...</h2> list.
-->
"""