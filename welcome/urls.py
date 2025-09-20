#month_challanges/challanges/views.py
from . import views



from django.urls import path 
urlpatterns=[

path("" ,views.options, name="index") #challenges
,
path("demo", views.demo, name="demo"),
path("Inventory_/", views.Inventory_view, name="Inventory"),
path("contact/<str:contactu>", views.contact, name="contact"),  
path("add_Inventory", views.add_Inventory, name="add_Inventory"),  
path("Inventory/<int:pk>/edit/", views.edit_inventory, name="edit_inventory"),


#path("contact-info/<str:contactu>",views.contact_info ,name="contact-info")

]


#str:  indetifier 



