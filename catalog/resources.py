from tastypie.resources import ModelResource
from .models import Book


class BookResource(ModelResource):
    class Meta:
        queryset = Book.objects.all()
        resource_name = 'book'
        fields = ['isbn', 'title', 'summary'] # 設定顯示欄位
        allowed_methods = ['get']

book_resource = BookResource() # 建立API資源
