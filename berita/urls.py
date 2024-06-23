from django.urls import path 
from berita.views import (
    dashboard, 
    Kategori_list, kategori_add, kategori_update, kategori_delete,
    artikel_list, artikel_add, artikel_detail, artikel_update, artikel_delate
    )

urlpatterns = [    
    path('', dashboard, name="dashboard"),
    path('Kategori/list', Kategori_list, name="Kategori_list"),
    path('kategori/add', kategori_add, name="kategori_add"),
    path('kategori/update/<int:id_kategori>', kategori_update, name="kategori_update"),
    path('kategori/delete/<int:id_kategori>', kategori_delete, name="kategori_delete"),

    path('artikel/list', artikel_list, name="artikel_list"),
    path('artikel/add', artikel_add, name="artikel_add"),
    path('artikel/detail/<int:id_artikel>', artikel_detail, name="artikel_detail"),
    path('artikel/update/<int:id_artikel>', artikel_update, name="artikel_update"),
    path('artikel/delate/<int:id_artikel>', artikel_delate, name="artikel_delate"),
]
