from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Music
from .serializers import SongSerializer

# Create your views here.


@api_view(["GET", "POST"])
def songs_list(request):

    if request.method == "GET":
        songs = Music.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = SongSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def song_detail(request, pk):

    song = get_object_or_404(Music, pk=pk)
    if request.method == "GET":
        serializer = SongSerializer(song)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = SongSerializer(song, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
