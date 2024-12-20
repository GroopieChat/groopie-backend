"""
ASGI config for groupChatBackend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'groupChatBackend.settings')

from django.core.asgi import get_asgi_application

django_asgi_app = get_asgi_application()
from chat import routing
from channels.routing import ProtocolTypeRouter, URLRouter

from channels_auth_token_middlewares.middleware import QueryStringSimpleJWTAuthTokenMiddleware

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": QueryStringSimpleJWTAuthTokenMiddleware(URLRouter(routing.websocket_urlpatterns))
})

ASGI_APPLICATION = 'groupChatBackend.asgi.application'
