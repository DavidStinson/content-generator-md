# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Django REST Framework Lab

| Title | Type | Duration | Author |
|-------|------|----------|--------|
| Building a RESTful API with Django REST Framework | Lab | 10 hours | John Doe |

### Learning Objectives

- Build a functional Django REST Framework application
- Implement key features of Django REST Framework, including serializers, views, and routing
- Understand and apply best practices for building RESTful APIs
- Test and debug a Django REST Framework implementation

#### Day 1: Project Setup and Models

**Estimated Time: 2 hours**

In this lab, we'll be building a RESTful API for a simple blog application using Django REST Framework (DRF). The application will have two models: `Post` and `Comment`.

1. Set up a new Django project and app.
2. Create the `Post` model with the following fields:
   - `title` (CharField)
   - `content` (TextField)
   - `author` (ForeignKey to Django's built-in `User` model)
   - `created_at` (DateTimeField, auto_now_add=True)
   - `updated_at` (DateTimeField, auto_now=True)

3. Create the `Comment` model with the following fields:
   - `content` (TextField)
   - `author` (ForeignKey to `User`)
   - `post` (ForeignKey to `Post`)
   - `created_at` (DateTimeField, auto_now_add=True)
   - `updated_at` (DateTimeField, auto_now=True)

4. Register the models in the Django admin interface.

#### Day 2: Serializers and Views

**Estimated Time: 3 hours**

Today, we'll create serializers and views for our models, allowing us to interact with the data through a RESTful API.

1. Create serializers for the `Post` and `Comment` models using DRF's `ModelSerializer`.
   - The `PostSerializer` should include nested comments.
   - The `CommentSerializer` should include a read-only field for the author's username.

2. Create views for the `Post` model:
   - `PostListView` (ListView)
   - `PostDetailView` (RetrieveUpdateDestroyAPIView)

3. Create views for the `Comment` model:
   - `CommentListView` (ListCreateAPIView)
   - `CommentDetailView` (RetrieveUpdateDestroyAPIView)

4. Test the views using Django's built-in test client or a tool like Postman.

![Postman Interface](https://i.imgur.com/4KSXQFE.png)

#### Day 3: Routing and Authentication

**Estimated Time: 3 hours**

Today, we'll set up routing for our views and implement authentication and authorization.

1. Configure URL routing for the views using DRF's `DefaultRouter`.
2. Implement token-based authentication for the API using DRF's `TokenAuthentication`.
   - Create a custom `UserSerializer` to handle user creation and updating.
   - Create views for user registration and token retrieval.

3. Implement permission classes to control access to the API:
   - `IsAuthenticated` for views that require authentication
   - `IsAuthenticatedOrReadOnly` for views that allow read access to unauthenticated users

4. Test the authentication and authorization by making requests with and without authentication headers.

![Django REST Framework Authentication Flow](https://i.imgur.com/8UKzxOV.png)

#### Day 4: Advanced Features and Testing

**Estimated Time: 2 hours**

On the final day, we'll explore some advanced features of DRF and implement testing for our API.

1. Implement pagination for the `PostListView` using DRF's `PageNumberPagination`.
2. Add filtering and searching capabilities to the `PostListView` using DRF's `FilterSet` and `SearchFilter`.
3. Write unit tests for the serializers and views using Django's built-in testing framework.
4. Write integration tests to ensure the API endpoints are working as expected.

#### Submission Instructions

1. Push your code to a GitHub repository and submit the link.
2. Include a README file with instructions on how to set up and run the project locally.
3. Optionally, you can deploy your application to a hosting service like Heroku or PythonAnywhere and include the live URL in the README.