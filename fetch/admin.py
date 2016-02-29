from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *

admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Trainer)
admin.site.register(Intent)

class TrainerInline(admin.StackedInline):
    model = Trainer
    can_delete = False
    verbose_name_plural = 'trainers'

class UserAdmin(BaseUserAdmin):
    inlines = (TrainerInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)