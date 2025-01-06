from django.contrib import admin
from .models import FreeTable

@admin.register(FreeTable)
class FreeTableAdmin(admin.ModelAdmin):
    list_display = ('car_no', 'reason', 'other')  # 列表页显示的字段
    search_fields = ('car_no',)  # 搜索栏字段
    list_filter = ('car_no',) # 过滤器字段
    readonly_fields = ('car_no',) # 只读字段




