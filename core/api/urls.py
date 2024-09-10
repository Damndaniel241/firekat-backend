from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'topics', TopicViewSet)
router.register(r'comments',CommentViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'faculties', FacultyViewSet)
urlpatterns = [
    path('topics/all/',CountTopicsView.as_view()),
    path('',include(router.urls)),
]

# This setup will give you the following endpoints for the Topic model:

# GET /topics/: List all topics.
# POST /topics/: Create a new topic.
# GET /topics/{id}/: Retrieve a specific topic.
# PUT /topics/{id}/: Update a specific topic.
# DELETE /topics/{id}/: Delete a specific topic.
# These endpoints will allow you to perform all standard CRUD operations on the Topic model using the DRF API.




# curl -X PUT -H "Authorization: Token a5540036d1339fca45696a403550bc0e7c934e55" \
# -H "Content-Type: application/json" \
# -d '{"title": "Updated Title", "content": "Updated content"}' \
# http://127.0.0.1:8000/api/topics/1/


# Explanation:
# -X PUT: Specifies that the HTTP method used is PUT.
# -H "Authorization: Token ...": Includes the token in the Authorization header for authentication.
# -H "Content-Type: application/json": Sets the Content-Type header to application/json to inform the server that the data being sent is in JSON format.
# -d '{"title": "Updated Title", "content": "Updated content"}': Specifies the data to update. This should be a JSON object that includes the fields you want to modify.
# The URL http://127.0.0.1:8000/api/topics/1/ targets the specific resource you want to update.


### `POST` Request using `curl`

# A `POST` request is used to create a new resource. Here's how you can perform a `POST` request using `curl`:

# ```bash
# curl -X POST -H "Authorization: Token a5540036d1339fca45696a403550bc0e7c934e55" \
# -H "Content-Type: application/json" \
# -d '{
#     "title": "New Topic",
#     "content": "This is a new topic content",
#     "subject": 1,
#     "author": 2
# }' \
# http://127.0.0.1:8000/api/topics/
# ```

# ### Explanation:

# - `-X POST`: Specifies that the HTTP method is `POST`.
# - `-d '{ ... }'`: The JSON data that represents the new resource to be created. Ensure that all required fields (e.g., `title`, `content`, `subject`, `author`) are included.

# ### `PATCH` Request using `curl`

# A `PATCH` request is used to update part of a resource. Here's how to perform a `PATCH` request:

# ```bash
# curl -X PATCH -H "Authorization: Token a5540036d1339fca45696a403550bc0e7c934e55" \
# -H "Content-Type: application/json" \
# -d '{
#     "content": "Updated content for the topic"
# }' \
# http://127.0.0.1:8000/api/topics/1/
# ```

# ### Explanation:

# - `-X PATCH`: Specifies that the HTTP method is `PATCH`.
# - `-d '{ ... }'`: The JSON data that includes only the fields you want to update. In this case, only the `content` field is being updated.

# ### Example Summary:

# - **`POST`**: Used to create a new resource (e.g., a new topic).
# - **`PATCH`**: Used to partially update a resource (e.g., updating just the content of a topic).
# - **`PUT`**: Used to completely update a resource (e.g., replacing the entire content of a topic).


# This setup will give you a full set of RESTful endpoints for the Subject model:

# GET /api/subjects/: List all subjects.
# POST /api/subjects/: Create a new subject.
# GET /api/subjects/<id>/: Retrieve a specific subject by its ID.
# PUT /api/subjects/<id>/: Update a specific subject by its ID.
# PATCH /api/subjects/<id>/: Partially update a specific subject by its ID.
# DELETE /api/subjects/<id>/: Delete a specific subject by its ID




# FacultyViewSet(viewsets.ModelViewSet): This defines a Django Rest Framework (DRF) 
# viewset that provides all the standard actions 
# (list, create, retrieve, update, partial_update, destroy) for the Faculty model.