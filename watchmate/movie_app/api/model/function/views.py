from rest_framework import status

from ....models import Movie
from ..serializers import MovieModelSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET", "POST"])
def movie_list_model_function_based(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        # passing a queryset into your serializer without setting the many flag, because by default it thinks it is a single value
        #  so serializer can fetch each movie and map it
        model_serializer = MovieModelSerializer(movies, many=True)
        # When we return data as JsonResponse(...) from your view, Django's JsonResponse() expects your JSON data to be in key:value pairs.
        # So to tell that to JsonResponse we need to pass set safe=False:
        return Response(model_serializer.data)
    if request.method == 'POST':
        model_serializer = MovieModelSerializer(data=request.data)
        if model_serializer.is_valid():
            model_serializer.save()
            return Response(model_serializer.data)
        else:
            return Response(model_serializer.errors)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def movie_detail_model_function_based(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return Response({'error': "Movie not found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        model_serializer = MovieModelSerializer(movie)
        return Response(model_serializer.data)
    if request.method == 'PUT' or request.method == "PATCH":
        model_serializer = model_serializer(movie, data=request.data)
        if model_serializer.is_valid():
            model_serializer.save()
            return Response(model_serializer.data)
        else:
            return Response(model_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
