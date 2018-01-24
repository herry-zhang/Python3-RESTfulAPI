from enum import Enum, unique


@unique
class ErrorCode(Enum):
    # base
    正确 = 0
    参数错误 = 1
    请求方法错误 = 2
    认证错误 = 3
    # user
    微信登录凭证错误 = 1000
    用户不存在 = 1001
    获取微信用户信息错误 = 1002
    账户余额不足 = 1003
    推送状态不正确 = 1004
