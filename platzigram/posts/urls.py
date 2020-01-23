from django.urls import path
from posts import views

urlpatterns=[path(  route='',
                    view=views.list_posts,
                    name='feed'
                 ),

            path(   route='new/',
                    view=views.new_post,
                    name='new'
                ),
        ]
