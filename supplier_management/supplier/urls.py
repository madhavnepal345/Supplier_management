from django.urls import path
from .views import ProductListView,ProductCreateView,ReviewListView,ReviewCreateView,OrderListReview,OrderUpdateView,ClientListView,ClientCreateView,ClientOrderView


urlpatterns=[
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:product_id>/reviews/', ReviewListView.as_view(), name='review_list'),
    path('products/<int:product_id>/reviews/create/', ReviewCreateView.as_view(), name='review_create'),
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('orders/<int:pk>/update/', OrderUpdateView.as_view(), name='order_update'),
    path('clients/', ClientListView.as_view(), name='client_list'),
    path('clients/create/', ClientCreateView.as_view(), name='client_create'),
    path('clients/orders/', ClientOrderView.as_view(), name='client_order'),
]