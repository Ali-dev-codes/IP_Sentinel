from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import IPAddress
from .utils import scan_ip_details
import io, csv
from django.http import HttpResponse


def dashboard(request):
    all_ips = IPAddress.objects.all().order_by('-last_scan')

    # حساب الإحصائيات للرسم البياني
    low_c = all_ips.filter(severity='low').count()
    med_c = all_ips.filter(severity='medium').count()
    high_c = all_ips.filter(severity='high').count()

    context = {
        'ips': all_ips,
        'total': all_ips.count(),
        'high_risk': high_c,
        'online': all_ips.filter(status='Online').count(),
        'chart_data': [low_c, med_c, high_c],
    }
    return render(request, 'scanner/dashboard.html', context)


def add_single_ip(request):
    if request.method == 'POST':
        ip = request.POST.get('ip_address', '').strip()
        if ip:
            obj, created = IPAddress.objects.get_or_create(address=ip)
            if created: messages.success(request, f'IP {ip} added to queue.')
    return redirect('dashboard')


def upload_ips(request):
    if request.method == 'POST' and request.FILES.get('ip_file'):
        file = request.FILES['ip_file']
        decoded_file = file.read().decode('utf-8')
        io_string = io.StringIO(decoded_file)
        for line in io_string:
            ip = line.strip()
            if ip: IPAddress.objects.get_or_create(address=ip)
        messages.success(request, 'Batch import completed.')
    return redirect('dashboard')


def delete_ip(request, ip_id):
    get_object_or_404(IPAddress, id=ip_id).delete()
    messages.warning(request, 'Asset removed.')
    return redirect('dashboard')


def delete_multiple_ips(request):
    if request.method == 'POST':
        ip_ids = request.POST.getlist('ip_ids')
        if ip_ids:
            IPAddress.objects.filter(id__in=ip_ids).delete()
            messages.warning(request, f'Successfully purged {len(ip_ids)} records.')
    return redirect('dashboard')


def scan_all_ips(request):
    all_ips = IPAddress.objects.all()
    for ip in all_ips:
        scan_ip_details(ip.id)
    messages.success(request, 'Global intelligence scan finished.')
    return redirect('dashboard')


def scan_single_ip(request, ip_id):
    scan_ip_details(ip_id)
    messages.success(request, "Targeted scan completed.")
    return redirect('dashboard')


def export_ips_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Sentinel_Threat_Log.csv"'
    writer = csv.writer(response)
    writer.writerow(['IP', 'Country', 'Status', 'Abuse Score', 'Severity'])
    for ip in IPAddress.objects.all():
        writer.writerow([ip.address, ip.country, ip.status, f"{ip.reputation_score}%", ip.severity])
    return response