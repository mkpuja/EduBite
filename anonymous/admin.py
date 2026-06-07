from django.contrib import admin
from .models import Register, Food, Cart, Order


admin.site.register(Register)
admin.site.register(Food)
admin.site.register(Cart)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'food',
        'quantity',
        'total_price',
        'status'
    )

    list_editable = (
        'status',
    )