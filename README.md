# Product CRUD App

This is a simple Django project for performing CRUD (Create, Read, Update, Delete) operations on products.

## Installation

Clone the repository:

    ```bash
    git clone https://github.com/abbappii/Simple_CRUD.git
    ```
    
Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## API Endpoints

The following API endpoints are available:

- `GET [/api/v1/products/](http://127.0.0.1:8000/api/v1/products)`: List all products.
- `POST [/api/v1/products/](http://127.0.0.1:8000/api/v1/products)`: Create a new product.
- `GET /api/v1/products/<pk>/`: Retrieve details of a specific product.
- `PUT /api/v1/products/<pk>/`: Update details of a specific product.
- `DELETE /api/v1/products/<pk>/`: Delete a specific product.
