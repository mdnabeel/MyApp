from django.contrib import admin
from .models import Customer, Status

# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age',
                    'acc_status', 'date_of_deactivation')


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Status)
