# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import, unicode_literals

from session_request import SessionRequest
from .logger import logger


class WeixinOpenAPi(SessionRequest):
    """
    微信请求接口
    """
    BASE_URL = 'https://api.weixin.qq.com/cgi-bin'

    def __init__(self, **kwargs):
        super(WeixinOpenAPi, self).__init__(self.BASE_URL, **kwargs)

    def after_request(self, response):
        logger.debug(response.content)
        res = response.json()
        return res

    def token(self, appid, secret):
        """
        获取 access_token
        (有效期7200秒，开发者必须在自己的服务全局缓存access_token）

        https://developers.weixin.qq.com/doc/offiaccount/Basic_Information/Get_access_token.html
        :param appid: 第三方用户唯一凭证
        :param secret: 第三方用户唯一凭证密钥，即appsecret
        :return:
        """
        options = {
            'path': '/token',
            'params': {
                'grant_type': 'client_credential',
                'appid': appid,
                'secret': secret

            }
        }

        return self.get(**options)

    def ticket_getticket(self, access_token, type='jsapi'):
        """
        获得jsapi_ticket
        （有效期7200秒，开发者必须在自己的服务全局缓存jsapi_ticket）
        :param access_token:
        :param type:
        :return:
        """
        options = {
            'path': '/ticket/getticket',
            'params': {
                'access_token': access_token,
                'type': type,
            }
        }

        return self.get(**options)
