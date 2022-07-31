from rest_framework import serializers
from zarcosApp.models.user import User
from zarcosApp.models.orders import Orders
from zarcosApp.serializers.ordersSerializer import OrderSerializer

class UserSerializer(serializers.ModelSerializer):
    orders = OrderSerializer()
    class Meta:
        model = User
        fields = ['id', 'username','name', 'lastname', 'password', 'email','orders' ]
    def create(self, validated_data):
        ordersData = validated_data.pop('orders')
        userInstance = User.objects.create(**validated_data)
        Orders.objects.create(user=userInstance, **ordersData)
        return userInstance
    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        orders = Orders.objects.get(user=obj.id)
        return {
                    'id': user.id,
                    'username':user.name,
                    'name': user.name,
                    'lastname':user.lastname,
                    'email': user.email,
                    'orders': {
                        'id': orders.id,
                        'date': orders.date,
                        'totalsale': orders.totalsale,
                    
                    }
                    
                }