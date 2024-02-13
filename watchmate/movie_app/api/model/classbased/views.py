from rest_framework import status, viewsets

from ....models import Movie
from ..serializers import MovieModelSerializer
from rest_framework.response import Response
from rest_framework.views import APIView


class MovieModelListAv(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        model_serializer = MovieModelSerializer(movies, many=True)
        return Response(model_serializer.data)

    def post(self, request):
        model_serializer = MovieModelSerializer(data=request.data)
        if model_serializer.is_valid():
            model_serializer.save()
            return Response(model_serializer.data)
        else:
            return Response(model_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieModelDetailAv(APIView):
    def get(self, request, movie_id):
        try:
            movie = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            return Response({'error': "Movie not found"}, status=status.HTTP_404_NOT_FOUND)
        model_serializer = MovieModelSerializer(movie)
        return Response(model_serializer.data)

    def put(self, request, movie_id):
        try:
            movie = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            return Response({'error': "Movie not found"}, status=status.HTTP_404_NOT_FOUND)
        model_serializer = MovieModelSerializer(movie, data=request.data)
        if model_serializer.is_valid():
            model_serializer.save()
            return Response(model_serializer.data)
        else:
            return Response(model_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, movie_id):
        try:
            movie = Movie.objects.get(id=movie_id)
        except Movie.DoesNotExist:
            return Response({'error': "Movie not found"}, status=status.HTTP_404_NOT_FOUND)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
