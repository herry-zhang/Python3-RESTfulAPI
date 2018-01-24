from rest_framework import serializers
from apps.user.models import User
from apis.api_v1.enum import ErrorCode
from apis.api_v1.base import BaseApi


class GetUserSerializer(serializers.Serializer):
    """
    获取用户信息
    """
    token = serializers.CharField(max_length=150)
    user_id = serializers.IntegerField()

    def get_user(self, validated_data):
        result = dict()
        base_api = BaseApi()
        # 获取用户
        try:
            user = User.objects.get(user_id=validated_data["user_id"])
        except User.DoesNotExist:
            result["error_code"] = ErrorCode.用户不存在.value
            result["error"] = "用户不存在"
            return result
        # 认证
        if not base_api.authenticate_user(validated_data["token"], user.user_guid):
            result["error_code"] = ErrorCode.认证错误.value
            result["error"] = "认证错误"
            return result
        result["nick_name"] = user.user_name
        result["avatar"] = user.avatar
        result["error_code"] = ErrorCode.正确.value
        result["error"] = ""
        return result


