from django.shortcuts import render

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
    return render(request, 'home/agendar_consulta.html')


