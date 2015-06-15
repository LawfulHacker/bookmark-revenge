from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastypie.constants import ALL

from .models import Bookmark


class BookmarkResource(ModelResource):
    class Meta:
        queryset = Bookmark.objects.all()
        resource_name = 'bookmark'
        filtering = {
            'url': ('exact'),
            'title': ALL,
            'tags': ('contains')
        }

    def dehydrate_tags(self, bundle):
        return bundle.obj.tags

    def build_filters(self, filters=None):
        ModelResource.build_filters(filters)
        print(filters)