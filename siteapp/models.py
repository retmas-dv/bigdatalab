# -*- coding: cp1251 -*-
from django.db import models


class Setting(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name=u"���")
    value = models.TextField(verbose_name=u"��������", blank=True)

    @staticmethod
    def get(name, default=None):
        try:
            return Setting.objects.get(name=name).value
        except Setting.DoesNotExist:
            return default

    class Meta:
        verbose_name_plural = u"��������� �����"


class Link(models.Model):
    url = models.CharField(max_length=2048, unique=True, verbose_name=u"������")
    page_template_name = models.CharField(max_length=128, null=True, blank=True, verbose_name=u"��� ����� ��������")
    page_name = models.CharField(max_length=128, null=True, blank=True, verbose_name=u"��� ��������")

    def save(self):
        if self.page_template_name:
            if self.url[0] != '/':
                self.url = "/%s" % self.url
            if self.url[-1] != '/':
                self.url = "%s/" % self.url
            self.url = "/pages%s" % self.url
        super(Link, self).save()

    class Meta:
        verbose_name_plural = u"������"

    def __unicode__(self):
        return self.url


class MenuItem(models.Model):
    parent = models.ForeignKey("self", blank=True, null=True)
    position = models.SmallIntegerField(verbose_name=u"������� ������ ����")
    name = models.CharField(max_length=50, verbose_name=u"�������� ������ ����")
    link = models.ForeignKey(Link, blank=True, null=True, verbose_name=u"������")

    class Meta:
        verbose_name_plural = u"���� �����"

    def __unicode__(self):
        return self.name
