# This is a demo of flask file architecture

## File Architecture
```
project_root/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── Model/
│   │   ├── __init__.py
│   │   ├── loadEnvironment.py
│   │   └── ...
│   └── ...
│
├── wsgi.py (WSGI entry point)
```

- **app/**: Contains the main application files.
  - `__init__.py`: Initializes the Flask application and registers Blueprints.
  - `routes.py`: Defines routes for the main application.
  - `api/`: Directory for API-related functionality.
    - `__init__.py`: Initializes the API Blueprint.
    - `routes.py`: Defines routes for the API.
  - **Model/**: Directory containing files related to environment setup or other models.
    - `__init__.py`: Initializes the Model package.
    - `loadEnvironment.py`: Loads environment variables or configurations.


## WSGI Entry Point (wsgi.py)
wsgi.py serves as the WSGI entry point for the application. It's responsible for creating and running the Flask application.  

## Routes and Blueprints
- **Routes**: Define URL endpoints and corresponding view functions for handling requests.
- **Blueprints**: Organize routes into logical groups or modules. Each Blueprint can have its own set of routes.
  - Nested routes: Routes defined within Blueprints can be nested to create hierarchical URL structures.
  - Accessing nested routes: Use the `url_prefix` parameter when registering Blueprints in `__init__.py` to define a common prefix for nested routes.

## Example Blueprint Registration in __init__.py
```python
from flask import Blueprint

# Create a Blueprint instance for the API
api = Blueprint('api', __name__, url_prefix='/api')

# Import routes from the api/routes.py file
from .api import routes
