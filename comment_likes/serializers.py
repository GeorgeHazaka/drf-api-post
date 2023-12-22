from django.db import IntegrityError
from rest_framework import serializers
from comment_likes.models import CommentLike


class CommentLikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the CommentLike model
    The create method handles the unique constraint on 'owner' and 'comment'
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = CommentLike
        fields = ['id', 'created_at', 'owner', 'comment']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
