from django.contrib.auth.models import User
from rest_framework import serializers


class RegisterUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField(max_length=150, min_length=10)
    password = serializers.CharField(max_length=100, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'username', 'password')

    def validate(self, args):
        username = args.get('username', None)
        email = args.get('email', None)
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'Email': ('email already exists')})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({'Username': ('username already exists')})

        return super().validate(args)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save(update_fields=['password'])
        return user
