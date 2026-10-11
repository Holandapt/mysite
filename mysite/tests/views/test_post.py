import pytest
from django.urls import reverse

# Função de teste. 
# O parâmetro client é uma fixture especial fornecida pelo pytest-django.
# Ele simula um navegador web (um cliente HTTP) para que possas fazer requisições a aplicação 
# sem precisar de a colocar a correr num servidor real.

@pytest.mark.django_db
def test_post_view(client):
    # Procura no sistema de rotas do Django qual é o endereço correspondente ao nome home e guarda-o na variável url
    url = reverse('home')
    # Utiliza o cliente simulado (client) para fazer um pedido HTTP do tipo GET 
    # (o mesmo que abrir a página no navegador) para aquela URL. 
    # O resultado (código de status, conteúdo HTML, headers, etc.) é guardado na variável response
    response = client.get(url)
    assert response.status_code == 200