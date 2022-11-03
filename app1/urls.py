from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('form_handler', views.index, name='form_handler'),
    path('blog', views.blog, name='blogs'),
    path('contact', views.contact, name='contact'),
    path('gallery', views.gallery, name='gallery'),
    path('render_blog/blog=<name>/?', views.render_blog, name='render_blog'),
    path('catogory_blog/<catogory>/?', views.blogfilter, name='blogfilter'),
    path(r'product_view/<name>/?/<title>/?/$', views.product_view, name='product_view'),
]
