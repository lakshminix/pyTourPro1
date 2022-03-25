from.import views
from django.urls import path

urlpatterns = [

    # path('',views.home,name='home'),
    # path('about/',views.about,name='about'),
    # path('contact',views.contact,name='contact'),
    # path('detail',views.detail,name='detail'),
    # path('thankyou',views.thankyou,name='thankyou')

    # path('',views.integer,name='demo'),
    # path('operation/',views.operation,name='operation')

    path('',views.demo,name='demo')

]
