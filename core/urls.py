from django.contrib import admin
from django.urls import path
from scanner import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    path('add-ip/', views.add_single_ip, name='add_single_ip'),
    path('upload/', views.upload_ips, name='upload_ips'),
    path('delete/<int:ip_id>/', views.delete_ip, name='delete_ip'),
    path('delete-multiple/', views.delete_multiple_ips, name='delete_multiple_ips'),
    path('scan-all/', views.scan_all_ips, name='scan_all_ips'),
    path('scan-single/<int:ip_id>/', views.scan_single_ip, name='scan_single_ip'),
    path('export/csv/', views.export_ips_csv, name='export_ips_csv'),
]