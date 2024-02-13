from django.urls import path, include
from .basics.views import movie_list, movie_detail
from .serializers.function.views import movie_list_serializer_function_based, movie_detail_serializer_function_based
from .serializers.classbased.views import MovieSerializerDetailAv, MovieSerializerListAv
from .model.function.views import movie_detail_model_function_based, movie_list_model_function_based
from .model.classbased.views import MovieModelListAv, MovieModelDetailAv

urlpatterns = [
    path('basics/list/', movie_list, name='basics-movie-list'),
    path('basics/<int:movie_id>/', movie_detail, name='basics-movie-detail'),

    path('serializer/function/list/', movie_list_serializer_function_based, name='serializer-function-movie-list'),
    path('serializer/function/<int:movie_id>/', movie_detail_serializer_function_based,
         name='serializer-function-movie-detail'),

    path('serializer/class/list/', MovieSerializerListAv.as_view(), name='serializer-class-movie-list'),
    path('serializer/class/<int:movie_id>/', MovieSerializerDetailAv.as_view(), name='serializer-class-movie-detail'),

    path('model/function/list/', movie_list_model_function_based, name='model-function-movie-list'),
    path('model/function/<int:movie_id>/', movie_detail_model_function_based,
         name='model-function-movie-detail'),

    path('model/class/list/', MovieModelListAv.as_view(), name='model-class-movie-list'),
    path('model/class/<int:movie_id>/', MovieModelDetailAv.as_view(), name='model-class-movie-detail')
]
