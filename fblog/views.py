#!/usr/bin/env python
# encoding: utf-8

from django.http import HttpResponse
import qrcode
from cStringIO import StringIO
from django.shortcuts import render
from .models import Article,Category,Tag
from django.shortcuts import render_to_response
from django.views.generic import ListView, DetailView
import markdown2


# Create your views here.

#def index(request):
#    blog_list = BlogsPost.objects.all()
#    string = u"我在自强学堂学习Django，用它来建网站"
#    TutorialList = ["HTML", "CSS", "jQuery", "Python", "Django"]
#    return render(request, 'fblog\index.html', {'blog_list': blog_list})
#    return render(request, 'fblog\index.html', {'string': string})
#    return render_to_response('fblog\index.html',{'blog_list':blog_list})
class blogindex(ListView):
    model = Article
    template_name = "fblog\index.html"
    context_object_name = 'Blogs'

    def get_queryset(self):
        Blogs = Article.objects.filter(status='p')
        for article in Blogs:
            article.body = markdown2.markdown(article.body, extras=['fenced-code-blocks'], )
        return Blogs

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        kwargs['date_archive'] = Article.objects.archive()
        kwargs['tag_list'] = Tag.objects.all().order_by('name')
        kwargs['body_limit']=Article.objects.all()[:1]
        return super(blogindex, self).get_context_data(**kwargs)

class ArticleDetailView(DetailView):
    model = Article
    template_name = "fblog/detail.html"
    context_object_name = "blogtext"
    pk_url_kwarg = 'article_id'

    def get_object(self, queryset=None):
        obj = super(ArticleDetailView, self).get_object()
        obj.body = markdown2.markdown(obj.body, extras=['fenced-code-blocks'], )
        return obj

class CategoryView(ListView):
    template_name = "fblog/index.html"
    context_object_name = "article_list"

    def get_queryset(self):
        article_list = Article.objects.filter(category=self.kwargs['cate_id'], status='p')
        for article in article_list:
            article.body = markdown2.markdown(article.body, extras=['fenced-code-blocks'], )
        return article_list

    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        return super(CategoryView, self).get_context_data(**kwargs)




def test(request):
    return render(request,'fblog/testqd.html')


def generate_qrcode(request, data):
    img = qrcode.make(data)

    buf = StringIO()
    img.save(buf)
    image_stream = buf.getvalue()

    response = HttpResponse(image_stream, content_type="image/png")
    response['Last-Modified'] = 'Mon, 27 Apr 2015 02:05:03 GMT'
    response['Cache-Control'] = 'max-age=31536000'
    return response

