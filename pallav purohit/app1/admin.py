from django.contrib import admin
from.models import Employee
from.models import image
from.models import Zomato
from.models import zoamto
from import_export.admin import ImportExportModelAdmin


admin.site.register(Employee)
admin.site.register(image)
##old
@admin.register(Zomato)
class ZomatoAdmin(ImportExportModelAdmin):
    pass
@admin.register(zoamto)
class zoamtoAdmin(ImportExportModelAdmin):
    pass

