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
