from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from django.db.models.query import QuerySet
from eav.admin import BaseEntityAdmin, BaseSchemaAdmin

from models import Category, Goods, Property, Schema, Choice
from forms import PropertyForm


class CategoryAdmin(DjangoMpttAdmin):
    pass


class PropertyAdmin(BaseEntityAdmin):
    form = PropertyForm


class GoodsAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            bad_ids = [
                x.id for x in Category.objects.all() if x.get_descendant_count() != 0]
            kwargs['queryset'] = Category.objects.exclude(id__in=bad_ids)
        return super(GoodsAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Property, PropertyAdmin)
admin.site.register(Schema, BaseSchemaAdmin)
admin.site.register(Choice)
admin.site.register(Goods, GoodsAdmin)
