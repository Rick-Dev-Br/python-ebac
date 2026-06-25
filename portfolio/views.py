from django.shortcuts import render


def home(request):
    context = {
        "profile": {
            "name": "Adilson Henrique",
            "role": "Desenvolvedor Python",
            "summary": (
                "Portfolio generico desenvolvido em Django para apresentar "
                "habilidades, projetos e formas de contato."
            ),
        },
        "skills": [
            "Python",
            "Django",
            "HTML",
            "CSS",
            "Git",
            "Banco de Dados",
        ],
        "projects": [
            {
                "title": "Web Scraper Assincrono",
                "description": (
                    "Coleta dados de paginas web usando Python, asyncio, "
                    "aiohttp e BeautifulSoup."
                ),
            },
            {
                "title": "API de Estudos",
                "description": (
                    "Projeto backend para praticar rotas, regras de negocio "
                    "e persistencia de dados."
                ),
            },
            {
                "title": "Portfolio Django",
                "description": (
                    "Pagina web simples para exibir perfil profissional, "
                    "habilidades e projetos."
                ),
            },
        ],
        "contact": {
            "email": "adilson@example.com",
            "github": "https://github.com/Rick-Dev-Br",
            "linkedin": "https://www.linkedin.com/",
        },
    }
    return render(request, "portfolio/home.html", context)
