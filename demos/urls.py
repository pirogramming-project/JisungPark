from django.urls import path
from demos import views
from .views import *

app_name = 'demos'

urlpatterns = [
    path('', views.home, name='home'),  
    path('map/', views.map, name='map'),  
    path('introduce/', views.introduce, name='introduce'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('guidemap/', views.guidemap, name='guidemap'),
    path('mypage/', views.mypage, name='mypage'),
    path("api/get_parking/<int:parking_lot_id>/", views.get_parking, name="get_parking"),
    path('api/myreviews/', views.get_myreviews, name='get_myreviews'),
    path('api/add_review/', views.add_review, name='add_review'),
    path('api/reviews/<int:parking_lot_id>/', views.get_reviews, name='get_reviews'),
    path("api/update_review/<int:review_id>/", update_review, name="update_review"),
    path('api/delete_review/<int:review_id>/', views.delete_review, name='delete_review'),  
    path('qna/', views.qna, name='qna'),
    path('qna/list/', views.qanda_list, name='qanda_list'),
    path('qna/detail/<int:pk>', views.qna_detail, name='qna_detail'),
    path('qna/create/', views.qanda_create, name='qanda_create'),
    path('qna/update/<int:pk>', views.qanda_update, name='qanda_update'),
    path('qna/delete/<int:pk>', views.qanda_delete, name='qanda_delete'),
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('api/real-time-parking/', views.load_parking_data, name='real_time_parking'),  # 실시간 데이터 API
    path('api/toggle_favorite/', toggle_favorite, name='toggle_favorite'),
    path("api/favorites/", get_favorites, name="get_favorites"),
    path("mypage/update/<int:user_id>", views.mypage_detail, name='mypage_detail'),
    path("accounts/withdraw/<int:user_id>/", withdraw_user, name="withdraw_user")
]