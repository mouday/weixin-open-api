# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import, unicode_literals

from .utils.sign import Sign
from .weixin_open_api import WeixinOpenAPi
from mo_cache import FileCache


class WeixinOpenClient(WeixinOpenAPi):
    # 开发者ID(AppID)
    appid = ''

    # 开发者密码(AppSecret)
    secret = ''

    def __init__(self, cache=None, **kwargs):
        super(WeixinOpenClient, self).__init__(**kwargs)
        self.cache = cache or FileCache()

    def get_access_token_cache_key(self):
        """缓存access_token key """
        return 'weixin_open.access_token.' + self.appid

    def get_jsapi_ticket_cache_key(self):
        """缓存jsapi_ticket key """
        return 'weixin_open.jsapi_ticket.' + self.appid

    def get_access_token(self):
        """对access_token进行缓存"""

        access_token_cache_key = self.get_access_token_cache_key()

        @self.cache(key=access_token_cache_key, expire=7200)
        def decorator():
            res = super(WeixinOpenClient, self).token(appid=self.appid, secret=self.secret)
            return res['access_token']

        return decorator()

    def get_jsapi_ticket(self):
        """对jsapi_ticket进行缓存"""

        access_token = self.get_access_token()

        jsapi_ticket_cache_key = self.get_jsapi_ticket_cache_key()

        @self.cache(key=jsapi_ticket_cache_key, expire=7200)
        def decorator():
            res = super(WeixinOpenClient, self).ticket_getticket(access_token=access_token, type='jsapi')
            return res['ticket']

        return decorator()

    def get_share_params(self, url):
        """
        :param url:
        :return:
        eg:
        {
            'nonceStr': '6dUStASaa9AE25L',
            'jsapi_ticket': 'LIKLckvwlJT9cWIhEQTwfK94S5h_Bg0fYWcNDaWnWfa6rwRWExu7s6EvcEyYLzvZdy3Cc8xY4BeteAvpSwvNCw',
            'timestamp': 1602467765,
            'url': 'https://t.345678.org/',
            'signature': '1df3593c7d409f6e0ee5c95f2406256575bab9eb'
        }
        """
        return Sign.sign(self.get_jsapi_ticket(), url)
