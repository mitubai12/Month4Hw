from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from post.views import (
    HelloView, AnekdotView, MainView,
    post_list_view, PostCreateView, PostDetailView, PostUpdateView, post
)
from user.views import (
    RegisterView, LoginView, LogoutView, ProfileView,
)

# Admin panel
urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path('admin/', admin.site.urls),
]

# General views
urlpatterns += [
    path('', MainView.as_view(), name='main_view'),
    path('hello/', HelloView.as_view(), name="hello_view"),
    path('fun/', AnekdotView.as_view(), name='anekdot_view'),
]

# Book-related views
urlpatterns += [
    path('posts/', post_list_view, name='book_list_view'),
    path('posts/create/', PostCreateView.as_view(), name='book_create_view'),
    path('posts/create2/', post, name='post_create_view'),
    path('posts/<int:post_id>/', PostDetailView.as_view(), name='book_detail_view'),
    path('posts/<int:post_id>/edit/', PostUpdateView.as_view(), name='book_update_view'),
]

# User-related views
urlpatterns += [
    path('register/', RegisterView.as_view(), name='register_view'),
    path('login/', LoginView.as_view(), name='login_view'),
    path('logout/', LogoutView.as_view(), name='logout_view'),
    path('profile/', ProfileView.as_view(), name='profilje_view')
]

# Serving media files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
