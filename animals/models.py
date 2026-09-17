from django.db import models
from users.models import TutorProfile
from users.models import OngProfile


class RegisterAnimals(models.Model):
    AGE=[
        ("PUPPY","Filhote"),
        ("ADULT","Adulto"),
        ("SENIOR","Idoso")
]
    SIZE=[
        ("LARGE","Grande"),
        ("SMALL","Pequeno")
]
    GENDER=[
        ("MALE","Macho"),
        ("FEMALE","Fêmea")
]
    SPECIE=[
        ("DOG","Cachorro"),
        ("CAT","Gato"),
        ("RABBIT","Coelho"),
        ("OTHER","Outro")
    ]
    TEMPERAMENT=[
        ("CALM","Calmo"),
        ("PLAYFUL","Brincalhão"),
        ("ACTIVE","Ativo"),
        ("SHY","Tímido")
]

    ANIMAL_STATUS=[
        ("AVAILABLE","Disponível"),
        ("RESERVED","Reservado"),
        ("ADOPTED","Adotado")
]
    name= models.CharField(max_length=50)
    age=models.CharField(max_length=15 , choices=AGE)
    size = models.CharField(max_length=15,choices=SIZE)
    breed = models.CharField(max_length=30)
    gender= models.CharField(max_length=15,choices=GENDER)
    color = models.CharField(max_length=20)
    specie=models.CharField(max_length=15,choices=SPECIE)
    temperament=models.CharField(max_length=15,choices=TEMPERAMENT)
    good_with_children=models.BooleanField(default=False)
    good_with_dogs=models.BooleanField(default=False)
    good_with_cats=models.BooleanField(default=False)
    neutered=models.BooleanField(default=False)
    vaccinated=models.BooleanField(default=False)
    animal_photo = models.ImageField(upload_to="usuarios/",blank=True, null=True)
    ong=models.ForeignKey(OngProfile,on_delete=models.CASCADE)
    status=models.CharField(max_length=15,choices=ANIMAL_STATUS,default="AVAILABLE")

    def __str__(self):
        return self.name

##############################################################################

class Adoption(models.Model):
    STATUS_CHOICES=[
        ("IN_PROGRESS","Em andamento"),
        ("COMPLETED","Concluída"),
        ("RETURNED","Devolvido")
]

    date_adoption = models.DateTimeField(auto_now_add=True)
    status= models.CharField(max_length=15,choices=STATUS_CHOICES,default="IN_CHOICES")
    date_devolution=models.DateField(null=True,blank=True)
    animal=models.ForeignKey(RegisterAnimals,on_delete=models.CASCADE)
    tutor=models.ForeignKey(TutorProfile,on_delete=models.CASCADE)

    def __str__(self):
        return F" Status da adoção: {self.status}"

##########################################################################

class Favorite(models.Model):
    
    animal=models.ForeignKey(RegisterAnimals,on_delete=models.CASCADE)
    tutor=models.ForeignKey(TutorProfile,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ['animal', 'tutor']

    def __str__(self):
        return f"{self.animal.name}"


