from django.urls import path

#import py func from views file!
from . import views

#after /blog should be there, then others!
app_name = 'blog'

urlpatterns = [
    path("",views.index,name="index"),

    #dynamic url, if int but string is given in url, then it wont work!
    path("post/<int:post_id>",views.detail,name="detail"),

    #new url path
    path("new_url",views.new_url_view,name="new_page_url"),
    #old url path
    path("old_url",views.old_url_redirect,name="old_url")
]
