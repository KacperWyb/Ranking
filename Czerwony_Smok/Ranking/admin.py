from django.contrib import admin
from django.utils.html import format_html
from .models import Fighter, Payment


class PaymentInline(admin.TabularInline):
    model = Payment
    print(model)


@admin.register(Fighter)
class FighterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'surname', 'club', 'show_url']
    list_filter = ['name', 'surname']
    inlines = [
        PaymentInline
    ]

    def show_url(self, obj):
        if len(obj.name) is not None:
            return format_html(f'<a href="{obj.name}" target=_blank> {obj.name} </a>')
        else:
            return ''

    show_url.short_description = "link"


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'fighter', 'value', 'status']
    list_filter = ['value']
