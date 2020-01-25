from django.urls import path
from posts import views

urlpatterns=[path(  route='',
                    view=views.PostFeedView.as_view(),
                    name='feed'
                 ),

            path(   route='new/',
                    view=views.CreatePostView.as_view(),
                    name='new'
                ),
                path(   route='detail/<int:pk>',
                        view=views.PostDetailView.as_view(),
                        name='posts_detail'
                    ),
        ]
