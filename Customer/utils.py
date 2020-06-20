from kavenegar import *
import urllib.parse

api_key = ''


def send_sms(to, template, context):
    print(urllib.parse.quote(context))
    try:
        import json
    except ImportError:
        import simplejson as json
    try:
        api = KavenegarAPI(api_key)
        params = {
            # 'sender': '10004346',
            'receptor': to,
            'message': urllib.parse.quote(context),
        }

        response = api.sms_send(params)
        print(str(response))
    except APIException as e:
        print(str(e.__doc__))
        print(str(e))
        print(urllib.parse.unquote(str(e)))
    except HTTPException as e:
        print(str(e))
