import imp
from django.urls import path

from . import views
from .views import items,item,addItem,deleteRow
app_name='fetcher'
urlpatterns = [
    path('items', items,name='items'),
    path('item/<int:row>', item,name='item'),
    path('add_item', addItem,name='add_item'),
    path('delete_row/<int:rowId>', deleteRow,name='delete_row'),

]