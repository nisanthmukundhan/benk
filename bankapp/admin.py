from django.contrib import admin

# Register your models here.
from bankapp.models import District, Branch, Register, Account, Materials


class DistrictAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug': ('name',)}



admin.site.register(District, DistrictAdmin)


class BranchAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug': ('name',)}



admin.site.register(Branch, BranchAdmin)


class RegisterAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Register, RegisterAdmin)


class AccountAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']

    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Account, AccountAdmin)


class MaterialsAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']

    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Materials, MaterialsAdmin)
