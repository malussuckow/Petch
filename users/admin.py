from django.contrib import admin
from users.models import User,TutorProfile,OngProfile,TutorPreferences

admin.site.register(User)
admin.site.register(TutorProfile)
admin.site.register(OngProfile)
admin.site.register(TutorPreferences)
