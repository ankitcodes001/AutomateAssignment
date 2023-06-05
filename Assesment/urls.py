from django.urls import path
from .views import QuestionListAPIView, QuestionDetailAPIView
from .views import QuestionPaperListAPIView, QuestionPaperDetailAPIView


urlpatterns = [
    path('api/questions/', QuestionListAPIView.as_view(), name='question-list'),
    path('api/questions/<int:question_id>/', QuestionDetailAPIView.as_view(), name='question-detail'),
    path('api/questionpapers/', QuestionPaperListAPIView.as_view(), name='question-paper-list'),
    path('api/questionpapers/<int:paper_id>/', QuestionPaperDetailAPIView.as_view(), name='question-paper-detail'),

]
