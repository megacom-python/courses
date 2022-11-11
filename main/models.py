from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Course(models.Model):
    title = models.CharField(_("title"), max_length=50)
    # contact_set
    # branch_set
    class Meta:
        verbose_name = _("course")
        verbose_name_plural = _("courses")

    def __str__(self):
        return self.title


class Branch(models.Model):
    course = models.ForeignKey(
        "main.Course",
        verbose_name=_("course"),
        on_delete=models.CASCADE,
        related_name="branches",
    )
    title = models.CharField(_("title"), max_length=50)
    latitude = models.DecimalField(
        _("latitude"), max_digits=7, decimal_places=2
    )
    longitude = models.DecimalField(
        _("longitude"), max_digits=7, decimal_places=2
    )
    address = models.CharField(_("address"), max_length=255)

    class Meta:
        verbose_name = _("branch")
        verbose_name_plural = _("branchs")

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(_("title"), max_length=50)

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categorys")

    def __str__(self):
        return self.title


class Contact(models.Model):
    category = models.ForeignKey(
        "main.Category", verbose_name=_("category"), on_delete=models.CASCADE
    )
    course = models.ForeignKey(
        "main.Course",
        verbose_name=_("course"),
        on_delete=models.CASCADE,
        related_name="contacts",
    )
    value = models.CharField(_("value"), max_length=50)

    class Meta:
        verbose_name = _("contact")
        verbose_name_plural = _("contacts")
