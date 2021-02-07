# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import, unicode_literals

import logging
from pprint import pprint

from weixin_open_api import WeixinOpenClient

weixin_open_api_logger = logging.getLogger("weixin-open-api")
weixin_open_api_logger.addHandler(logging.StreamHandler())


class CustomWeixinOpenClient(WeixinOpenClient):
    appid = ''
    secret = ''


if __name__ == '__main__':
    client = CustomWeixinOpenClient()
    ret = client.get_share_params(url='https://www.pjw.cn/download/app')
    pprint(ret)
