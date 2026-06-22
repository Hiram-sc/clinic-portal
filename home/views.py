from urllib.parse import quote

from django.shortcuts import render, redirect

from home.forms import AgendarForm

def home(request):

    carousel = [
        {
            "id": 1,
            "star" : 5,
            "comment":"Excelente profissional, atenciosa, dedicada. Cuida com amor 😍"
        },
        {
            "id": 2,
            "star" : 5,
            "comment":"Excelente médica e pessoa, humana e super atenciosa! Se pudesse daria 10 estrelas."
        },
        {
            "id": 3,
            "star" : 5,
            "comment":"A Dra Janaína é maravilhosa, muito atenciosa e positiva! A cura da alergia veio! Foi uma benção de Deus encontrá-la!"
        },
        {
            "id": 4,
            "star" : 5,
            "comment":"Excelente"
        }
    ]

    for item in carousel:
        item["stars_range"] = range(item["star"])

    return render(request, 'home/home.html', {
        "carousel" : carousel
    })

def para_pais(request):
    return render(request, 'home/para_pais.html')

def agendar(request):
    if request.method == 'POST':
        form = AgendarForm(request.POST)

        if form.is_valid():
            responsavel = form.cleaned_data['responsavel']
            paciente = form.cleaned_data['paciente']

            grau_parentesco = form.cleaned_data['parentesco']
            parentesco = dict(form.fields['parentesco'].choices).get(grau_parentesco)

            data_nascimento = form.cleaned_data['data_nascimento']
            telefone = form.cleaned_data['telefone']
            cidade = form.cleaned_data['cidade']
            bairro = form.cleaned_data['bairro']

            data_nascimento = data_nascimento.strftime('%d/%m/%Y')

            mensagem = quote(
                f"Olá! 👋\n\n"
                f"Me chamo {responsavel} e gostaria de agendar uma consulta com a Dra. Janaína.\n\n"
                f"Paciente: {paciente}\n"
                f"Parentesco: {parentesco}\n"
                f"Data de nascimento: {data_nascimento}\n"
                f"Telefone para contato: {telefone}\n"
                f"Endereço: {bairro} - {cidade}\n\n"
                f"Fico no aguardo de um retorno. Muito obrigado(a)! 😊"
            )

            return redirect(f"https://api.whatsapp.com/send?phone=5522999060047&text={mensagem}")

    else:
        form = AgendarForm()

    return render(request, 'home/agendar_consulta.html', {
        'form' : form
    })


