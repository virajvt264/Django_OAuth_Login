# users/adapters.py
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        # Skip the intermediate confirmation page
        return super().pre_social_login(request, sociallogin)

    def get_connect_redirect_url(self, request, socialaccount):
        # Directly redirect to the final destination
        return settings.LOGIN_REDIRECT_URL


class CustomAccountAdapter(DefaultAccountAdapter):
    def login(self, request, user):
        # Perform login directly without additional pages
        ret = super().login(request, user)
        return ret