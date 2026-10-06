# Esse código é uma estrutura de Factories (fábricas de dados fictícios) 
# usando as bibliotecas factory_boy e Faker


import factory
from faker import Factory as FakerFactory

from django.contrib.auth.models import User
from django.utils.timezone import now

from blog.models import Post

faker = FakerFactory.create()

# Meta.model = User: Informa ao factory_boy que esta classe cria instâncias do model User padrão do Django. 
# email: Gera um e-mail aleatório e seguro (ex: user@example.com).
# username: Usa um LazyAttribute (calculado no momento do disparo) para atribuir um nome falso ao campo username.

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker("safe_email")
    username = factory.LazyAttribute(lambda x: faker.name())

# Manipulação de senha: No Django, 
# senhas não podem ser salvas diretamente como texto puro (password="123"), 
# elas precisam passar por hash (set_password)

# Esse método @classmethod sobrescreve a preparação do objeto: 
# se você passar um parâmetro password ao chamar a fábrica, ele intercepta a senha, 
# aplica o set_password para criptografá-la corretamente e salva o usuário.

    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop("password", None)
        user = super(UserFactory, cls)._prepare(create, **kwargs)
        if password:
            user.set_password(password)
            if create:
                user.save()
            return user
        
class PostFactory(factory.django.DjangoModelFactory):
    title = factory.LazyAttribute(lambda x: faker.sentence())
    created_on = factory.LazyAttribute(lambda x: now())
    author = factory.SubFactory(UserFactory)
    status = 0


    class Meta:
        model = Post