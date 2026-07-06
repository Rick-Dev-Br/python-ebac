from django.urls import reverse


def test_home_view_uses_index_template(client):
    response = client.get(reverse("home"))
    template_names = [template.name for template in response.templates]

    assert response.status_code == 200
    assert "portfolio/base.html" in template_names
    assert "portfolio/index.html" in template_names
    assert b"Desenvolvedor Python" in response.content
