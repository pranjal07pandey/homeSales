from django.contrib import admin
from .models import *


class Display(admin.ModelAdmin):
    list_display = ('fname', 'house_sold', 'joined_date')
    list_filter = ('house_sold',)
# Register your models here.
admin.site.register(Agent, Display)
admin.site.register(Home)
admin.site.register(Contact)


admin.site.site_header = "Home Sales"