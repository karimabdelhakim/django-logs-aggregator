from rest_framework import serializers

from logs.models import Log


class CreateLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ('server_name', 'type', 'message', 'text')

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        server_name = validated_data.get('server_name')
        type = validated_data.get('type')
        message = validated_data.get('message')
        text = validated_data.get('text')
        log_obj = Log(server_name=server_name, type=type,
                      message=message, text=text)
        log_obj.user = user
        log_obj.save()
        return log_obj
