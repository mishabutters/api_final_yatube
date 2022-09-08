from django.shortcuts import get_object_or_404
from posts.models import Post, Group, Comment, Follow
from rest_framework import filters, mixins, viewsets, permissions
from rest_framework.pagination import LimitOffsetPagination

from .permissions import IsOwnerOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    ]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_pagination_class(self):
        if self.request.query_params.get("limit"):
            return LimitOffsetPagination
        return None

    pagination_class = property(fget=get_pagination_class)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsOwnerOrReadOnly]


class FollowViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = (filters.SearchFilter,)
    search_fields = ("following__username",)

    def get_queryset(self):
        new_queryset = Follow.objects.filter(user=self.request.user)
        return new_queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    ]
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get("post_id")
        new_queryset = Comment.objects.filter(post=post_id)
        return new_queryset

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get("post_id"))
        serializer.save(author=self.request.user, post=post)
