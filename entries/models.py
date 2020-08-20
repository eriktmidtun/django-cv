from django.db import models

class CommonModel(models.Model):
    title = models.CharField(max_length=200, null=True)
    visible = models.BooleanField(default=True)
    order_priority = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True
        ordering = ['-order_priority']


class Section(CommonModel):
    class Meta:
        verbose_name = 'Section'

class Entry(CommonModel):
    time = models.CharField(max_length=100)
    place = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    section = models.ForeignKey(Section, on_delete = models.CASCADE)

    class Meta:
        verbose_name = 'Entrie'

class Sidebar(CommonModel):
    class Meta:
        verbose_name = 'Sidebar section'

class Sentry(CommonModel):
    link = models.CharField(max_length=100, null=True, blank=True)
    sidebar_section = models.ForeignKey(Sidebar, on_delete = models.CASCADE)
    space_bottom = models.BooleanField(default=False)
   
    class Meta:
        verbose_name = 'Sidebar entrie'