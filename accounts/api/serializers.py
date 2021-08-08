from rest_framework import serializers
from ..models import User
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):

    """
    Serializes user data - first_name, last_name, email, token,
                            age, DoB, Phone Number
    """

    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "token",
            "age",
            "date_of_birth",
            "phone_number",
        )

    def get_token(self, value):
        refresh = RefreshToken.for_user(value)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }


class RegisterSerializer(serializers.ModelSerializer):

    """
    Serializes User Registration data
    """

    password = serializers.CharField(
        style={"input_type": "password"}, write_only=True
    )
    password2 = serializers.CharField(
        style={"input_type": "password"}, write_only=True
    )
    message = serializers.SerializerMethodField(read_only=True)
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "password2",
            "message",
            "age",
            "date_of_birth",
            "phone_number",
            "token",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def get_message(self, obj):
        return "Thank you for registering. You can now log in now."

    def get_token(self, value):
        refresh = RefreshToken.for_user(value)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

    def validate_email(self, value):
        qs = User.objects.filter(email__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(
                "User with this email already exists"
            )
        return value

    def validate(self, data):
        pw = data.get("password")
        pw2 = data.pop("password2")
        if pw != pw2:
            raise serializers.ValidationError("Passwords must match")
        return data

    def create(self, validated_data):
        user_obj = User.objects.create(
            first_name=validated_data.get("first_name"),
            last_name=validated_data.get("last_name"),
            email=validated_data.get("email"),
            age=validated_data.get("age"),
            date_of_birth=validated_data.get("date_of_birth"),
            phone_number=validated_data.get("phone_number"),
        )
        user_obj.set_password(validated_data.get("password"))
        user_obj.save()
        return user_obj
