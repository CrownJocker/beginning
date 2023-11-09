from rest_framework.pagination import PageNumberPagination
from rest_framework.request import Request


class BasePagination(PageNumberPagination):
    page_size_auery_param = 'page_size'
    max_page_size = '1000'

    def get_paginated_response(self, data):
        return Request({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'pages': self.page.paginator.num_pages,
            'results': data
        })