from django.db import models

class CommonModel(models.Model):
    title = models.CharField(max_length=200, null=True)
    visible = models.BooleanField(default=True)
    order_priority = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True

class Section(CommonModel):
    class Meta:
        verbose_name = 'Section'
        ordering = ['-order_priority']

class Entry(CommonModel):
    time = models.CharField(max_length=100)
    place = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    section = models.ForeignKey(Section, on_delete = models.CASCADE, related_name='entries')

    class Meta:
        verbose_name = 'Entrie'
        ordering = ['-order_priority']

class Sidebar(CommonModel):
    class Meta:
        verbose_name = 'Sidebar section'
        ordering = ['-order_priority']

class Sentry(CommonModel):
    link = models.CharField(max_length=100, null=True, blank=True)
    sidebar_section = models.ForeignKey(Sidebar, on_delete = models.CASCADE, related_name='sidebar_entries')
    space_bottom = models.BooleanField(default=False)
   
    class Meta:
        verbose_name = 'Sidebar entrie'
        ordering = ['-order_priority']