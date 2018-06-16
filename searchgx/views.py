# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'searchgx/index.html')


from haystack.views import SearchView
class MySearchView(SearchView):
    def extra_context(self):
        context = super(MySearchView,self).extra_context()
        context['title'] = '搜索'
        context['guest_cart'] = 1
        context['cart_count'] = cart_count(self.request)
        return context