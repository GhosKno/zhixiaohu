from rest_framework.response import Response as __resp
from rest_framework.viewsets import GenericViewSet as __View

from api.utils import mixins


def success(data=None, context=None):
    if data is not None:
        return __resp({'success': True, 'data': data})
    return __resp({'success': True})


def error(msg):
    return __resp({'success': False, 'msg': msg})


class GenericViewSet(__View):

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
                'Expected view %s to be called with a URL keyword argument '
                'named "%s". Fix your URL conf, or set the `.lookup_field` '
                'attribute on the view correctly.' %
                (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}

        obj = None
        try:
            obj = queryset.get(**filter_kwargs)
        except Exception:
            obj = None
        self.check_object_permissions(self.request, obj)
        return obj


class ReadOnlyModelViewSet(mixins.RetrieveModelMixin,
                           mixins.ListModelMixin,
                           GenericViewSet):
    pass


class ModelViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    pass


