from . import view
from django.urls import path

urlpatterns = [
    path('', view.getallprojects, name ="projetos"),
    path('', view.getproject, name='projeto')

]