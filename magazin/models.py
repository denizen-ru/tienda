from django.db import models
from django.contrib.contenttypes import generic
from django.core.urlresolvers import reverse

from mptt.models import MPTTModel, TreeForeignKey
from eav.models import BaseEntity, BaseSchema, BaseAttribute, BaseChoice


class Category(MPTTModel):
    name = models.CharField(max_length=255, unique=True)
    parent = TreeForeignKey(
        'self', null=True, blank=True, related_name='children')

    def __unicode__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


class Schema(BaseSchema):
    category = models.ManyToManyField(Category, related_name='category')


class Choice(BaseChoice):
    schema = models.ForeignKey(Schema, related_name='choices')


class Attribute(BaseAttribute):
    schema = models.ForeignKey(Schema, related_name='attrs')
    choice = models.ForeignKey(Choice, blank=True, null=True)


class Goods(BaseEntity):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category)
    receipt_date = models.DateTimeField('date of receipt')
    attrs = generic.GenericRelation(Attribute, object_id_field='entity_id',
                                    content_type_field='entity_type')

    def __unicode__(self):
        return self.name

    @classmethod
    def get_schemata_for_model(cls):
        return Schema.objects.all()

    def get_schemata_for_instance(self, qs):
        if hasattr(self, 'category'):
            return qs.filter(category=self.category)
        return qs
