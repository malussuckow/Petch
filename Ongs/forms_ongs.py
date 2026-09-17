from users.models import RegisterOng
from django import forms

class forms_Ongs(forms.ModelForm):
    
    class Meta:
        model = RegisterOng
        fields = ['cnpj','responsavel','site','instagram',
                'logo','descricao','horario_funcionamento']