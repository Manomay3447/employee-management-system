"""
URL configuration for employee_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('insert',views.insert, name = 'insert'),
    path('deleteemp/<int:vid>',views.deleteemp, name = 'deleteemp'),
    path('deleteempos/<int:vid>',views.deleteempos, name = 'deleteempos'),
    path('deleteempwfh/<int:vid>',views.deleteempwfh, name = 'deleteempwfh'),
    path('deletedepartment/<int:vid>',views.deletedepartment, name = 'deletedepartment'),
    path('deleteproject/<int:vid>',views.deleteproject, name = 'deleteproject'),
    path('deletetakes/<int:vid>',views.deletetakes, name = 'deletetakes'),
    path('deleteleave/<int:vid>',views.deleteleave, name = 'deleteleave'),
    path('editemp/<int:vid>',views.editemp, name = 'editemp'),
    path('updateemp/<int:vid>',views.updateemp, name = 'updateemp'),
    path('editempos/<int:vid>',views.editempos, name = 'editempos'),
    path('updateempos/<int:vid>',views.updateempos, name = 'updateempos'),
    path('editempwfh/<int:vid>',views.editempwfh, name = 'editempwfh'),
    path('updateempwfh/<int:vid>',views.updateempwfh, name = 'updateempwfh'),
    path('editdepartment/<int:vid>',views.editdepartment, name = 'editdepartment'),
    path('updatedepartment/<int:vid>',views.updatedepartment, name = 'updatedepartment'),
    path('editproject/<int:vid>',views.editproject, name = 'editproject'),
    path('updateproject/<int:vid>',views.updateproject, name = 'updateproject'),
    path('edittakes/<int:vid>',views.edittakes, name = 'edittakes'),
    path('updatetakes/<int:vid>',views.updatetakes, name = 'updatetakes'),
    path('editleave/<int:vid>',views.editleave, name = 'editleave'),
    path('updateleave/<int:vid>',views.updateleave, name = 'updateleave'),
    path('modify',views.modify, name = 'modify'),
    path('modifyemp',views.modifyemp, name = 'modifyemp'),
    path('modifyempwfh',views.modifyempwfh, name = 'modifyempwfh'),
    path('modifyempos',views.modifyempos, name = 'modifyempos'),
    path('modifydepartment',views.modifydepartment, name = 'modifydepartment'),
    path('modifyproject',views.modifyproject, name = 'modifyproject'),
    path('modifyleave',views.modifyleave, name = 'modifyleave'),
    path('modifytakes',views.modifytakes, name = 'modifytakes'),
    path('view',views.view, name = 'view'),
    path('viewemp',views.viewemp, name = 'viewemp'),
    path('viewempos',views.viewempos, name = 'viewempos'),
    path('viewempwfh',views.viewempwfh, name = 'viewempwfh'),
    path('viewdepartment',views.viewdepartment, name = 'viewdepartment'),
    path('viewproject',views.viewproject, name = 'viewproject'),
    path('viewtakes',views.viewtakes, name = 'viewtakes'),
    path('viewleave',views.viewleave, name = 'viewleave'),
    path('empsalary',views.empsalary, name = 'empsalary'),
    path('insertemployee',views.insertemployee, name = 'insertemployee'),
    path('insertempos',views.insertempos, name = 'insertempos'),
    path('insertempwfh',views.insertempwfh, name = 'insertempwfh'),
    path('insertdept',views.insertdept, name = 'insertdept'),
    path('insertleave',views.insertleave, name = 'insertleave'),
    path('insertproject',views.insertproject, name = 'insertproject'),
    path('inserttakes',views.inserttakes, name = 'inserttakes'),
    path('insertinempos',views.insertinempos, name = 'insertinempos'),
    path('insertinempwfh',views.insertinempwfh, name = 'insertinempwfh'),
    path('insertindept',views.insertindept, name = 'insertindept'),
    path('insertinproject',views.insertinproject, name = 'insertinproject'),
    path('insertemp',views.insertemp, name = 'insertemp'),
    path('insertintakes',views.insertintakes, name = 'insertintakes'),
    path('insertinleave',views.insertinleave, name = 'insertinleave'),
]
