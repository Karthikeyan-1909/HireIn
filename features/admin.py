from django.contrib import admin
from features.models import Jobs, UpdateProfile, Resume, Blog, Contact, Apply

# Register your models here.
admin.site.register(Jobs)
admin.site.register(UpdateProfile)
admin.site.register(Resume)
admin.site.register(Blog)
admin.site.register(Contact)
admin.site.register(Apply)