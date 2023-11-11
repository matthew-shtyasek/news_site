from django.http import JsonResponse
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.views import APIView

from news.models import News
from news.serializers import NewsSerializer


class NewsListApiView(ListAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()


class NewsDetailApiView(APIView):
    serializer_class = NewsSerializer
    model = News

    def get_queryset(self, request, id):
        return get_object_or_404(News, id=id)

    def get(self, request, id):
        return JsonResponse(
            self.serializer_class(
                self.get_queryset(request, id)
            ).data
        )
