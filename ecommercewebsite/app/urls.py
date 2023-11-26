from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm

urlpatterns = [
    path('', views.ProductView.as_view(), name = "home"),
    path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),

    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('homeappliances/', views.homeappliances, name='homeappliances'),
    path('homeappliances/<slug:data>/', views.homeappliances, name='homeappliancesdata'),
    #LoginView paila nai banya hunxa inbuild, yesma template dina parxa ja nera login form hunxa
    
    path('accounts/login/', auth_view.LoginView.as_view(template_name = 'app/login.html', authentication_form = LoginForm), name='login'),
    
    path('password-reset/', auth_view.PasswordResetView.as_view
        (template_name='app/password_reset.html',form_class=MyPasswordResetForm), name='password_reset'),

    path('password-reset/done', auth_view.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), 
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view
         (template_name='app/password_reset_confirm.html',form_class=MySetPasswordForm), name='password_reset_confirm'),

     path('password-reset/complete', auth_view.PasswordResetCompleteView.as_view(template_name=
            'app/password_reset_confirm.html'), name='password_reset_confirm'),
    
    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name = 'logout'),
    path('registration/', views.CustomerRegistratioinView.as_view(), name='customerregistration'),
    
    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name='app/passwordchange.html', 
        form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),

    path('passwordchangedone/', auth_view.PasswordChangeView.as_view(template_name='app/passwordchangedone.html'), 
        name='passwordchangedone'),

    path('checkout/', views.checkout, name='checkout'),
    path('menwear/', views.menwear, name='menwear'),
    path('womenwear/', views.womenwear, name='womenwear'),
    path('childrenwear/', views.childrenwear, name='childrenwear'),
    path('cosmetics/', views.cosmetics, name='cosmetics'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
