# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Testing Django Models

| Title                 | Type   | Duration | Author               |
|-----------------------|--------|----------|----------------------|
| Testing Django Models | Lesson | 2:00     | Suresh Melvin Sigera |

### Lesson Objectives

- By the end of this lesson, students will be able to
- Understand the importance of testing Django models
- Set up and structure model tests using Django’s `TestCase` class
- Write and run unit tests for model string representations
- Test model methods to ensure correct business logic implementation
- Verify model relationships such as **Many-to-Many** and **ForeignKey** associations.
- Test cascading delete behaviors to maintain data integrity
- Understand how to test model data ordering

### Setting Up the Python Environment (10 minutes)

Before diving into the authentication testing implementation, we need to properly configure our development environment.
In Django development, isolating project dependencies is crucial for maintaining consistent test environments. We'll
start by activating our virtual environment, which creates an isolated Python environment for our project.

Let's begin with the environment setup:

```text
# On Unix/MacOS
source venv/bin/activate

# On Windows
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Introduction to Testing Django Models (5 minutes)

In Django applications, models are the backbone that handle data management and database interactions. Ensuring the
reliability of models through comprehensive testing is crucial. Django provides a robust framework for testing through
the `django.test` module, leveraging Python's built-in unittest framework.

We will cover different types of tests using a sample Django app with `Cat`, `Toy`, and `Feeding` models. These models
demonstrate common relationships: One-to-Many, Many-to-Many, and ForeignKey.

### Setting Up Tests with TestCase (10 minutes)

Before writing tests, ensure Django's testing framework is correctly configured. Tests reside in the `test_models.py`
file within each app or can be organized in a `tests/models` directory for better modularity.

```python
from django.test import TestCase
from django.contrib.auth.models import User
from main_app.models import Cat, Toy, Feeding
from datetime import date
```

The `TestCase` class sets up an isolated test environment with a temporary database.

### The `setUp` Method (15 minutes)

The `setUp` method initializes data before each test is run. This ensures a consistent test environment and avoids code
duplication.

```python
class ModelsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.toy = Toy.objects.create(name='Mouse', color='Gray')
        self.cat = Cat.objects.create(
            name='Felix',
            breed='Tabby',
            description='Playful cat',
            age=3,
            user=self.user
        )
        self.cat.toys.add(self.toy)
        self.feeding = Feeding.objects.create(
            date=date.today(),
            meal='B',
            cat=self.cat
        )
```

This method creates:

- A test user
- A toy linked to a cat
- A feeding record for the cat

Each test starts with this clean, controlled dataset.

### Testing String Representations (20 minutes)

**Testing `Toy` String Representation**

The `__str__` method in Django models defines the human-readable representation of an object. Testing it ensures models
display correctly in Django Admin and other interfaces.

```python
def test_toy_str(self):
    self.assertEqual(str(self.toy), 'Mouse')
```

**Testing `Cat` String Representation**

```python
def test_cat_str(self):
    self.assertEqual(str(self.cat), 'Felix')
```

This ensures the `Cat` model's string representation reflects its name.

**Testing Feeding String Representation**

```python
def test_feeding_str(self):
    expected = f"Breakfast on {date.today()}"
    self.assertEqual(str(self.feeding), expected)
```

This ensures the `Feeding` model dynamically includes the meal and date.

### Testing Model Methods (15 minutes)

Model methods encapsulate business logic. For example, checking if a cat is fully fed for the day.

**`fed_for_today` Method Test**

```python
def test_cat_feeding_status(self):
    self.assertFalse(self.cat.fed_for_today())  # Initially not fully fed

    # Add remaining meals
    Feeding.objects.create(date=date.today(), meal='L', cat=self.cat)
    Feeding.objects.create(date=date.today(), meal='D', cat=self.cat)

    self.assertTrue(self.cat.fed_for_today())  # Now fully fed
```

This test verifies the business rule: a cat must have all meals (Breakfast, Lunch, Dinner) logged to be considered fully
fed.

### Testing Model Relationships (15 minutes)

Relationships between models (One-to-Many, Many-to-Many) are integral to Django's ORM.

**Testing Many-to-Many Relationship Between `Cat` and `Toy`**

```python
def test_cat_toy_relationship(self):
    new_toy = Toy.objects.create(name='Ball', color='Red')
    self.cat.toys.add(new_toy)

    self.assertEqual(self.cat.toys.count(), 2)  # Two toys associated
    self.assertIn(new_toy, self.cat.toys.all())  # Verify new toy exists
```

This ensures that toys can be correctly added to a cat and retrieved via the relationship.

### Testing Data Ordering (15 minutes)

Django allows models to be ordered using the `Meta` class. Testing ensures data is retrieved in the correct sequence.

**Testing `Feeding` Model Ordering**

```python
def test_feeding_ordering(self):
    yesterday = date.today().replace(day=date.today().day - 1)
    old_feeding = Feeding.objects.create(date=yesterday, meal='B', cat=self.cat)

    feedings = Feeding.objects.all()
    self.assertEqual(feedings[0], self.feeding)  # Most recent feeding first
    self.assertEqual(feedings[1], old_feeding)
```

This test confirms the order in which feedings are returned from the database.

#### Testing Cascade Deletes (10 minutes)

Cascade deletion ensures related objects are deleted automatically when their parent is removed.

**Testing `User` Deletion Cascading to `Cats`**

```python
def test_cascade_delete(self):
    cat_id = self.cat.id
    self.user.delete()
    self.assertEqual(Cat.objects.filter(id=cat_id).count(), 0)  # Cat should be deleted
```

This verifies that deleting a `User` cascades the deletion to associated `Cat` records.

### Summary (10 minutes)

In this lesson, we explored the fundamentals of testing Django models:

- `setUp` Method: Establishing a consistent test environment
- String Representation Tests: Ensuring models display correctly
- Model Method Tests: Validating business logic within model methods.
- Relationship Tests: Checking integrity of Many-to-Many and ForeignKey associations.
- Ordering Tests: Confirming data retrieval order.
- Cascade Delete Tests: Ensuring data integrity through proper cascading behavior.

Comprehensive model testing helps catch errors early, maintain data integrity, and ensure business rules are
consistently enforced. Regularly writing tests as part of development enhances code quality and reduces the likelihood
of bugs in production.