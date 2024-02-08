from rest_framework import routers

from . import views

from django.urls import path, re_path


app_name = "bcmr_main"

router = routers.DefaultRouter()

# router.register("tokens", views.TokenViewSet)


urlpatterns = router.urls
urlpatterns += [
    # re_path(r"^registry/(?P<category>[\w+:]+)/$", views.get_published_url, name='get-registry'),
    # re_path(r"^registry/(?P<category>[\w+:]+)/urls/$", views.get_published_url, name='get-registry-urls'),
    # re_path(r"^registry/(?P<category>[\w+:]+)/urls/published/$", views.get_published_url, name='get-registry-urls-published'),
    re_path(r"^registry/(?P<category>[\w+:]+)/identity-snapshot/$", views.IdentitySnapshot.as_view(), name='get-identity-snapshot'),
    re_path(r"^registry/(?P<category>[\w+:]+)/identity-snapshot/token-category/$", views.TokenCategory.as_view(), name='get-token-category'),
    re_path(r"^registry/(?P<category>[\w+:]+)/identity-snapshot/token-category/nfts/$", views.NftCategory.as_view(), name='get-nfts'),
    re_path(r"^registry/(?P<category>[\w+:]+)/identity-snapshot/token-category/nfts/parse/bytecode/$", views.ParseBytecode.as_view(), name='get-nfts-parse-bytecode'),
    re_path(r"^registry/(?P<category>[\w+:]+)/identity-snapshot/token-category/nfts/parse/types/$", views.NftType.as_view(), name='get-nfts-parse-type'),
    
]
