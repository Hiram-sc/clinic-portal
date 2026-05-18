from django import forms
from datetime import date
from dateutil.relativedelta import relativedelta
import re
from django.core.exceptions import ValidationError

"""
Trocar form de idade para data de nascimento e implementar endereço.
"""
class AgendarForm(forms.Form):
    responsavel = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Nome do responsável'
        }),
        max_length=150, 
        label="Responsável",
        required=True,
        error_messages={
            'required': "Preencha este campo."
        }
    )

    paciente = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Nome do paciente'
        }),
        label="Paciente",
        max_length=150,
        required=True,
        error_messages= {
            'required': "Preencha este campo."
        }
    )

    data_nascimento = forms.DateField(
        widget=forms.DateInput(attrs={
            'id': 'id_data_nascimento',
            'class': 'form-input',
            'placeholder': 'dd/mm/aaaa'
        }),
        label="Data de nascimento",
        input_formats=['%d/%m/%Y'],
        required=True,
        error_messages= {
            'required': 'Preencha este campo.'
        }
    )

    telefone = forms.CharField(
        widget=forms.TextInput(attrs={
            'id': 'id_telefone',
            'class': 'form-input',
            'placeholder': '(00) 00000-0000'
        }),
        label="Whatsapp",
        max_length=20,
        required=True,
        error_messages= {
            'required': 'Preencha este campo.'
        }
    )


    def clean_responsavel(self):
        responsavel = (self.cleaned_data.get('responsavel') or '').strip()

        if len(responsavel.split()) < 2:
            raise ValidationError(
                'Informe o nome e sobrenome do responsável.'
            )
        
        return responsavel
    
    def clean_paciente(self):
        paciente = (self.cleaned_data.get('paciente') or '').strip()

        if len(paciente.split()) < 2:
            raise ValidationError(
                'Informe o nome e sobrenome do paciente.'
            )
        
        return paciente
    
    def clean_data_nascimento(self):
        data_nascimento = self.cleaned_data.get('data_nascimento')

        hoje = date.today() 

        if data_nascimento > hoje:
            raise ValidationError(
                'Data de nascimento fora do intervalo permitido.'
            )
        
        limite_18 = hoje - relativedelta(years=18)

        if data_nascimento < limite_18:
            raise ValidationError(
                'Atendimento apenas para menores de 18 anos.'
            )

        return data_nascimento
    
    def clean_telefone(self):
        telefone = (self.cleaned_data.get('telefone') or '').strip()

        telefone_limpo = re.sub(r'\D', '', telefone)

        if len(telefone_limpo) < 10 or len(telefone_limpo) > 11:
            raise ValidationError(
                'O número deve conter pelo menos 10 dígitos e estar no formato (00) 00000-0000.'
            )
        
        if len(telefone_limpo) == 11 and telefone_limpo[2] != '9':
            raise ValidationError(
                'Número de telefone inválido.'
                )
        
        if telefone_limpo == telefone_limpo[0] * len(telefone_limpo):
            raise ValidationError(
                'Número de telefone inválido.'
            )
        
        return telefone_limpo
        

        