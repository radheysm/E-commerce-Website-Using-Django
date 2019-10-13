from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("tracker/", views.tracker, name="tracker"),
    path("search/", views.search, name="search"),
    path("productview/", views.prodview, name="prodview"),
    path("checkout/", views.checkout, name="checkout"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("register/", views.register, name="register"),
    path("sign", views.sign, name = "sign")
]
