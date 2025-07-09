import requests
# client_id, authorize_code 노출 주의, 실제 값은 임시로만 넣고 Git에 올라가지 않도록 유의

client_id = '1377c40d1eb13eb53cfa54bc3d60aa7b'
redirect_uri = 'https://example.com/oauth'
authorize_code = 's7zgKYaf_O0II46GvCdtRYc1dFYiL8FeEkSTp_hc9EHB6o5HKSGawwAAAAQKDSAbAAABl4sF6DktjdRiIM79qQ'


token_url = 'https://kauth.kakao.com/oauth/token'
data = {
    'grant_type': 'authorization_code',
    'client_id': client_id,
    'redirect_uri': redirect_uri,
    'code': authorize_code,
    }

response = requests.post(token_url, data=data)
tokens = response.json()
print(tokens)
