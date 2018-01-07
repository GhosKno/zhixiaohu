from time import time

from qiniu import Auth
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from backend import settings
from utils.views import success


class ImageAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        #request.query_params['']
        q = Auth(settings.access_key,
                 settings.secret_key)
        file_name = str(time())
        token = q.upload_token(settings.bucket_name,
                               file_name,
                               3600)
        return success({'token': token})
