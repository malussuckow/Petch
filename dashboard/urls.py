from django.urls import path
from dashboard import views

urlpatterns = [
    path('tutor/',views.dashboardTutor,name='dashboardTutor'),
    path("ong/",views.dashboardOng, name="dashboardOng")
]