"""csIA URL Configuration

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
from django.contrib import admin
from django.urls import path

import aboutus.views as aviews
import Home.views as hviews
import account.views as cviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', aviews.about, name="about"),
    path('', hviews.home, name="home"),
    # path(r'^$', hviews.home, name="home"),
    path('login', cviews.login, name="login"),
    path('home', hviews.user_home, name="user_home"),
    path('logout', cviews.logout, name="logout"),
    path('add_player', hviews.add_player, name="add_player"),
    path('search_player',hviews.search_player, name='search_player'),
    path('update_data',hviews.update_data, name='update_data'),
    path('players/<int:age_id>', hviews.view_players, name="players"),
]