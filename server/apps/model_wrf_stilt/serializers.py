from rest_framework import serializers

from .models import ModelWrfStilt, Receptor, Region


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"


class SimpleRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ["id", "name", "xmn", "xmx", "ymn", "ymx"]


class ReceptorSerializer(serializers.ModelSerializer):
    region = SimpleRegionSerializer(read_only=True)
    region_id = serializers.PrimaryKeyRelatedField(
        source="region", queryset=Region.objects.all(), write_only=True  # 指定写入目标字段
    )

    class Meta:
        model = Receptor
        fields = "__all__"


class ModelWRFStiltSerializer(serializers.ModelSerializer):

    class Meta:
        model = ModelWrfStilt
        fields = "__all__"
