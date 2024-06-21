from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    """Пагинатор для вывода указанного определенного количества данных."""

    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = 15
