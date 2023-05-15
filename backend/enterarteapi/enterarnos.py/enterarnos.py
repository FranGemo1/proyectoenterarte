from rest_framework import enterarnos
from ..models import usuarios

class usuariosEnterarnos(enterarnos.ModelEnterarnos):
    class Meta:
        model = usuarios
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = usuarios(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
