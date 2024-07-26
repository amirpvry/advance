from rest_framework import serializers
from blog.models import Post, Categories
from accounts.models import Profile


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ["name"]


class PostSerializer(serializers.ModelSerializer):

    related_url = serializers.URLField(source="get_absolute_api_url", read_only=True)
    absolute_api_url = serializers.SerializerMethodField(method_name="get_abs_api_url")

    class Meta:

        model = Post
        fields = [
            "id",
            "author",
            "title",
            "image",
            "content",
            "create_date",
            "categories",
            "status",
            "related_url",
            "absolute_api_url",
        ]
        read_only_fields = ["content", "author"]

    def get_abs_api_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.pk)

    def to_representation(self, instance):
        request = self.context.get("request")
        rep = super().to_representation(instance)
        if request.parser_context.get("kwargs").get("pk"):
            rep.pop("related_url")
            rep.pop("absolute_api_url")

        else:
            rep.pop("content")

        rep["categories"] = CategorySerializer(instance.categories).data

        return rep

    def create(self, validated_data):
        validated_data["author"] = Profile.objects.get(
            user__id=self.context.get("request").user.id
        )
        return super().create(validated_data)
