from django.contrib import admin
from django.utils.html import format_html
from .models import IPAddress
from .utils import scan_ip_details


@admin.register(IPAddress)
class IPAddressAdmin(admin.ModelAdmin):
    list_display = ('address', 'country', 'reputation_score', 'colored_severity', 'status', 'last_scan')

    list_filter = ('severity', 'status', 'country')

    # إضافة خانة بحث بالعنوان
    search_fields = ('address', 'country')

    actions = ['run_full_scan']

    @admin.action(description='Run Comprehensive SOC Scan')
    def run_full_scan(self, request, queryset):
        count = queryset.count()
        for ip_obj in queryset:
            scan_ip_details(ip_obj.id)

        self.message_user(request, f"Successfully scanned {count} IP addresses and updated database.")

    def colored_severity(self, obj):
        colors = {
            'high': 'red',
            'medium': 'orange',
            'low': 'green',
        }
        return format_html(
            '<b style="color:{}; text-transform:uppercase;">{}</b>',
            colors.get(obj.severity, 'black'),
            obj.severity
        )

    colored_severity.short_description = 'Severity Level'


admin.site.site_header = "IP Sentinel Security Portal"
admin.site.site_title = "IP Sentinel Admin"
admin.site.index_title = "Welcome to SOC Analysis Dashboard"