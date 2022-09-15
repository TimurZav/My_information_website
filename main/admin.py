import json
from django import forms
from django.contrib import admin
from django.db import models
from django.forms import widgets
from django.utils.html import format_html
from django.utils.safestring import mark_safe
# from django_admin_json_editor import JSONEditorWidget
from django_json_widget.widgets import JSONEditorWidget
from prettyjson import PrettyJSONWidget
from rest_framework.serializers import ModelSerializer

from .models import Import, Port, ExamplePosts, Line


@admin.register(Import)
class ImportSearch(admin.ModelAdmin):
    list_filter = ('date', 'terminal')
    date_hierarchy = 'date'
    list_editable = [
        'ship',
        'date',
        'terminal',
        'container_number',
        'container_size',
        'container_type',
        'goods_name_rus',
        'consignment',
        'shipper',
        'consignee',
        'line',
        'count',
        'teu',
        'voyage',
        'shipper_country',
        'goods_weight',
        'package_number',
        'city',
        'shipper_seaport',
        'year',
        'month',
        'goods_tnved',
        'parsed_on',
        'month_parsed_on',
        'year_parsed_on'
    ]
    search_fields = ['import_id', 'container_number', 'date', 'parsed_on', 'line', 'terminal']
    list_display = [
        'import_id',
        'ship',
        'date',
        'terminal',
        'container_number',
        'container_size',
        'container_type',
        'goods_name_rus',
        'consignment',
        'shipper',
        'consignee',
        'line',
        'count',
        'teu',
        'voyage',
        'shipper_country',
        'goods_weight',
        'package_number',
        'city',
        'shipper_seaport',
        'year',
        'month',
        'goods_tnved',
        'parsed_on',
        'month_parsed_on',
        'year_parsed_on'
    ]


# @admin.register(Port)
# class PortSearch(admin.ModelAdmin):
#     list_editable = [
#         'image',
#         'url_image',
#         'data_json'
#     ]
#     search_fields = [
#         'id',
#         'image',
#         'url_image',
#         'data_json']
#     list_display = [
#         'id',
#         'image',
#         'url_image',
#         'data_json'
#     ]


DATA_SCHEMA = {
    'type': 'object',
    'title': 'Data'
}


class PrettyJSONWidgetCustom(PrettyJSONWidget):
    def format_value(self, value):
        try:
            value = json.dumps(json.loads(value), indent=4, ensure_ascii=False)
            # these lines will try to adjust size of TextArea to fit to content
            row_lengths = [len(r) for r in value.split('\n')]
            self.attrs['rows'] = min(max(len(row_lengths) + 2, 10), 30)
            self.attrs['cols'] = min(max(max(row_lengths) + 2, 40), 120)
            return value
        except Exception as e:
            return super(PrettyJSONWidget, self).format_value(value)


class JSONModelAdminForm(forms.ModelForm):
    class Meta:
        model = Port
        fields = ('url_image', 'data_json',)
        widgets = {
            'data_json': JSONEditorWidget
        }


@admin.register(Port)
class JSONModelForm(admin.ModelAdmin):
    form = JSONModelAdminForm
    # readonly_fields = ('image_preview',)
    search_fields = ['id', 'image', 'url_image', 'data_json']
    list_editable = ['image', 'url_image', 'data_json']
    list_per_page = 250
    list_display = ['id', 'image', 'url_image', 'data_json']
    
    # def image_preview(self, obj):
    #     return obj.image_preview

    # image_preview.short_description = 'Image Preview'
    # image_preview.allow_tags = True


@admin.register(ExamplePosts)
class ExampleSearch(admin.ModelAdmin):
    list_editable = [
        'name',
        'email',
        'phone',
        'website'
    ]
    search_fields = [
        'name',
        'email',
        'phone',
        'website'
        ]
    list_display = [
        'id',
        'name',
        'email',
        'phone',
        'website'
    ]
    

class JSONModelLineAdminForm(forms.ModelForm):
    class Meta:
        model = Line
        fields = '__all__'
        widgets = {
            'data_json': PrettyJSONWidgetCustom(attrs={'initial': 'parsed'})
        }
        
        
@admin.register(Line)
class LineSearch(admin.ModelAdmin):
    list_editable = [
        'image',
        'url_image',
        'data_json'
    ]
    search_fields = [
        'id',
        'image',
        'url_image',
        'data_json']
    list_display = [
        'id',
        'image',
        'url_image',
        'data_json'
    ]
    form = JSONModelLineAdminForm