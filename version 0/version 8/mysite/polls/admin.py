from django.contrib import admin
from polls.models import My_car
# Register your models here.
@admin.register(My_car)
class Mycar_admin(admin.ModelAdmin):
    list_display = ['id','name','player_ID','Number_of_brakes']