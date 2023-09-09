from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework.response import Response

from applications.account.utils import send_activation_code

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(required=True, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')

    def validate_email(self, email):
        return email

    def validate(self, attrs):
        password1 = attrs.get('password')
        password2 = attrs.pop('password2')

        if password1 != password2:
            raise serializers.ValidationError('Пароли не совпадают!!!')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        send_activation_code(user.email, user.activation_code)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)

    def validate_email(self, email):
        if User.objects.filter(email=email).exists(): # exists() -> [user1, user2] - queryset 
            return email
        raise serializers.ValidationError('Нет такого пользователя')
    
    def validate(self, attrs):
        user = authenticate(username=attrs.get('email'), password=attrs.get('password'))
        if not user:
            raise serializers.ValidationError('Неверный пароль!')
        attrs['user'] = user
        return attrs
    

