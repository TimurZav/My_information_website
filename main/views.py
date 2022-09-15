from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import PortSerializer, LineSerializer
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination
from django.db.models.expressions import RawSQL
import re
from rest_framework.renderers import JSONRenderer
from django_filters.rest_framework import DjangoFilterBackend


def index(request):
    categories = Port.objects.all()
    context = {'categories': categories}
    return render(request, 'main/test.html', context)

    
# class StandardResultsSetPagination(PageNumberPagination):
#     page_query_param = 'page'
#     page_size_query_param = "perPage"


# class CustomOrderFilter(OrderingFilter):
#     ordering_param = "order"
#     sort_param = 'sort'
#     fields_related = {
#         'id': 'id',
#         'url_image': 'url_image',
#         'data_json.file_name': 'data_json.file_name',
#         'data_json.example.text': 'data_json.example.text',
#     }
#     for export in Port.objects.all():
#         len_predicted_box = len(export.data_json)
#         print(len_predicted_box)

#     for len_box in range(len_predicted_box):
#         len_cell = len(export.data_json["predicted_box"][len_box]["cells"])
#         for data_cell in range(len_cell):
#             fields_related[f"data_json.predicted_box.{len_box}.cells.{data_cell}.text"] = f"data_json.predicted_box.{len_box}.cells.{data_cell}.text"
#             fields_related[f"data_json.predicted_box.{len_box}.cells.{data_cell}.validation"] = f"data_json.predicted_box.{len_box}.cells.{data_cell}.validation"

#     # for data_cells in range(len_cells):
#     #     fields_related[f"data_json.predicted_box.1.cells.{data_cells}.text"] = f"data_json.predicted_box.1.cells.{data_cells}.text"

#     # for labels in range(len_labels):
#     #     fields_related[f"data_json.predicted_box.0.cells.{labels}.text"] = f"data_json.predicted_box.0.cells.{labels}.text"
#     #     fields_related[f"data_json.predicted_box.0.cells.{labels}.validation"] = f"data_json.predicted_box.0.cells.{labels}.validation"

#     def get_ordering(self, request, queryset, view):
#         params = request.query_params.get(self.ordering_param)
#         params_sort = request.query_params.get(self.sort_param)
#         if params and params_sort:
#             fields = [param.strip() for param in params.split(',')]
#             fields_sort = [params_sort.strip() for params_sort in params_sort.split(',')]
#             # print(fields_sort)
#             if fields and fields_sort:
#                 return [fields, fields_sort]
#         return self.get_default_ordering(view)

#     def filter_queryset(self, request, queryset, view):
#         order_fields_dict = {}
#         order_fields = []
#         ordering = self.get_ordering(request, queryset, view)
#         try:
#             split_order = ordering[1][0].split('.')
#         except:
#             pass
#         if ordering:
#             symbol = "DESC" if "DESC" in ordering[0] else "ASC"
#             try:
#                 order_fields_dict[self.fields_related[ordering[1][0]]] = symbol

#                 if order_fields_dict[self.fields_related[ordering[1][0]]] == 'DESC':
#                     # print(split_order)
#                     order_fields.append('-' + split_order[-1])
#                 else:
#                     order_fields.append(split_order[-1])
#             except:
#                 if order_fields_dict[self.fields_related[ordering[1][0]]] == 'DESC':
#                     # print(split_order)
#                     # print(self.fields_related[ordering[1][0]])
#                     order_fields.append('-' + self.fields_related[ordering[1][0]])
#                 else:
#                     order_fields.append(self.fields_related[ordering[1][0]])
#         if order_fields:
#             try:
#                 return queryset.order_by(*order_fields)
#             except:
#                 var_sort = split_order[1:]
#                 join_specific_arrow = "'->'".join(var_sort)
#                 splitter = f"{split_order[0]}->'{join_specific_arrow}'"
#                 expression = re.sub("'(\d+)'", r'\1', splitter)
#                 try:
#                     return queryset.annotate(text=RawSQL(expression, [])).order_by(*order_fields)
#                 except:
#                     return queryset.annotate(validation=RawSQL(expression, [])).order_by(*order_fields)

#                 # return queryset.annotate(file_name=RawSQL(f"{split_order[0]}->%s", [var_sort])).order_by(*order_fields)

#         return queryset


# class CustomSearchFilter(SearchFilter):
#     search_param = 'q'


# class PortView(viewsets.ModelViewSet):

#     serializer_class = PortSerializer
#     queryset = Port.objects.all()
#     filter_backends = [CustomSearchFilter, CustomOrderFilter, DjangoFilterBackend]
#     search_fields = ["id", "url_image", "data_json__example__text", "data_json__predicted_box__0__cells__0__text"]
#     filterset_fields = ['id']

#     # for export in ExportReadFromPdf.objects.all():
#     #     len_cells = len(export.data_json["predicted_box"][1]["cells"])

#     # for data_cells in range(len_cells):
#     #     search_fields.append(f"data_json__predicted_box__1__cells__{data_cells}__text")

#     for export in Port.objects.all():
#         len_predicted_box = len(export.data_json["predicted_box"])

#     for len_box in range(len_predicted_box):
#         len_cell = len(export.data_json["predicted_box"][len_box]["cells"])
#         for data_cell in range(len_cell):
#             search_fields.append(f"data_json__predicted_box__{len_box}__cells__{data_cell}__text")

#     pagination_class = StandardResultsSetPagination


# class LineView(viewsets.ModelViewSet):
#     serializer_class = LineSerializer
#     queryset = Line.objects.all()
#     filter_backends = [CustomSearchFilter, CustomOrderFilter, DjangoFilterBackend]
#     search_fields = ["id", "url_image", "data_json__example__text"]
#     filterset_fields = ['id']
#     # for export in ExportReadFromPdfTypeLine.objects.all():
#     #     len_cells = len(export.data_json["predicted_box"][1]["cells"])

#     # for data_cells in range(len_cells):
#     #     search_fields.append(f"data_json__predicted_box__1__cells__{data_cells}__text")

#     # for export in ExportReadFromPdf.objects.all():
#     #     len_cells = len(export.data_json["predicted_box"][1]["cells"])
#     #     len_labels = len(export.data_json["predicted_box"][0]["cells"])

#     # for data_cells in range(len_cells):
#     #     search_fields.append(f"data_json__predicted_box__1__cells__{data_cells}__text")

#     # for labels in range(len_labels):
#     #     search_fields.append(f"data_json__predicted_box__0__cells__{labels}__text")
#     #     search_fields.append(f"data_json__predicted_box__0__cells__{labels}__validation")

#     for export in Line.objects.all():
#         len_predicted_box = len(export.data_json["predicted_box"])

#     for len_box in range(len_predicted_box):
#         len_cell = len(export.data_json["predicted_box"][len_box]["cells"])
#         for data_cell in range(len_cell):
#             search_fields.append(f"data_json__predicted_box__{len_box}__cells__{data_cell}__text")
#             search_fields.append(f"data_json__predicted_box__{len_box}__cells__{data_cell}__validation")

#     pagination_class = StandardResultsSetPagination


class PrettyJsonRenderer(JSONRenderer):    
    def get_indent(self, accepted_media_type, renderer_context):
        return 4
    