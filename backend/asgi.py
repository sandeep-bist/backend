"""
ASGI config for backend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from chat.route import websocket_urlpatterns
from chat.channels_middleware import JWTWebsocketMiddleware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application = get_asgi_application()

application=ProtocolTypeRouter({
    "http":application,
    "websocket":JWTWebsocketMiddleware(AuthMiddlewareStack(URLRouter(websocket_urlpatterns)))
    
}
)
