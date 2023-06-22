from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = User.objects.filter(username=username).first()

        if user is None or not user.check_password(password):
            raise serializers.ValidationError('Invalid username or password')

        refresh = RefreshToken.for_user(user)

        attrs['refresh'] = str(refresh)
        attrs['access'] = str(refresh.access_token)

        return attrs


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True},  # Thuộc tính bổ sung: chỉ cho phép ghi dữ liệu
                        'email': {'required': True},  # Thuộc tính bổ sung: yêu cầu dữ liệu}
                        }
