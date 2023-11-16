from django.urls import path
from .views import Quiz, RandomQuestionTopic, StartQuiz, QuizQuestions
from django.conf import settings
from django.conf.urls.static import static

app_name='quiz'

urlpatterns = [
    path('', Quiz.as_view(), name='quiz'),
    path('q/<str:topic>/', QuizQuestions.as_view(), name='questions'),
    # #path('a/', Answer.as_view(), name='answer'),
    path('r/<str:topic>/', RandomQuestionTopic.as_view(), name='RandomQuestionTopic'),
    path('single/<str:title>/', StartQuiz.as_view(), name='quiz'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)