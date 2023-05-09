import os
from django.contrib import admin
from .models import User
from django.utils.safestring import mark_safe
from django.conf import settings


# Register your models here.
class MyModelAdmin(admin.ModelAdmin):

    def pull_credit_report(self, obj):
        base_path = settings.MEDIA_URL
        url = os.path.join(base_path, 'sample.pdf')
        return mark_safe(f'<input type="button" id="pull_button" onclick="showPdf(\'{url}\')" value="Pull credit report" data-value="{url}">' f'<iframe id="pdfViewer" style="display: none;margin-top: 10px;height: 300px;width: 500px;"></iframe>')

    pull_credit_report.short_description = 'Pull credit report'

    class Media:
        js = ('admin/js/myapp.js', )

    list_display = (
        'first_name',
        'last_name',
        'email',
        'password',
        'is_active',
        'is_staff',
        'is_admin',
        'country',
        'state',
        'city',
        'pull_credit_report',
    )
    readonly_fields = (
        'pull_credit_report',
    )


admin.site.register(User, MyModelAdmin)
