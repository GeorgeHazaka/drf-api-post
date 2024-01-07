from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from comments.models import Comment
from comment_likes.models import CommentLike


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model
    Adds extra fields when returning a list of Comment instances
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    comment_like_id = serializers.SerializerMethodField()
    comment_likes_count = serializers.ReadOnlyField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_comment_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            comment_like = CommentLike.objects.filter(
                owner=user, comment=obj
            ).first()
            return comment_like.id if comment_like else None
        return None

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'post', 'created_at',
            'updated_at', 'content', 'comment_likes_count',
            'comment_like_id', 'test',
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for the Comment model used in Detail view
    Post is a read only field so that we dont have to set it on each update
    """
    post = serializers.ReadOnlyField(source='post.id')
