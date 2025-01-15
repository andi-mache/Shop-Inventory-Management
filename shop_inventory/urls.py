"""SalesManagementSystem URL Configuration"""

from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.contrib.auth import views as auth_views
from users import views as user_views
from shop import views as shop_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('shop/',include('shop.urls')),
    path("register/", user_views.register, name="register"),
    path("dashboard/", user_views.dashboard, name="dashboard"),
    path("update-profile/", user_views.update_profile, name="update-profile"),
    path(
        "", auth_views.LoginView.as_view(template_name="users/login.html"), name="login"
    ),
    path("logout", auth_views.logout_then_login, name="logout"),
    path("user", shop_views.user),
    path("show", shop_views.show),
    path("edit/<int:id>", shop_views.edit),
    path("update/<int:id>", shop_views.update),
    path("delete/<int:id>", shop_views.delete),
    # Items
    path("user_items", shop_views.user_items),
    path("show_items", shop_views.show_items),
    path("edit_items/<int:id>", shop_views.edit_items),
    path("update_items/<int:id>", shop_views.update_items),
    path("delete_items/<int:id>", shop_views.delete_items),
    # sales
    path("user_catsales", shop_views.user_catsales),
    path("show_catsales", shop_views.show_catsales),
    path("delete_catsales/<int:id>", shop_views.delete_catsales),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

