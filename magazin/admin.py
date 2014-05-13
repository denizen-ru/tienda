from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from django.utils import simplejson
from eav.admin import BaseEntityAdmin, BaseSchemaAdmin

from models import Category, Goods, Schema, Choice
from forms import GoodsForm
import sys

class CategoryAdmin(DjangoMpttAdmin):
    pass


class GoodsAdmin(BaseEntityAdmin):
    form = GoodsForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            ids = [x.id for x in Category.objects.first().get_leafnodes()]
            kwargs['queryset'] = Category.objects.filter(id__in=ids)
        return super(GoodsAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def render_change_form(self, request, context, **kwargs):
        # context['itswork'] = simplejson.dumps(Category.objects.all())
        categories = {}
        for category in Category.objects.all():
            categories[category.id] = [x.name for x in Schema.objects.filter(category=category.id)]
        print >> sys.stderr, categories
        context['categories'] = simplejson.dumps(categories)
        return super(GoodsAdmin, self).render_change_form(request, context, **kwargs)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Schema, BaseSchemaAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Choice)
