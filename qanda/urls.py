from django.urls import  path,include

from rest_framework.routers import DefaultRouter

from . views import QuestionViewSet,AnswerCreate,AnswerList,AnswerDeleteUpdate

router = DefaultRouter()
router.register('question',QuestionViewSet, basename='question')


urlpatterns = [
    path('', include(router.urls)),
    path('question/<slug:slug>/answercreate/', AnswerCreate.as_view()),
    path('question/<slug:slug>/answers/',AnswerList.as_view()),
    path('answers/<int:pk>/',AnswerDeleteUpdate.as_view()),
    
]
