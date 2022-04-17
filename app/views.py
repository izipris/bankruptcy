from django.shortcuts import render, HttpResponse
from .services.CrawlingService import *
import csv


# Create your views here.
def crawl(request):
    if request.method == 'POST' and request.POST is not None:
        data = request.POST.get("id_list", "").split("\r\n")
        response = HttpResponse(
            content_type='text/csv',
            headers={'Content-Disposition': 'attachment; filename="somefilename.csv"'},
        )
        generate_csv(response, get_bankrupts(data))
        return response
    return render(request, 'crawl.html')


def generate_csv(path, bankrupts):
    writer = csv.writer(path)
    writer.writerow(['סוג', 'ת.ז. / ח.פ', 'מספר תיק בכנ"ר', 'סיבת ביטול הצו', 'סטטוס התיק', 'רשות מטפלת',
                     'תאריך ביטול הצו כינוס/פש"ר', 'תאריך צו פשיטת רגל', 'תאריך צו כינוס', 'תאריך צו פירוק',
                     'תאריך ביטול\חיסול\עיכוב הצו'])
    for bankrupt in bankrupts:
            writer.writerow([bankrupt.get_type(), bankrupt.get_id(), bankrupt.get_case_id(), bankrupt.get_cancel_reason(),
                         bankrupt.get_case_status(), bankrupt.get_authority(), bankrupt.get_cancel_date(),
                         bankrupt.get_bankruptcy_date(), bankrupt.get_concentration_date(),
                         bankrupt.get_destruction_date(), bankrupt.get_delay_date()])
    return writer
