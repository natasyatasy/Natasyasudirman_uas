from django.contrib import admin
from django.urls import path, include

##################ini untuk menampilkan gambar yang sudah di upload pada folder media###############
from django.conf import settings
from django.conf.urls.static import static


from myproject.views import home, about, Contact, detail_artikel
from myproject.authentikasi import akun_login, akun_registrasi, akun_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', home, name="home"),
    path('about', about, name="about"),
    path('contact', Contact, name="contact"),
    path('artikel/<slug:slug>',detail_artikel, name="detail_artikel"),
    
    path('dashboard/', include("berita.urls")),


    path('authentikasi/login', akun_login, name="akun_login"),
    path('authentikasi/registrasi', akun_registrasi, name="akun_registrasi"),
    path('authentikasi/logout', akun_logout, name="akun_logout"),

    path('ckeditor/', include('ckeditor_uploader.urls')),

]



##################ini untuk menampilkan gambar yang sudah di upload pada folder media###############
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)