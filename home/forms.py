from django import forms
from django.core.exceptions import ValidationError

class AgendarForm(forms.Form):
    responsavel = forms.CharField(
        widget=forms.TextInput(attrs={
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
            'placeholder': 'Nome do paciente'
        }),
        label="Paciente",
        max_length=150,
        required=True,
        error_messages= {
            'required': "Preencha este campo."
        }
    )

    idade = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'placeholder': 'Idade do paciente'
        }),
        label="Idade",
        min_value=0,
        max_value=120,
        required=True,
        error_messages= {
            'required': 'Preencha este campo.'
        }
    )

    telefone = forms.CharField(
        widget=forms.TextInput(attrs={
            'type': 'tel',
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
    
    def clean_idade(self):
        idade = self.cleaned_data.get('idade')

        if idade is None:
            raise ValidationError(
                'Informe a idade do paciente.'
            )

        return idade
    
    def clean_telefone(self):
        telefone = (self.cleaned_data.get('telefone') or '').strip()

        if len(telefone) < 10 or not telefone.replace('(', '').replace(')', '').replace('-', '').replace(' ', '').isdigit():
            raise ValidationError(
                'O número deve conter pelo menos 10 dígitos e estar no formato (00) 00000-0000'
            )
        
        return telefone
        

        