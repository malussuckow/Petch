from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    TYPE_CHOICES=[
        ("TUTOR","tutor"),
        ("ONG","ong")
    ]
    STATES = [
        ("AC", "Acre"),("AL", "Alagoas"),("AP", "Amapá"),
        ("AM", "Amazonas"),("BA", "Bahia"),("CE", "Ceará"),
        ("DF", "Distrito Federal"),("ES", "Espírito Santo"),("GO", "Goiás"),
        ("MA", "Maranhão"),("MT", "Mato Grosso"),("MS", "Mato Grosso do Sul"),
        ("MG", "Minas Gerais"),("PA", "Pará"),("PB", "Paraíba"),
        ("PR", "Paraná"),("PE", "Pernambuco"),("PI", "Piauí"),
        ("RJ", "Rio de Janeiro"),("RN", "Rio Grande do Norte"),("RS", "Rio Grande do Sul"),
        ("RO", "Rondônia"),("RR", "Roraima"),("SC", "Santa Catarina"),
        ("SP", "São Paulo"),("SE", "Sergipe"),("TO", "Tocantins"),
    ]
    user_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=2, choices=STATES)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    profile_photo = models.ImageField(upload_to="users/", blank=True, null=True)
    cep = models.CharField(max_length=9)
    street = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    complement = models.CharField(max_length=100, null=True, blank=True)
    neighborhood = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

##################################################################


class TutorProfile(models.Model):

    HOUSING_TYPE = [
        ("HOUSE", "Casa"),
        ("APARTMENT", "Apartamento"),
        ("FARM", "Sítio"),
        ("OTHER" ,"outro"),
    ]
    housing_type = models.CharField(max_length=10, choices=HOUSING_TYPE)
    birth_date = models.DateField()
    has_backyard = models.BooleanField(default=False)
    rents_home = models.BooleanField(default=False)
    landlord_allows_pets = models.BooleanField(default=False)
    has_other_pets = models.BooleanField(default=False)
    number_of_pets = models.IntegerField(default=0)
    experience_with_animals = models.BooleanField(default=False)
    adoption_reason = models.TextField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Profile of: {self.user.name}"


class OngProfile(models.Model):

    cnpj = models.CharField(max_length=18, unique=True)
    responsavel = models.CharField(max_length=100)
    site = models.URLField(blank=True)
    instagram = models.CharField(max_length=100, blank=True)
    logo = models.ImageField(upload_to="ongs/", blank=True, null=True)
    descricao = models.TextField(blank=True)
    horario_funcionamento = models.CharField(max_length=100, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"Ong: {self.user.name}"
    

class TutorPreferences(models.Model):
    SIZE=[
        ("LARGE","Grande"),
        ("SMALL","Pequeno"),
        ("ANY","Qualquer"),
    ]
    AGE=[
        ("PUPPY","Filhote"),
        ("ADULT","Adulto"),
        ("SENIOR","Idoso"),
        ("ANY","Qualquer"),
    ]
    GENDER=[
        ("MALE","Macho"),
        ("FEMALE","Fêmea"),
        ("ANY","Qualquer"),
    ]
    SPECIE=[
        ("DOG","Cachorro"),
        ("CAT","Gato"),
        ("RABBIT","Coelho"),
        ("OTHER","Outro"),
        ("ANY","Qualquer"),
    ]
    TEMPERAMENT=[
        ("CALM","Calmo"),
        ("PLAYFUL","Brincalhão"),
        ("ACTIVE","Ativo"),
        ("SHY","Tímido"),
        ("ANY","Qualquer"),
    ]

    tutor = models.OneToOneField(TutorProfile, on_delete=models.CASCADE)
    preferred_size = models.CharField(max_length=15, choices=SIZE, default="ANY")
    preferred_age = models.CharField(max_length=15, choices=AGE, default="ANY")
    preferred_gender = models.CharField(max_length=15, choices=GENDER, default="ANY")
    preferred_specie = models.CharField(max_length=15, choices=SPECIE, default="ANY")
    preferred_temperament = models.CharField(max_length=15, choices=TEMPERAMENT, default="ANY")
    wants_good_with_children = models.BooleanField(default=False)
    wants_good_with_dogs = models.BooleanField(default=False)
    wants_good_with_cats = models.BooleanField(default=False)
    accepts_not_neutered = models.BooleanField(default=True)
    accepts_not_vaccinated = models.BooleanField(default=True)

    def __str__(self):
        return f"Preferences of {self.tutor.user.name}"