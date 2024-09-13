from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .assesment_service import QuestionService,QuestionPaperService
from .serializers import QuestionSerializer
from .serializers import QuestionPaperSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from Features.urls import *
class QuestionListAPIView(APIView):
    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description='List of questions',
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Items(type=openapi.TYPE_OBJECT, properties={
                        'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'text': openapi.Schema(type=openapi.TYPE_STRING),
                        'difficulty': openapi.Schema(type=openapi.TYPE_STRING),
                    })
                )
            )
        }
    )
    def get(self, request):
        questions = QuestionService.get_all_questions()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data, status=200)

    @swagger_auto_schema(
        request_body=question_request_body,
        responses={
            201: openapi.Response(
                description='Question created successfully',
                schema=question_response_body
            ),
            400: openapi.Response(description='Invalid input', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={'error': openapi.Schema(type=openapi.TYPE_STRING)}))
        }
    )
    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            question = QuestionService.create_question(serializer.validated_data)
            return Response(QuestionSerializer(question).data, status=201)
        return Response(serializer.errors, status=400)

class QuestionDetailAPIView(APIView):
    @swagger_auto_schema(
        responses={
            200: question_response_body,
            404: openapi.Response(description='Question not found', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={'error': openapi.Schema(type=openapi.TYPE_STRING)}))
        }
    )
    def get(self, request, question_id):
        question = QuestionService.get_question_by_id(question_id)
        if question:
            serializer = QuestionSerializer(question)
            return Response(serializer.data, status=200)
        return Response({"error": "Question not found."}, status=404)

    @swagger_auto_schema(
        request_body=question_request_body,
        responses={
            200: question_response_body,
            400: openapi.Response(description='Invalid input', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={'error': openapi.Schema(type=openapi.TYPE_STRING)})),
            404: openapi.Response(description='Question not found', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={'error': openapi.Schema(type=openapi.TYPE_STRING)}))
        }
    )
    def put(self, request, question_id):
        question = QuestionService.get_question_by_id(question_id)
        if question:
            serializer = QuestionSerializer(question, data=request.data)
            if serializer.is_valid():
                updated_question = QuestionService.update_question(question, serializer.validated_data)
                return Response(QuestionSerializer(updated_question).data, status=200)
            return Response(serializer.errors, status=400)
        return Response({"error": "Question not found."}, status=404)

    @swagger_auto_schema(
        responses={
            204: openapi.Response(description='Question deleted successfully'),
            404: openapi.Response(description='Question not found', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={'error': openapi.Schema(type=openapi.TYPE_STRING)}))
        }
    )
    def delete(self, request, question_id):
        question = QuestionService.get_question_by_id(question_id)
        if question:
            QuestionService.delete_question(question)
            return Response({"message": "Question deleted successfully."}, status=204)
        return Response({"error": "Question not found."}, status=404)

class QuestionPaperListAPIView(APIView):
    @swagger_auto_schema(
        responses={
            200: openapi.Response(
                description='List of question papers',
                schema=openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Items(type=openapi.TYPE_OBJECT, properties={
                        'id': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'title': openapi.Schema(type=openapi.TYPE_STRING),
                        'questions': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_INTEGER)),
                    })
                )
            )
        }
    )
    def get(self, request):
        question_papers = QuestionPaperService.get_all_question_papers()
        serializer = QuestionPaperSerializer(question_papers, many=True)
        return Response(serializer.data, status=200)

    @swagger_auto_schema(
        request_body=question_paper_request_body,
        responses={
            201: openapi.Response(
                description='Question paper created successfully',
                schema=question_paper_response_body
            ),
            400: openapi.Response(description='Invalid input', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={'error': openapi.Schema(type=openapi.TYPE_STRING)}))
        }
    )
    def post(self, request):
        serializer = QuestionPaperSerializer(data=request.data)
        if serializer.is_valid():
            question_paper = QuestionPaperService.create_question_paper(serializer.validated_data)
            return Response(QuestionPaperSerializer(question_paper).data, status=201)
        return Response(serializer.errors, status=400)

class QuestionPaperDetailAPIView(APIView):
    @swagger_auto_schema(
        responses={
            200: question_paper_response_body,
            404: openapi.Response(description='Question paper not found', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={'error': openapi.Schema(type=openapi.TYPE_STRING)}))
        }
    )
    def get(self, request, paper_id):
        question_paper = QuestionPaperService.get_question_paper_by_id(paper_id)
        if question_paper:
            serializer = QuestionPaperSerializer(question_paper)
            return Response(serializer.data, status=200)
        return Response({"error": "Question paper not found."}, status=404)

    @swagger_auto_schema(
        request_body=question_paper_request_body,
        responses={
            200: question_paper_response_body,
            400: openapi.Response(description='Invalid input', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={'error': openapi.Schema(type=openapi.TYPE_STRING)})),
            404: openapi.Response(description='Question paper not found', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={'error': openapi.Schema(type=openapi.TYPE_STRING)}))
        }
    )
    def put(self, request, paper_id):
        question_paper = QuestionPaperService.get_question_paper_by_id(paper_id)
        if question_paper:
            serializer = QuestionPaperSerializer(question_paper, data=request.data)
            if serializer.is_valid():
                updated_question_paper = QuestionPaperService.update_question_paper(question_paper, serializer.validated_data)
                return Response(QuestionPaperSerializer(updated_question_paper).data, status=200)
            return Response(serializer.errors, status=400)
        return Response({"error": "Question paper not found."}, status=404)

    @swagger_auto_schema(
        responses={
            204: openapi.Response(description='Question paper deleted successfully'),
            404: openapi.Response(description='Question paper not found', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={'error': openapi.Schema(type=openapi.TYPE_STRING)}))
        }
    )
    def delete(self, request, paper_id):
        question_paper = QuestionPaperService.get_question_paper_by_id(paper_id)
        if question_paper:
            QuestionPaperService.delete_question_paper(question_paper)
            return Response({"message": "Question paper deleted successfully."}, status=204)
        return Response({"error": "Question paper not found."}, status=404)
