from django.urls import path
from .import views

urlpatterns = [
    path('',views.home),
    path('ShowProduct/<id>',views.ShowProduct),
    path('ViewDetails/<id>',views.ViewDetails),
    path('Login',views.Login),
    path('SignUp',views.SignUp),
    path('SignOut',views.SignOut),
    path('addToCart',views.addToCart),
    path('showCartItems',views.showCartItems),
    #path('getquery',views.getquery,name='getquery')
]
