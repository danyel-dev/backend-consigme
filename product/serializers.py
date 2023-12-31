from rest_framework import serializers
from .models import product, message, bag, comment
from django.contrib.auth.models import User
from setup.serializers import UserSerializer
from drf_extra_fields.fields import Base64ImageField


class commentSerializer(serializers.HyperlinkedModelSerializer):
    full_name = serializers.SerializerMethodField()
    initial_letters = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
     
    
    class Meta:
        model = comment
        fields = ['id', 'url', 'user', 'product', 'full_name', 'initial_letters', 'message', 'created_at']
    
    
    extra_kwargs = {
        'user': {'write_only': True},
        'product': {'write_only': True},
    }
    
    
    def get_full_name(self, obj):
        return f'{obj.user.first_name} {obj.user.last_name}'
    
    
    def get_initial_letters(self, obj):
        return f'{obj.user.first_name[0]}{obj.user.last_name[0]}' 
    
     
    def get_created_at(self, obj):
        return f'{obj.created_at.strftime("%d/%m/%Y")} ás {obj.created_at.strftime("%H:%M")}'
    

class productSerializer(serializers.HyperlinkedModelSerializer):
    # user = UserSerializer()
    comment_set = commentSerializer(many=True, read_only=True)
    fullname = serializers.SerializerMethodField()
    image = Base64ImageField()
    
    class Meta:
        model = product
        fields = ['id', 'url', 'fullname', 'comment_set', 'sacoleira', 'image', 'description', 'name', 'value', 'size', 'quantity']
        
    
    def get_fullname(self, obj):
        return f'ricardo'
    
    
class bagSerializer(serializers.HyperlinkedModelSerializer):    
    class Meta:
        model = bag
        fields = ['id', 'url', 'user', 'products']
    
    
class messageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = message
        fields = ['id', 'url', 'title', 'email', 'message', 'created_at' ,'updated_at']


class searchSacoleirasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email']


class sacoleiraProductsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = product
        fields = ['id', 'sacoleira', 'image', 'description', 'name', 'value', 'size', 'quantity']
    

class productDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = product
        fields = ['id', 'image', 'description', 'name', 'value', 'size', 'quantity']
