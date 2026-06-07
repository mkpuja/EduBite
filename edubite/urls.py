"""
URL configuration for edubite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from anonymous import views as anoview

urlpatterns = [

    path('admin/', admin.site.urls),

    path('', anoview.index, name="index"),
    path('login/', anoview.login, name="login"),
    path('register/', anoview.register, name="register"),
    path('dashboard/', anoview.dashboard, name="dashboard"),
    path('menu/', anoview.menu, name="menu"),
    path('cart/', anoview.cart, name="cart"),
    path('orders/', anoview.orders, name="orders"),
    path('profile/', anoview.profile, name="profile"),
    path('viewdata/', anoview.viewdata, name="viewdata"),
    path('edit/<int:id>/', anoview.edit, name="edit"),
    path('delete/<int:id>/', anoview.delete, name="delete"),
    path('logout/', anoview.logout, name="logout"),
    path('add-to-cart/<int:food_id>/', anoview.add_to_cart, name="add_to_cart"),
    path('remove-cart/<int:cart_id>/', anoview.remove_cart, name="remove_cart"),
    path('place-order/', anoview.place_order, name="place_order"),
    path('decrease-cart/<int:cart_id>/', anoview.decrease_cart, name="decrease_cart"),
    path('cancel-order/<int:order_id>/', anoview.cancel_order, name="cancel_order"),
]