from django.contrib import admin
from .models import IPAddress
from .utils import scan_ip_details

@admin.register(IPAddress)
class IPAddressAdmin(admin.ModelAdmin):
    # الأعمدة التي ستظهر في الجدول
    list_display = ('address', 'status', 'reputation_score', 'severity', 'last_scan')
    # إضافة الزر (Action)
    actions = ['run_full_scan']

    @admin.action(description='تشغيل فحص الأتمتة الشامل (SOC Scan)')
    def run_full_scan(self, request, queryset):
        for ip_obj in queryset:
            scan_ip_details(ip_obj.id)
        self.message_user(request, "تم اكتمال الفحص وتحديث قاعدة البيانات!")