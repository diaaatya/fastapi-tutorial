# FastAPI Item Management API

This FastAPI application demonstrates a simple RESTful API for managing items such as food, drinks, and snacks. The API allows you to create, read, update, and delete items, as well as query them based on parameters like name, price, count, and category.
show support by subscirbing to my yt channel [https://www.youtube.com/@CodeWithD] Thank you for support
## Features
- **GET /**: Returns all items.
- **GET /items/{item_id}**: Query an item by its ID.
- **GET /items**: Query items by optional parameters (name, price, count, category).
- **POST /**: Create a new item.
- **PUT /items/{item_id}**: Update an existing item.
- **DELETE /{item_id}**: Delete an item by its ID.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/diaaatya/fastapi-item-management.git
    ```

2. Navigate to the project directory:

    ```bash
    cd fastapi-item-management
    ```

3. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Linux/macOS
    venv\Scripts\activate     # For Windows
    ```

4. Install the required dependencies:

    ```bash
    pip install fastapi uvicorn pydantic
    ```

## Running the Application

To start the FastAPI server, run the following command:

```bash
uvicorn main:app --reload
