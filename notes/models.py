from django.db import models

class Notebook(models.Model):
    name = models.CharField(max_length=200)

class Section(models.Model):
    notebook = models.ForeignKey(Notebook, on_delete=models.CASCADE, related_name="sections")
    name = models.CharField(max_length=200)

class Page(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="pages")
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
