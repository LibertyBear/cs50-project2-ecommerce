from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    # Additionals:

    path("create", views.create, name = "create"),


    path("categories", views.categories, name = "categories"),

    path("listing/<int:listing_id>", views.listing, name = "listing"),
   

    path("watchlist", views.watchlist, name = "watchlist"),
    path("close/<int:listing_id>", views.close, name = "close"),
    
    path("listing/<str:category>", views.categoryListing, name = "categoryListing"),

    path("toggle_watchlist/<int:listing_id>", views.toggle_watchlist, name = "toggle_watchlist")
]
