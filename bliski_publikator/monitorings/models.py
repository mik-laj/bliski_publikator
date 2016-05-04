from autoslug.fields import AutoSlugField
from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from django_bleach.models import BleachField
from model_utils.models import TimeStampedModel
from versatileimagefield.fields import VersatileImageField


class MonitoringQuerySet(models.QuerySet):
    pass


@python_2_unicode_compatible
class Monitoring(TimeStampedModel):
    name = models.CharField(verbose_name=_("Name"), max_length=50)
    slug = AutoSlugField(populate_from='name', verbose_name=_("Slug"), unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    description = BleachField(verbose_name=_("Description"))
    active = models.BooleanField(verbose_name=_("Active status"), default=False)
    logo = VersatileImageField(verbose_name=_("Logo"), null=True, blank=True)
    max_point = models.IntegerField(verbose_name=_("Max point"))
    institutions = models.ManyToManyField(to='institutions.Institution',
                                          verbose_name=_("Institution"),
                                          help_text=_("Specifies which institutions are " +
                                                      "covered by monitoring"),
                                          blank=True)
    objects = MonitoringQuerySet.as_manager()

    class Meta:
        verbose_name = _("Monitoring")
        verbose_name_plural = _("Monitorings")
        ordering = ['active', 'created', ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('monitorings:details', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('monitorings:update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse('monitorings:delete', kwargs={'slug': self.slug})

    def get_assign_url(self):
        return reverse('monitorings:assign', kwargs={'slug': self.slug})

    def get_answer_url(self, institution):
        kwargs = {'slug': self.slug, 'institution_slug': institution.slug}
        return reverse('monitorings:institution_answer', kwargs=kwargs)

    def get_institution_url(self, institution):
        kwargs = {'slug': self.slug, 'institution_slug': institution.slug}
        return reverse('monitorings:institution_detail', kwargs=kwargs)

    @staticmethod
    def get_add_url():
        return reverse('monitorings:create')

MonitoringInstitution = Monitoring.institutions.through
