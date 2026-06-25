import pytest

from portfolio.models import Post


@pytest.mark.django_db
def test_post_str_returns_title():
    post = Post.objects.create(
        title="Primeiro post",
        content="Conteudo de exemplo para o portfolio.",
    )

    assert str(post) == "Primeiro post"


@pytest.mark.django_db
def test_post_generates_slug_automatically():
    post = Post.objects.create(
        title="Meu Post Novo",
        content="Conteudo qualquer para teste.",
    )

    assert post.slug == "meu-post-novo"


@pytest.mark.django_db
def test_post_is_unpublished_by_default():
    post = Post.objects.create(
        title="Post em rascunho",
        content="Este post ainda nao foi publicado.",
    )

    assert post.is_published is False
