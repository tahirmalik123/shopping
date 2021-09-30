from django.contrib.auth import views as auth_views
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from .forms import LoginForm, passwordchange, pass_reset, pass_reset_confirm
urlpatterns = [
    # path('', views.ProductView.as_view(), name="productview"),
    path('', views.home, name="home"),
    path('product-detail/<int:id>', views.product_detail, name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('pluscart/', views.plus_cart, name='plus-cart'),
    path('minuscart/', views.Minus_cart, name='minus-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', auth_views.PasswordChangeView.as_view(template_name= 'app/passwordchange.html', form_class = passwordchange, success_url = '/pass_done/'), name='changepassword'),
    path('pass_done/', auth_views.PasswordChangeDoneView.as_view(template_name='app/pass_change_done.html'), name='pass_done'),
    path('pass_reset/', auth_views.PasswordResetView.as_view(template_name='app/pass_reset.html', form_class = pass_reset), name='pass_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name = 'app/pass_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = 'app/pass_reset_confirm.html', form_class = pass_reset_confirm), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'app/pass_reset_complete.html'), name='password_reset_complete'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('logout/', auth_views.LogoutView.as_view(next_page = 'login'), name='logout'),
    path('registration/', views.customerregistration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('removecart/', views.Remove_cart),
    path('paymentdone/', views.payment_done, name = "paymentdone"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
