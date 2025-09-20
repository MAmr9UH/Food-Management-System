from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse ,HttpResponseNotFound, HttpResponseRedirect
# Create your views here.
from django.urls import reverse 
from django.http import HttpResponseNotFound
#from django.template.loader import render_to_string

from .models import Inventory 


def Inventory_view(request):   # don’t use `Inventory` as a function name; it conflicts with your model
    items = Inventory.objects.all()
    return render(request, "welcome/Inventory_.html", {
        "itemsx": items
    })
# Item x Is FOR THE TEMPLATE AND THE items IS FOR THE python variable 

def add_Inventory(request):
    if request.method == "POST":
        name = request.POST.get("name")
        location = request.POST.get("location")
        current_quantity = request.POST.get("current_quantity")
        min_level = request.POST.get("min_level")
        expiry_date = request.POST.get("expiry_date")
        status = request.POST.get("status")
        price = request.POST.get("price")

        Inventory.objects.create(
            name=name,
            location=location,
            Current_Quantity=current_quantity,
            min_Level=min_level,
            expiry_date=expiry_date or None,
            status=status,
            Price=price
        )
        return redirect("Inventory")  # <- make sure your URL name matches
    
    return render(request, "welcome/add_Inventory.html")





def edit_inventory(request, pk):
    item = get_object_or_404(Inventory, pk=pk)   # ✅ fetch or return 404

    if request.method == "POST":
        item.name = request.POST.get("name")
        item.location = request.POST.get("location")
        item.Current_Quantity = request.POST.get("current_quantity")
        item.Price = request.POST.get("price")
        item.status = request.POST.get("status")
        item.save()
        return redirect("Inventory")

    return render(request, "welcome/edit_inventory.html", {"item": item})









def options(request):
    lists = ["demo", "contact"]
    return render(request, "welcome/welcome.html", {
        "options": lists  # must match template name
    }

    )



def demo(request):
    # You’ll implement later
    #return HttpResponse("Demo Page (to be implemented)")
    items = Inventory.objects.all()
    return render(request, "welcome/index.html", {
        "itemsx": items
    })

    #return render(request, "welcome/index.html", {
     # }
      
      
     # )

#def Inventory_page(request):
    # You’ll implement later
    #return HttpResponse("Demo Page (to be implemented)")
 #   return render(request, "welcome/Inventory_.html", {
  #    })
    




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