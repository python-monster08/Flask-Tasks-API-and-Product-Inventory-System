
# Flask Tasks API and Product Inventory System

This project contains two components:

1. **Flask Tasks API**: A Flask-based web application for managing tasks with CRUD operations.
2. **Product Inventory System**: A file-based product inventory system where data is persisted in a JSON file, supporting CRUD operations for managing products.

---

## Table of Contents

1. [Task 1: Flask Tasks API](#task-1-flask-tasks-api)
   - [Requirements](#requirements)
   - [Project Setup](#project-setup)
   - [Running the Application](#running-the-application)
   - [API Endpoints](#api-endpoints)
     - [Create a New Task (POST)](#create-a-new-task-post)
     - [Retrieve All Tasks (GET)](#retrieve-all-tasks-get)
     - [Update a Task (PUT)](#update-a-task-put)
     - [Delete a Task (DELETE)](#delete-a-task-delete)
   - [Dockerization](#dockerization)
   - [Advanced Usage](#advanced-usage)
   - [API Testing with Postman and curl](#api-testing)
   
2. [Task 2: Product Inventory System](#task-2-product-inventory-system)
   - [Requirements](#requirements-1)
   - [Running the Application](#running-the-application-1)
   - [Operations](#operations)
     - [Add a Product](#add-a-product)
     - [Display All Products](#display-all-products)
     - [Update a Product](#update-a-product)
     - [Delete a Product](#delete-a-product)

---

## Task 1: Flask Tasks API

### Requirements

- [Docker](https://www.docker.com/products/docker-desktop) installed
- [Postman](https://www.postman.com/downloads/) or `curl` for API testing

### Project Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/python-monster08/Flask-Tasks-API-and-Product-Inventory-System.git
   cd Flask-Tasks-API-and-Product-Inventory-System
   ```

2. Install dependencies:

    - If using Docker, skip to the next section.
    - If running locally, install the Python dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up and run the Docker containers:

    ```bash
    docker-compose up --build
    ```

    This will start the Flask app on `http://localhost:5000`.

### Running the Application

To run the application, use the following command:

```bash
docker-compose up --build
```

Once running, the application will be accessible on `http://localhost:5000`.

### API Endpoints

The Flask app provides a simple **Tasks API** to manage tasks with the following CRUD operations:

#### **Create a New Task (POST)**

- **Method**: `POST`
- **URL**: `http://localhost:5000/tasks`
- **Headers**: `Content-Type: application/json`
- **Body Example**:

    ```json
    {
      "description": "First task"
    }
    ```

- **Response**:
  - **Status**: `201 Created`
  - **Body**:

    ```json
    {
      "message": "Task created!"
    }
    ```

#### **Retrieve All Tasks (GET)**

- **Method**: `GET`
- **URL**: `http://localhost:5000/tasks`
- **Response**:
  - **Status**: `200 OK`
  - **Body Example**:

    ```json
    [
      {
        "id": 1,
        "description": "First task",
        "status": "Incomplete"
      }
    ]
    ```

#### **Update a Task (PUT)**

- **Method**: `PUT`
- **URL**: `http://localhost:5000/tasks/<id>`
- **Headers**: `Content-Type: application/json`
- **Body Example**:

    ```json
    {
      "description": "Updated task",
      "status": "Completed"
    }
    ```

- **Response**:
  - **Status**: `200 OK`
  - **Body**:

    ```json
    {
      "message": "Task updated!"
    }
    ```

#### **Delete a Task (DELETE)**

- **Method**: `DELETE`
- **URL**: `http://localhost:5000/tasks/<id>`
- **Response**:
  - **Status**: `200 OK`
  - **Body**:

    ```json
    {
      "message": "Task deleted!"
    }
    ```

### Dockerization

The Flask app has been containerized using **Docker**. You can start the app and the database together with `docker-compose`.

#### Build the Docker containers:

```bash
docker-compose up --build
```

#### Connect the Flask app to the database using the environment variables in the `docker-compose.yml` file:

```yaml
environment:
  - FLASK_ENV=development
  - DATABASE_URL=sqlite:///tasks.db
```

### Advanced Usage

You can modify the `DATABASE_URL` to point to PostgreSQL or MySQL if required. By default, it uses SQLite for simplicity.

### API Testing

You can test the API using **Postman** or **curl**.

#### **With Postman**:

For POST, GET, PUT, and DELETE requests, use the raw JSON body format for POST and PUT requests. Set the URL to `http://localhost:5000/tasks`.

#### **With curl**:

- **Create a Task**:

  ```bash
  curl -X POST http://localhost:5000/tasks -H "Content-Type: application/json" -d '{"description": "First task"}'
  ```

- **Retrieve All Tasks**:

  ```bash
  curl http://localhost:5000/tasks
  ```

- **Update a Task**:

  ```bash
  curl -X PUT http://localhost:5000/tasks/1 -H "Content-Type: application/json" -d '{"description": "Updated task", "status": "Completed"}'
  ```

- **Delete a Task**:

  ```bash
  curl -X DELETE http://localhost:5000/tasks/1
  ```

---

## Task 2: Product Inventory System

### Requirements

- [Python](https://www.python.org/downloads/) installed on your system.

### Running the Application

1. **Change to the directory**:

    ```bash
    cd product_inventory_system
    ```

2. **Run the program**:

    ```bash
    python inventory_system.py
    ```

    This will start the interactive Product Inventory System where you can add, view, update, and delete products.

### Operations

#### **Add a Product**

1. Select option `1` from the menu to add a product.
2. Enter the following:
    - **Product ID** (e.g., "101")
    - **Product Name** (e.g., "Laptop")
    - **Quantity** (e.g., "10")
    - **Price** (e.g., "1000.0")

The product will be saved in a file named `product_inventory.json`.

#### **Display All Products**

1. Select option `2` from the menu to display all products.
2. The system will read and display the contents from the JSON file, showing each product's ID, name, quantity, and price.

#### **Update a Product**

1. Select option `3` from the menu.
2. Enter the **Product ID** of the product to update.
3. Provide the new quantity or price (you can leave one field blank to skip updating that field).
4. The updated product will be saved in the JSON file.

#### **Delete a Product**

1. Select option `4` from the menu.
2. Enter the **Product ID** of the product to delete.
3. The product will be removed from the JSON file.

---

## Conclusion

This project includes two separate systems:

1. **Flask Tasks API**: A web-based API for managing tasks with CRUD operations.
2. **Product Inventory System**: A console-based inventory system for managing products stored in a JSON file.

Both systems demonstrate different techniques for handling CRUD operations, one with a REST API and the other with file-based persistence. Let me know if you encounter any issues or need further instructions!
