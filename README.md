# Django Models Submodule

This repository contains shared Django models that can be used across multiple projects.

## Models

- `Todo`: A simple todo list model with title, description, and completion status.

## Usage

1. Add this repository as a submodule to your project:

```bash
git submodule add <repository-url> python-api-submodules-example-django-modals
```

2. Add the models to your Django project's INSTALLED_APPS:

```python
INSTALLED_APPS = [
    ...
    'django_modals',
    ...
]
```

3. Import and use the models in your project:

```python
from django_modals.models import Todo
```
