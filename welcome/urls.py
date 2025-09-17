#month_challanges/challanges/views.py
from . import views



from django.urls import path 
urlpatterns=[

path("" ,views.options, name="index") #challenges
,
path("demo", views.demo, name="demo"),
path("contact/<str:contactu>", views.contact, name="contact"),  
#path("contact-info/<str:contactu>",views.contact_info ,name="contact-info")

]


#str:  indetifier 



