from django.urls import path
from Sales_Management.views import *

urlpatterns = [
    path('', dash_board, name='dash_board'),
    path('register/', register_view, name='register_view'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
    path('sale-list/', sale_list, name='sale_list'),
    path('add-sale/', add_sale, name='add_sale'),
    path('update-sale/<str:s_id>/', update_sale, name='update_sale'),
    path('delete-sale/<str:s_id>/', delete_sale, name='delete_sale'),
]
