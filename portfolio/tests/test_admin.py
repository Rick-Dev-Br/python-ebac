from django.contrib import admin

from portfolio.admin import PostAdmin
from portfolio.models import Post


def test_post_is_registered_in_django_admin():
    assert admin.site.is_registered(Post)
    assert isinstance(admin.site._registry[Post], PostAdmin)
