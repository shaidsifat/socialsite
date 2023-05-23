from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields =['id','text','image','like','comment','share','created_by','created_at']
