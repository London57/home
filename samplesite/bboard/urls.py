from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import (BdIndex,
                    BdByRubricView,
                    BdDetailView,
                    BdCreateView,
                    BdDeleteView,
                    BdUpdateView,
                    BdMonthArchiveView,
                    MyLoginView,
                    MyProfileView,
                    ProfileView,
                    MyLogoutView,
                    RegView,
                    fetch,
                    ajax_delete,)


urlpatterns = [
    path('accounts/login/', MyLoginView.as_view(), name='login'),
    path('accounts/registration', RegView.as_view(), name='reg'),
    path('accunts/logout', MyLogoutView.as_view(), name='logout'),
    path('<int:rubric_id>/', BdByRubricView.as_view(), name='by_rubric'),
    path('', BdIndex, name='index'),
    path('add/', BdCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', BdDetailView.as_view(), name='detail'),
    path('detail/<int:pk>/', ajax_delete, name='ajax_delete'),
    path('edit/<int:pk>', BdUpdateView.as_view(), name='post_edit'),
    path('delete/<int:pk>', BdDeleteView.as_view(), name='delete'),
    path('<int:year>/<int:month>/',BdMonthArchiveView.as_view(), name='by_month'),
    path('accounts/profile/', MyProfileView.as_view(), name='my_profile'),
    path('accounts/profile/<int:user_id>', ProfileView.as_view(), name='profile'),
    path('test_fetch', fetch.as_view()),
]