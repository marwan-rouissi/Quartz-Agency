from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): # *args, **kwargs
    print(args, kwargs)
    print(request.user)

    prompt1 = """Je suis freelance sur les réseaux sociaux depuis 3 ans. Mon expérience m'a permis de toucher à tout et de voir évoluer 
le secteur. Une évolution stagnante jusqu'à l'arrivée de l'intelligence artificielle génératrice de contenus entre les 
mains du grand public."""
    prompt2 = """Pour la majorité de la population, Chat GPT, Midjourney... sont des révolutions. Ainsi, une multitude de tâches est 
simplifiée : les posts LinkedIn, les articles de blog, ... et mes demandes pour ce genre de prestations ont disparu.
Des collègues concurrents freelance sur les réseaux sociaux ont dû chercher un plan B voir arrêter cette activité.
Bref, notre métier est menacé. Plutôt que de chercher à me battre à tous les coups contre l'intelligence artificielle,
j'ai décidé de travailler avec elle : elle a ses forces et ses faiblesses et j'ai les miennes.
Utilisons ses forces pour combler nos faiblesses, gagner du temps et être plus productifs, tout en connaissant ses
failles pour les apprivoiser."""
    prompt3 = """Voilà le projet pour l'outil que vous vous apprêtez à utiliser : selon notre étude, 90% des dirigeants de petites structures, 
responsables communication ou freelance sur les réseaux sociaux, se plaignent de leurs communications. Trop peu de créations, 
pas assez d'idées, trop cher, pas suffisamment rentable, trop aléatoire, changeant...
L'IA réduit le temps de production (donc les coûts), trouve une multitude d'idées, et exécute rapidement. Mon agence grâce à
mon expertise connait les réseaux sociaux, les normes, les algorithmes, les trend et les manie avec brio.
Allions les 2 !"""
    prompt4 = """Voici donc le 1e générateur de contenus automatisé par intelligence artificielle au service des petites structures pour générer
du contenu adapté à vos réseaux sociaux, vos besoins, votre budget.
Qu'attendez-vous pour le tester ?"""
    context = {

        "prompt1":prompt1,
        "prompt2":prompt2,
        "prompt3":prompt3,
        "prompt4":prompt4
    }
    return render(request, "home.html", context)

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        "title": "abc this is about us",
        "this_is_true": True,
        "my_number": 123,
        "my_list": [1313, 4231, 312, "Abc"],
        "my_html": "<h1>Hello World</h1>"

    }
    return render(request, "about.html", my_context)


def social_view(request, *args, **kwargs):
    return HttpResponse("<h1>Socail Page</h1>")