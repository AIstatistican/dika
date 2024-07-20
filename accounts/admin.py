

# Register your models here.
# admin.py

from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display=['inputName', 'inputSurname']
    list_display_links=['inputName']
    list_filter=['inputName']
    search_fields=['inputName','inputUsername']
    list_editable=['inputSurname'] # ama buraya yazdığın birşey display_links de olmamalı
    class Meta:
        model=Contact




admin.site.register(Contact,ContactAdmin)
