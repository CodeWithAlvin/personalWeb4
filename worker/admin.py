from django.contrib import admin
from worker.models import Blog,Project,Review
# Register your models here.
admin.site.register(Blog)
admin.site.register(Project)
admin.site.register(Review)