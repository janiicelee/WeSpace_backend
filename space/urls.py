from django.urls import path

from .views      import (
    CategoryView,
    RecommendView,
    EditorView,
    DetailSpaceView,
    Registration,
    Reservation
)

urlpatterns = [
    path(''                , SpaceView.as_view())      , 
    # Recommend는 위 엔도포인트에서 옵션 처리 해주기
    #path('/recommend'      , RecommendView.as_view())   , 
    # registration은 위 SpaceView의 post 로 들어가기
    #path('/registration'   , Registration.as_view())    , 
    path('/categories'     , CategoryView.as_view())    , 
    path('/reservation'    , Reservation.as_view())     , 
    path('/<int:space_id>' , DetailSpaceView.as_view())
]
