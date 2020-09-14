### jwt加密解密

```
import jwt
import time


class JwtToken:
    def JwtEncode(self, phone):
        issued_at = int(time.time())
        token_dict = {
            'iat': issued_at,
            'name': phone,  # 用户的手机号
            'exp': issued_at + 1200,  # 过期时间
            'iss': "shumei123"
        }

        jwt_token = jwt.encode(token_dict,  # payload, 有效载体
                               'secret',
                               algorithm="HS256",  # 指明签名算法方式, 默认也是HS256
                               )
        return jwt_token

    def JwtDecode(self, token):
        result = jwt.decode(token, 'secret', issuer='shumei123', algorithms=['HS256'])
        return result


token = JwtToken()
entry = token.JwtEncode("15527433582")
detry = token.JwtDecode(entry)
print(entry)
print(detry)
```

