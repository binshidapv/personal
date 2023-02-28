from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import RedirectView

from .import views

urlpatterns = [
     path("home/",views.HomeView,name="port-home"),
     path("about/",views.AboutView,name="port-about"),
     path("skill/", views.SkillView, name="port-skills"),
     path("project/",views.ProjectsView,name="port-projects"),
     path('details/<int:pk>/', views.ProjectDetailView, name="port-projectdetails"),
     path("contact/",views.ContactsView,name="port-contact"),


]