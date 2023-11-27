import groups as groups
from django.contrib import admin
from . import models
from .models import *


@admin.register(Instruction)
class InstructionAdmin(admin.ModelAdmin):
    #filter_horizontal = ('steps',)
    list_display = ('name', 'id')

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('position', 'id')


admin.site.register(PublicHoliday)
admin.site.register(StepForInstruction)

