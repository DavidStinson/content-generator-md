# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Django CRUD Lab

| Title               | Type   | Duration | Author               |
|---------------------|--------|----------|----------------------|
| Django CRUD DEF Lab | Lesson | 6:00     | Suresh Melvin Sigera |

### Learning Objectives

- Build a full-stack Django application with authentication using Django Rest Framework (DRF).
- Implement One-to-Many and Many-to-Many relationships with DRF serializers.
- Manage user authorization and data protection with DRF.

#### Day 1: Django Setup, URLs, Views, and DRF Intro

- Set up Django project and app.
- Configure URLs for Django and DRF endpoints.
- Introduction to Django models and serializers.
- Create Dog model with fields: name, breed, description, age.
- Implement basic CRUD views using DRF:
    - List (index)
    - Detail
    - Create
    - Update
    - Delete
- Set up user authentication (registration and login) via DRF for creating dogs.
- Add dog feeding functionality with datetime tracking via API endpoints.

#### Day 2: Many-to-Many Relationships with DRF

- Create Toy model with fields: name, color.
- Add Many-to-Many relationship between Dog and Toy models.
- Create CRUD API endpoints for managing toys.
- Implement toy assignment to dogs through DRF endpoints.
- Display assigned toys on dog detail page through DRF serializers.

#### Day 3: Authentication & Authorization with DRF

- Implement user signup, login, and logout using DRF's authentication system.
- Add user-specific API views, ensuring that each user can only access their own data.
- Restrict dog and toy operations to authenticated users using DRF permissions.
- Add a user profile API endpoint showing the authenticated user's dogs.

## How to submit homework

### Submitting work

- Step 1. Create a new repository on your GitHub Enterprise account named "dog-collector-drf."
- Step 2. Push your project to the newly created repository.
- Step 3. Create an issue in this repository
- Step 3.1. Add a title (First name, Last Name) and your repository URL

In the comment section, you must add the following:

```text
* Comfort level [0 to 5]
* Completeness [0 to 5]
* What was a win?
* What was a challenge?
* Any other comments
```
