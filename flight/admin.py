from django.contrib import admin

from .models import *

admin.AdminSite.site_title = "Admin"
admin.AdminSite.site_header = "Airline MS DBMS Project G2-2"
admin.AdminSite.index_title = "Airline MS"
# Register your models here.

admin.site.register(Place)
admin.site.register(Week)
admin.site.register(Flight)
admin.site.register(Passenger)
admin.site.register(User)
admin.site.register(Ticket)