from django.contrib import admin

# Register your models here.
from testapp.models import scan_data,Company_Info,Device_Details,print_data


admin.site.register(scan_data)
admin.site.register(Company_Info)
admin.site.register(Device_Details)
admin.site.register(print_data)
