from rest_framework import status

from ....models import Movie
from ..serializers import MovieSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET", "POST"])
def movie_list_serializer_function_based(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        # passing a queryset into your serializer without setting the many flag, because by default it thinks it is a single value
        #  so serializer can fetch each movie and map it
        serializer = MovieSerializer(movies, many=True)
        # When we return data as JsonResponse(...) from your view, Django's JsonResponse() expects your JSON data to be in key:value pairs.
        # So to tell that to JsonResponse we need to pass set safe=False:
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(["GET", "PUT", "PATCH", "DELETE"])
def movie_detail_serializer_function_based(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id)
    except Movie.DoesNotExist:
        return Response({'error': "Movie not found"}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    if request.method == 'PUT' or request.method == "PATCH":
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
