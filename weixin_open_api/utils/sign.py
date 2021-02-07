# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import, unicode_literals

import time
import random
import string
import hashlib


class Sign(object):
    """
    附录1-JS-SDK使用权限签名算法
    https://developers.weixin.qq.com/doc/offiaccount/OA_Web_Apps/JS-SDK.html#62
    """

    @classmethod
    def create_nonce_str(cls):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15))

    @classmethod
    def create_timestamp(cls):
        return int(time.time())

    @classmethod
    def get_signature(cls, params):
        text = '&'.join(['%s=%s' % (key.lower(), params[key]) for key in sorted(params)])
        return hashlib.sha1(text.encode()).hexdigest()

    @classmethod
    def sign(cls, jsapi_ticket, url):
        params = {
            'nonceStr': cls.create_nonce_str(),
            'jsapi_ticket': jsapi_ticket,
            'timestamp': cls.create_timestamp(),
            'url': url
        }

        params['signature'] = cls.get_signature(params)
        return params
