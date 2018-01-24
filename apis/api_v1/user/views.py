import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apis.api_v1.user.serializers import *
from apis.api_v1.enum import ErrorCode


@api_view(['GET', 'POST'])
def user(request):
    """
    GET:获取用户信息
    POST:更新用户信息
    """
    if request.method == 'GET':
        param = dict()
        param["token"] = request.GET.get("token", None)
        param["user_id"] = request.GET.get("user_id", 0)
        serializer = GetUserSerializer(data=param)
        if serializer.is_valid():
            result = serializer.get_user(serializer.validated_data)
            return Response(result, status=status.HTTP_201_CREATED)
        return Response(dict(error_code=ErrorCode.参数错误.value, error=json.dumps(serializer.errors, ensure_ascii=False)), status=status.HTTP_400_BAD_REQUEST)
    # elif request.method == 'POST':
    #     serializer = PostUserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         result = serializer.update_user(serializer.validated_data)
    #         return Response(result, status=status.HTTP_201_CREATED)
    #     return Response(dict(error_code=ErrorCode.参数错误.value, error=json.dumps(serializer.errors, ensure_ascii=False)), status=status.HTTP_400_BAD_REQUEST)
