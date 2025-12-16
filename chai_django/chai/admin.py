from django.contrib import admin
from .models import chai_menu, chai_stores, chai_Certificate, chai_Review, store


class ChaiReviewInline(admin.TabularInline):
    model = chai_Review
    extra = 2

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'price')
    inlines = [ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varities',)

class ChaiStoresAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'distance')

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'cerificate_no')




admin.site.register(chai_menu, ChaiVarietyAdmin)
admin.site.register(chai_stores, ChaiStoresAdmin)
admin.site.register(store, StoreAdmin)
# admin.site.register(chai_Review,ChaiReviewInline)
admin.site.register(chai_Certificate, ChaiCertificateAdmin)
# Register your models here.


