from django.contrib.auth.models import User, Group
from nodes.models import Node, Activity
from rest_framework import serializers, viewsets


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class NodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Node
        fields = (
            'name',
            'mac_address',
            'ip_address',
            'registered_since',
            'last_active',
            'signal_strength',
            'battery_status',
            'is_soft_deleted',
            'info_string',
        )


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        fields = ('node', 'datetime', 'value')
