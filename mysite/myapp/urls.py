from django.urls import path
from . import views
app_name = 'myapp'
urlpatterns = [
    path("", views.index, name='home'),
    path("details/<int:my_id>", views.index_item, name='item'),           #не сделано
]

