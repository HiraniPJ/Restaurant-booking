"""restaurant_booking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin # type: ignore
from django.contrib.auth import views as auth_views # type: ignore
from django.urls import path # type: ignore
from bookings import views # type: ignore
from django.contrib.auth.views import LogoutView # type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='bookings/login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('reserve/', views.make_reservation, name='make_reservation'),
    path('my_reservations/', views.my_reservations, name='my_reservations'),
    path('delete_reservation/<int:reservation_id>/', views.delete_reservation, name='delete_reservation'),
    path('edit_reservation/<int:reservation_id>/', views.edit_reservation, name='edit_reservation'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]
