from rest_framework import serializers
from .models import Profile, SystemUser


### Registratrion serializer....
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemUser
        fields = ('id','username','password','Name','Phone','email')
        extra_kwargs = {
            'password':{'write_only': True},
            'Phone':{'required':True},
            'email':{'required':True}
        }
    def create(self, validated_data):
        user = SystemUser.objects.create_user(validated_data['username'],password=validated_data['password'],email=validated_data['email'],Phone=validated_data['Phone'],Name=validated_data['Name'])
        user.save()
        return user


# User serializer....
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemUser
        fields = '__all__'
        extra_kwargs = {
          
            'Phone':{'required':True},
         
        }
### UserProfileserializer....
class UserProfileUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'
        extra_kwargs = {
          
            'user':{'read_only':True},
         
        }
       
###CustomUserSerializer.....
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemUser
        fields = ('username', 'email', 'password', 'bio', 'birth_date')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = SystemUser(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password is not None:
            instance.set_password(password)
        return super().update(instance, validated_data)
