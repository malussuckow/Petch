from django.contrib import admin
from animals.models import RegisterAnimals,Adoption,Favorite

admin.site.register(RegisterAnimals)
admin.site.register(Adoption)
admin.site.register(Favorite)
