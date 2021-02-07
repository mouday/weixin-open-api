# weixin-open-api

![PyPI](https://img.shields.io/pypi/v/weixin-open-api.svg)
![PyPI - Downloads](https://img.shields.io/pypi/dm/weixin-open-api)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/weixin-open-api)
![PyPI - License](https://img.shields.io/pypi/l/weixin-open-api)


微信开放部分接口Python封装

Github: https://github.com/mouday/weixin-open-api

## 已实现：

1. 微信分享必要参数



## install
 
```bash
pip install weixin-open-api
```

`access_token` 默认使用了 [mo-cache](https://pypi.org/project/mo-cache/) 的FileCache文件缓存

## demo

```python
from weixin_open_api import WeixinOpenClient


class CustomWeixinOpenClient(WeixinOpenClient):
    appid = ''
    
    secret = ''

if __name__ == '__main__':
    client = CustomWeixinOpenClient()
    data = client.get_share_params(url='https://www.baidu.cn/app')
    print(data)
```
