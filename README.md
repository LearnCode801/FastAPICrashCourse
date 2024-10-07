# FastAPI Full Course Overview

This course covers everything you need to know to work with FastAPI, from setting up your environment to building a fully functioning API with database integration, authentication, and more.

| Topic                          | Description |
|---------------------------------|-------------|
| **Intro**                       | Introduction to the course and its objectives. |
| **Project Overview**            | Overview of the API project you will build throughout the course. |
| **Mac Python Installation**     | Step-by-step guide to install Python on Mac. |
| **Mac VS Code Install & Setup** | Instructions for setting up Visual Studio Code on Mac. |
| **Windows Python Installation** | Step-by-step guide to install Python on Windows. |
| **Windows VS Code Install & Setup** | Instructions for setting up Visual Studio Code on Windows. |
| **Python Virtual Environment Basics** | Overview of creating and managing virtual environments in Python. |
| **Virtual Environment on Windows** | Setting up a virtual environment in Windows. |
| **Virtual Environment on Mac** | Setting up a virtual environment on Mac. |
| **Install Dependencies with pip** | How to install necessary dependencies using `pip`. |
| **Starting FastAPI**            | Introduction to FastAPI framework and its basic structure. |
| **Path Operations**             | Explanation of creating basic path operations (endpoints) in FastAPI. |
| **Intro to HTTP Requests**      | Basics of HTTP requests, methods, and handling them in FastAPI. |
| **Schema Validation with Pydantic** | Using Pydantic for data validation in FastAPI applications. |
| **CRUD Operations**             | Implementing Create, Read, Update, Delete operations. |
| **Storing in Array**            | Techniques to store data in an array structure. |
| **Creating**                    | Creating new entries in your API. |
| **Postman Collections & Saving Requests** | How to use Postman to test APIs and save requests. |
| **Retrieve One**                | Fetching a single resource from the API. |
| **Path Order Matters**          | The importance of ordering path operations in FastAPI. |
| **Changing Response Status Codes** | How to modify the status codes returned by the API. |
| **Deleting**                    | Implementing the delete functionality in your API. |
| **Updating**                    | Updating existing entries in the API. |
| **Automatic Documentation**     | FastAPI’s built-in support for automatic API documentation. |
| **Python Packages**             | Overview of important Python packages used in FastAPI projects. |
| **Database Intro**              | Introduction to using databases in FastAPI projects. |
| **Postgres Windows Install**    | How to install PostgreSQL on Windows. |
| **Postgres Mac Install**        | How to install PostgreSQL on Mac. |
| **Database Schema & Tables**    | Designing a database schema and creating tables. |
| **Managing Postgres with PgAdmin GUI** | Using PgAdmin to manage and interact with PostgreSQL databases. |
| **Your First SQL Query**        | Writing and executing basic SQL queries. |
| **Filter Results with WHERE**   | Using the `WHERE` clause to filter SQL query results. |
| **SQL Operators**               | Overview of SQL operators to manipulate and query data. |
| **IN Operator**                 | Using the `IN` operator in SQL queries. |
| **Pattern Matching with LIKE**  | Using the `LIKE` operator for pattern matching in SQL. |
| **Ordering Results**            | Sorting SQL query results using `ORDER BY`. |
| **LIMIT & OFFSET**              | Paginating results using `LIMIT` and `OFFSET` in SQL. |
| **Modifying Data**              | Techniques for modifying (insert, update, delete) data in SQL. |
| **Setup App Database**          | Setting up the FastAPI app to work with a database. |
| **Connecting to Database with Python** | How to connect FastAPI to a PostgreSQL database using Python. |
| **Database CRUD**               | Implementing CRUD operations in the database via FastAPI. |
| **ORM Introduction**            | Introduction to Object-Relational Mapping (ORM) in FastAPI. |
| **SQLAlchemy Setup**            | Setting up SQLAlchemy as the ORM for the FastAPI project. |
| **Adding CreatedAt Column**     | Adding timestamps for created entries in the database. |
| **Get All**                     | Fetching all entries from a database table. |
| **Create**                      | Adding new entries to the database. |
| **Get by ID**                   | Fetching a single entry by its ID from the database. |
| **Delete**                      | Deleting an entry from the database. |
| **Update**                      | Updating an entry in the database. |
| **Pydantic vs ORM Models**      | Understanding the difference between Pydantic and ORM models in FastAPI. |
| **Pydantic Models Deep Dive**   | In-depth discussion on using Pydantic models for data validation. |
| **Response Model**              | Creating structured response models in FastAPI. |
| **Creating Users Table**        | Creating a database table for users. |
| **User Registration Path Operation** | Implementing a user registration feature in FastAPI. |
| **Hashing Passwords**           | Securing user passwords by hashing them. |
| **Refactor Hashing Logic**      | Improving and refactoring the password hashing logic. |
| **Get User by ID**              | Fetching a user by their ID. |
| **FastAPI Routers**             | Organizing FastAPI routes using routers. |
| **Router Prefix**               | Using prefixes to group related routes in FastAPI. |
| **Router Tags**                 | Organizing routes with tags for better API documentation. |
| **JWT Token Basics**            | Basics of JWT tokens for authentication in FastAPI. |
| **Login Process**               | Implementing user login and authentication. |
| **Creating Token**              | How to generate JWT tokens for users. |
| **OAuth2 Password Request Form**| Using OAuth2 for secure authentication in FastAPI. |
| **Verify User is Logged In**    | Verifying whether a user is authenticated. |
| **Fixing Bugs**                 | Common bugs and how to fix them during FastAPI development. |
| **Protecting Routes**           | Securing routes to allow only authorized users to access them. |
| **Test Expired Token**          | Testing expired tokens in the authentication process. |
| **Fetching User in Protected Routes** | Fetching the currently authenticated user in protected routes. |
| **Postman Advanced Features**   | Exploring advanced features of Postman for API testing. |
| **SQL Relationship Basics**     | Introduction to relationships between SQL tables. |
| **Postgres Foreign Keys**       | Implementing foreign keys in PostgreSQL. |
| **SQLAlchemy Foreign Keys**     | Managing foreign keys with SQLAlchemy in FastAPI. |
| **Update Schema to Include User** | Updating the database schema to include user relationships. |
| **Assigning Owner ID When Creating New** | Assigning a user as the owner of a newly created resource. |
| **Delete and Update Only Your Own** | Restricting delete and update actions to the owner of the resource. |
| **Only Retrieving Logged In User’s** | Allowing users to retrieve only their own resources. |
| **SQLAlchemy Relationships**    | Working with relationships between models in SQLAlchemy. |
| **Query Parameters**            | Using query parameters in FastAPI routes. |
| **Cleanup Main.py File**        | Organizing and cleaning up the main FastAPI file. |
| **Environment Variables**       | Using environment variables to secure sensitive data. |
| **Vote/Like Theory**            | Overview of implementing a vote/like feature in your application. |
| **Votes Table**                 | Creating a database table for storing votes/likes. |
| **Votes SQLAlchemy**            | Managing vote data with SQLAlchemy. |
| **Votes Route**                 | Creating API routes for voting/liking resources. |
| **SQL Joins**                   | Using SQL joins to combine data from multiple tables. |
| **Joins in SQLAlchemy**         | Implementing joins using SQLAlchemy. |
| **Get One with Joins**          | Fetching a single resource using joins to include related data. |
| **Database Migration Tool**     | Introduction to tools for migrating database schema changes. |
| **Alembic Setup**               | Setting up Alembic for database migrations in FastAPI. |
| **Disable SQLAlchemy Create Engine** | Optimizing SQLAlchemy engine behavior for better performance. |
| **What is CORS?**               | Explanation of Cross-Origin Resource Sharing (CORS) and its configuration. |
| **Git Prerequisites**           | Setting up prerequisites for using Git in projects. |
| **Git Install**                 | Installing Git on your system. |
| **Github**                      | Using GitHub for version control and project collaboration. |

---

Happy Coding!
