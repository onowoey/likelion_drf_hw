from rest_framework import serializers
from .models import *

class SingerSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    songs = serializers.SerializerMethodField(read_only=True)
    
    def get_songs(self, instance):
        serializer = SongSerializer(instance.songs, many=True)
        return serializer.data
    
    class Meta:
        model = Singer
        fields = ['id', 'name','debut','songs']
        
class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
        read_only_fields = ['singer'] #시리얼라이저가 데이터를 받을 때 singer 필드는 입력 받지 않겠다
        #나중 views.py 에서 singer 넣어줌