from django.urls import path
from . import views

app_name = "mainapp"

urlpatterns = [
    path("", views.index_view, name="index"),
    path("graph1/", views.graph1_view, name="graph1"),
    path("graph2/", views.graph2_view, name="graph2"),
    path("graph3/", views.graph3_view, name="graph3"),
    path("graph4/", views.graph4_view, name="graph4"),
    path("graph5/", views.graph5_view, name="graph5"),
    path("graph6/", views.graph6_view, name="graph6"),
    path("graph7/", views.graph7_view, name="graph7"),
    path("graph8/", views.graph8_view, name="graph8"),
    path("graph9/", views.graph9_view, name="graph9"),
    path("graph10/", views.graph10_view, name="graph10"),
    path("graph11/", views.graph11_view, name="graph11"),
    path("graph12/", views.graph12_view, name="graph12"),
]