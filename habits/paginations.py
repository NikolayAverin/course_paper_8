from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    """Вывод 5 привычек на страницу, максимальный вывод 50 привычек"""

    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 50
