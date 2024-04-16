import requests
import json

API_KEY = "uozMl6O310y9lUeL855cONi3"
SECRET_KEY = "KuQwQKes8e2eM8EwmTiqCyMYO6yxSiWO"


def method():
    url = ("https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?charset=KuQwQKes8e2eM8EwmTiqCyMYO6yxSiWO"
           "&access_token=") + get_access_token()

    payload = json.dumps({
        "text": "我通常会等待切达干酪版本降至 6.00 "
                "美元左右（更宽的面条），但已经过了一分钟.所以我试着用这些来支撑我。第一口（勺子/叉子/什么）就像“天哪，当他们说辣时，他们不是在开玩笑”，到最后一口..“我必须再做一次..就像现在一样“!!"
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


# if __name__ == '__main__':
#     main()
