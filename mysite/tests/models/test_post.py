import pytest
from blog.factories import PostFactory


#Este código é um teste automatizado em Python utilizando a ferramenta pytest
#  e o pacote factory_boy 


# @pytest.fixture: Este decorador diz ao pytest que a função abaixo é uma fixture. 
# Uma fixture serve para preparar o ambiente ou criar dados que vão ser usados nos testes.

#def post_published():: Define a fixture. Sempre que um teste pedir post_published como argumento, 
# o pytest vai executar esta função primeiro.

# return PostFactory(title='pytest with factory'): A fábrica cria e grava na base de dados um post. 
# O título é explicitamente definido como 'pytest with factory', 
# enquanto os outros campos obrigatórios do modelo (se existirem) são gerados automaticamente pela fábrica.

@pytest.fixture
def post_published():
    return PostFactory(title='pytest with factory')


# @pytest.mark.django_db: Este decorador é obrigatório para testes do Django que interagem com a base de dados.
#  Ele avisa o pytest que este teste vai ler ou escrever na base de dados (neste caso, 
# a fábrica cria um registo) e garante que as alterações são apagadas após o teste acabar, para não poluir o ambiente.

#assert post_published.title == 'pytest with factory': É a verificação real (afirmação). 
# O teste confirma se o título do post criado na fixture é 
# exatamente igual ao esperado. Se for igual, o teste passa ✅; se for diferente, o teste falha ❌.

@pytest.mark.django_db
def test_create_published_post(post_published):
    assert post_published.title == 'pytest with factory'