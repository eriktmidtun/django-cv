from django.db import models

class Section(models.Model):
    section_title = models.CharField(max_length=100)

    def __str__(self):
        return self.section_title

class Entry(models.Model):
    time = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    place = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    section = models.ForeignKey(Section, on_delete = models.CASCADE)

    def __str__(self):
        return self.title
