import hashlib
from apis.api_v1.setting import IS_TEST, APP_VERIFY_CODE


class BaseApi(object):
    
    def authenticate(self, token):
        """
        认证
        """
        if IS_TEST:
            return True
        elif not IS_TEST and self.md5(APP_VERIFY_CODE) == token:
            return True
        return False

    def authenticate_user(self, token, guid):
        """
        登录用户认证
        """
        if IS_TEST:
            return True
        elif not IS_TEST and self.md5(APP_VERIFY_CODE + guid) == token:
            return True
        return False

    def md5(self, str):
        """
        MD5加密
        """
        m = hashlib.md5()
        m.update(str.encode("utf8"))
        return m.hexdigest()

    def is_in_enum(self, eunm, key=None, value=None):
        """
        判断是否为枚举值的元素
        """
        for name, member in eunm.__members__.items():
            if key is not None and name == key or value is not None and value == member.value:
                return True
        return False
