from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Singer, Song , Tag
from .serializers import SingerSerializer, SongSerializer , TagSerializer

from django.shortcuts import get_object_or_404

@api_view(['GET','POST'])
def singer_list_create(request):
    if request.method == 'GET':
        singers = Singer.objects.all()
        serializer = SingerSerializer(singers, many=True)
        return Response(data = serializer.data)
    if request.method == 'POST':
        serializer = SingerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            singer = serializer.save()
            content = request.data['content']
            tags = [words[1:] for words in content.split(' ') if words.startswith('#')]
            for t in tags:
                try:
                    tag = get_object_or_404(Tag, name=t)
                except:
                    tag = Tag(name=t)
                    tag.save()
                singer.tags.add(tag)
            singer.save()
            return Response(data=SingerSerializer(singer).data)
        
@api_view(['GET','DELETE','PATCH'])
def singer_detail_update_delete(request, singer_id):
    singer = get_object_or_404(Singer, id = singer_id)
    
    if request.method == 'GET':
        serializer = SingerSerializer(singer)
        return Response(serializer.data)
    
    elif request.method == 'PATCH':
        serializer = SingerSerializer(instance=singer, data=request.data, partial=True)
        if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data)
            singer = serializer.save()
            content = request.data.get("content")
            if content is not None: #content 잇을 때만 수정 -> 다른 필드 수정할 때를 위해
                singer.tags.clear()
                tags = [words[1:] for words in content.split(' ') if words.startswith('#')]

                for t in tags:
                    tag, created = Tag.objects.get_or_create(name=t)
                    singer.tags.add(tag)

            singer.save()


        return Response(data=SingerSerializer(singer).data)
    
    elif request.method == 'DELETE':
        singer.delete()
        data = {
            'deleted_singer': singer_id
        }
        return Response(data)
    
@api_view(['GET','POST'])
def song_read_create(request, singer_id):
    singer = get_object_or_404(Singer, id=singer_id)
    
    if request.method == 'GET':
        songs = Song.objects.filter(singer=singer)
        serializer = SongSerializer(songs, many=True)
        return Response(data=serializer.data)
    
    elif request.method == 'POST':
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(singer=singer)
        return Response(serializer.data)
    
@api_view(['GET'])
def find_tag(request, tags_name):
    tags = get_object_or_404(Tag, name=tags_name)
    if request.method == 'GET':
        singer = Singer.objects.filter(tags__in = [tags])
        serializer = SingerSerializer(singer, many=True)
        return Response(data = serializer.data)