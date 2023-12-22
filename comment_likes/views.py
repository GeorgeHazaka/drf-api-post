from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import CommentLike
from .serializers import CommentLikeSerializer


class CommentLikeList(generics.ListCreateAPIView):
    """
    List comment_likes or create a comment_like if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CommentLikeSerializer
    queryset = CommentLike.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentLikeDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a comment_like or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentLikeSerializer
    queryset = CommentLike.objects.all()
