from django.contrib import admin

# Register your models here.
from index.models import *

admin.site.register(GoodsType)

class GoodsAdmin(admin.ModelAdmin):
    list_filter = ('goodsType',)
    search_fields = ('title',)

admin.site.register(Users)
admin.site.register(Goods,GoodsAdmin)
admin.site.register(CartInfo)