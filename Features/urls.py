from django.contrib import admin
from django.urls import path, re_path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Your Project API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="ankitbharti5478@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Define the request schema for registration and login
register_request_body = openapi.Schema(
    title='User Registration',
    type=openapi.TYPE_OBJECT,
    properties={
        'name': openapi.Schema(type=openapi.TYPE_STRING, description='User name'),
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='User email'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='User password'),
    },
    required=['name', 'email', 'password']
)

login_request_body = openapi.Schema(
    title='User Login',
    type=openapi.TYPE_OBJECT,
    properties={
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='User email'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='User password'),
    },
    required=['email', 'password']
)

# Define the response schema
success_response = openapi.Response(
    description='Operation was successful',
    schema=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'message': openapi.Schema(type=openapi.TYPE_STRING, description='Success message'),
            'token': openapi.Schema(type=openapi.TYPE_STRING, description='Authentication token'),
        },
    )
)

error_response = openapi.Response(
    description='Error response',
    schema=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'error': openapi.Schema(type=openapi.TYPE_STRING, description='Error message'),
        },
    )
)



# Define schemas for Question
question_request_body = openapi.Schema(
    title='Question',
    type=openapi.TYPE_OBJECT,
    properties={
        'text': openapi.Schema(type=openapi.TYPE_STRING, description='The text of the question'),
        'difficulty': openapi.Schema(type=openapi.TYPE_STRING, description='The difficulty level of the question'),
        # Add other fields as necessary
    },
    required=['text', 'difficulty']
)

question_response_body = openapi.Schema(
    title='Question Response',
    type=openapi.TYPE_OBJECT,
    properties={
        'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the question'),
        'text': openapi.Schema(type=openapi.TYPE_STRING, description='The text of the question'),
        'difficulty': openapi.Schema(type=openapi.TYPE_STRING, description='The difficulty level of the question'),
        # Add other fields as necessary
    }
)

# Define schemas for Question Paper
question_paper_request_body = openapi.Schema(
    title='Question Paper',
    type=openapi.TYPE_OBJECT,
    properties={
        'title': openapi.Schema(type=openapi.TYPE_STRING, description='Title of the question paper'),
        'questions': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_INTEGER), description='List of question IDs'),
        # Add other fields as necessary
    },
    required=['title', 'questions']
)

question_paper_response_body = openapi.Schema(
    title='Question Paper Response',
    type=openapi.TYPE_OBJECT,
    properties={
        'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='ID of the question paper'),
        'title': openapi.Schema(type=openapi.TYPE_STRING, description='Title of the question paper'),
        'questions': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_INTEGER), description='List of question IDs'),
        # Add other fields as necessary
    }
)




urlpatterns = [
    path('admin/', admin.site.urls),
    # ... your other URL patterns
    path('user/',include("Users.urls")),
    path('',include("Assesment.urls")),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),
]
