# coding=utf-8
from haystack import indexes
from models import gaoxin


class gaoxinIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return gaoxin

    def index_queryset(self, using=None):
        return self.get_model().objects.all()