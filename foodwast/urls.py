"""foodwast URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url

from food import views as food_views

urlpatterns = [
    url('admin/', admin.site.urls),

    url(r'^$', food_views.index, name='index' ),

    url(r'^about/$', food_views.about, name='about' ),
 
    url(r'^donate/$',food_views.donate,name='donate'),

    url(r'^admin1/$',food_views.admin1,name='admin1'),

    url(r'^agent/$',food_views.agent,name='agent'),

    url(r'^contact/$',food_views.contact,name='contact'),

    url(r'^AdminHome/$',food_views.AdminHome,name='AdminHome'),

    url(r'^AgentHome/$',food_views.AgentHome,name='AgentHome'),

    url(r'^AddAgent/$',food_views.AddAgent,name='AddAgent'),

    url(r'^ViewADonars/$',food_views.ViewADonars,name='ViewADonars'),


    url(r'^donatesuccess/$',food_views.donatesuccess,name='donatesuccess'),

    url(r'^ViewAgent/$',food_views.ViewAgent,name='ViewAgent'),

    url(r'^updateagent/(?P<a_id>\w+)',food_views.update_agent),

    url(r'^deleteagent/(?P<a_id>\w+)',food_views.delete_agent),

    
    url(r'^ViewSDonars/(?P<c_id>\w+)',food_views.ViewSDonars),


    url(r'^ViewDonars/$',food_views.ViewDonars,name='ViewDonars'),
    
    url(r'^AssignDonars/$',food_views.AssignDonars,name='AssignDonars'),
   
    url(r'^ViewAssignAgents/$',food_views.ViewAssignAgents,name='ViewAssignAgents'),

    
]
