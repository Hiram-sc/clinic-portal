import re
from datetime import date

from dateutil.relativedelta import relativedelta

from django import forms
from django.core.exceptions import ValidationError

"""
Trocar form de idade para data de nascimento e implementar endereço.
"""
class AgendarForm(forms.Form):
    responsavel = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-input input-name',
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
            'class': 'form-input input-name',
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

    cidade = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-input input-name',
            'placeholder': 'Ex: Campos dos Goytacazes'
        }),
        label="Cidade",
        max_length=100,
        required=True,
        error_messages= {
            'required': 'Preencha este campo.'
        }
    )

    bairro = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-input input-name',
            'placeholder': 'Ex: Centro'
        }),
        label="Bairro",
        max_length=100,
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
        
        texto_limpo = responsavel.replace(" ", "").lower()
        
        if len(set(texto_limpo)) == 1:
            raise ValidationError(
                'Nome inválido.'
            )
        
        return responsavel
    
    def clean_paciente(self):
        paciente = (self.cleaned_data.get('paciente') or '').strip()

        if len(paciente.split()) < 2:
            raise ValidationError(
                'Informe o nome e sobrenome do paciente.'
            )
        
        texto_limpo = paciente.replace(" ", "").lower()

        if len(set(texto_limpo)) == 1:
            raise ValidationError(
                'Nome inválido.'
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
    
    def clean_cidade(self):
        cidade = (self.cleaned_data.get('cidade') or '').strip()

        if len(cidade) < 3:
            raise ValidationError(
                'Cidade inválida.'
            )

        if not re.match(r"^[A-Za-zÀ-ÿ0-9\s\-']+$", cidade):
            raise ValidationError(
                'Cidade inválida.'
            )
        
        texto_limpo = cidade.replace(" ", "").lower()
        
        if len(set(texto_limpo)) == 1:
            raise ValidationError(
                'Cidade inválida.'
            )

        return cidade
    
    def clean_bairro(self):
        bairro = (self.cleaned_data.get('bairro') or '').strip()
        
        if len(bairro) < 3:
            raise ValidationError(
                'Bairro inválido.'
            )

        if not re.match(r"^[A-Za-zÀ-ÿ0-9\s\-']+$", bairro):
            raise ValidationError(
                'Bairro inválido.'
            )
        
        texto_limpo = bairro.replace(" ", "").lower()
        
        if len(set(texto_limpo)) == 1:
            raise ValidationError(
                'Bairro inválido.'
            )

        return bairro

        