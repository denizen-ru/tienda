from django.db import models
from django.contrib.contenttypes import generic

from mptt.models import MPTTModel, TreeForeignKey
from eav.models import BaseChoice, BaseEntity, BaseSchema, BaseAttribute


class Category(MPTTModel):
    name = models.CharField(max_length=255, unique=True)
    parent = TreeForeignKey(
        'self', null=True, blank=True, related_name='children')

    def __unicode__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


class Goods(models.Model):
    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Category)

    def __unicode__(self):
        return self.name


class Schema(BaseSchema):
    pass


class Choice(BaseChoice):
    schema = models.ForeignKey(Schema, related_name='choices')


class Attribute(BaseAttribute):
    schema = models.ForeignKey(Schema, related_name='attrs')
    choice = models.ForeignKey(Choice, blank=True, null=True)


class Property(BaseEntity):
    title = models.CharField(max_length=50)
    category = models.ManyToManyField(Category)
    attrs = generic.GenericRelation(Attribute, object_id_field='entity_id',
                                    content_type_field='entity_type')

    @classmethod
    def get_schemata_for_model(self):
        return Schema.objects.all()

    def __unicode__(self):
        return self.title
