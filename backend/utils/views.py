from rest_framework.views import APIView as _View
from rest_framework.response import Response as _res


class APIView(_View):
    def success(self, data=None):
        if data is None:
            return _res({
                'success': True
            })
        return _res({
            'success': True,
            'data': data
        })

    def error(self, msg):
        return _res({
            'success': False,
            'msg': msg
        })