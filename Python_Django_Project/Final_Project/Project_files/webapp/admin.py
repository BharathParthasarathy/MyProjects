from django.contrib import admin

# Register your models here.

from . models import employee_record,payroll_table,time_off_table,schedule_table,timing_table,Events

admin.site.register(employee_record)
admin.site.register(payroll_table)

admin.site.register(time_off_table)

admin.site.register(schedule_table)

admin.site.register(timing_table)

admin.site.register(Events)





