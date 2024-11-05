# Chocolate House Application

## Overview
This application is a Python-based management system for a fictional chocolate house, designed to handle:
- Seasonal chocolate flavor offerings
- Ingredient inventory management
- Customer flavor suggestions and allergy concerns

The backend uses SQLite for data storage, providing a simple and efficient way to manage the shop's essential operations.

## Features
1. **Seasonal Flavors**: Manage a list of seasonal flavors, allowing the store to offer a unique selection to customers.
2. **Ingredient Inventory**: Track ingredients used in chocolate-making, helping the store maintain stock levels and manage inventory efficiently.
3. **Customer Suggestions & Allergy Concerns**: Collect customer feedback on flavor ideas and allergy concerns, supporting the development of customer-oriented products.

## Prerequisites
- Python 3.x
- SQLite3
- Docker (if using Docker for deployment)

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/KHU2403/chocolate_app.git
   cd chocolate_app
   ```

2. **Install Dependencies**
   - It’s recommended to use a virtual environment:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows, use venv\Scripts\activate
     ```
   - Install the required Python packages:
     ```bash
     pip install -r requirements.txt
     ```

## Running the Application

1. **Initialize the Database**
   - Run the following command to set up the SQLite database:
     ```bash
     python setup_db.py
     ```
   - This will create the necessary tables for seasonal flavors, ingredient inventory, and customer suggestions.

2. **Run the Application**
   ```bash
   python app.py
   ```
   - The application will start, and you can interact with it via the command line or a specified user interface.

## Usage

- **Adding Seasonal Flavors**: You can add, view, update, and delete seasonal flavors.
- **Managing Ingredient Inventory**: View current ingredients, add new ones, or update existing stocks.
- **Handling Customer Feedback**: Review customer suggestions and allergy concerns to tailor products to customer needs.

## Docker Deployment

1. **Build the Docker Image**
   ```bash
   docker build -t chocolate_house_app .
   ```

2. **Run the Docker Container**
   ```bash
   docker run -p 5000:5000 chocolate_house_app
   ```
   - The application will be accessible on `localhost:5000`.

## Code Structure

- `app.py`: Main application logic and routing.
- `setup_db.py`: Script to initialize the SQLite database with required tables.
- `models.py`: Database models for managing seasonal flavors, inventory, and customer feedback.
- `requirements.txt`: List of dependencies.
- `Dockerfile`: Docker configuration for containerized deployment.

## SQL Queries / ORM
This application uses SQLAlchemy ORM for database operations, enabling seamless interaction with the SQLite database without needing raw SQL queries. Key operations include:
- Adding and retrieving seasonal flavors
- Managing ingredient stock levels
- Recording and viewing customer suggestions and allergy concerns

## Edge Case Handling
The application has been designed to handle:
- Duplicate entries for seasonal flavors and ingredients.
- Validation of input data to prevent incorrect entries.
- Graceful handling of empty inventory or flavor lists.

## Testing
To test the application, follow these steps:
1. Run the application using `python app.py`.
2. Test each feature:
   - **Adding flavors**: Try adding a new seasonal flavor.
   - **Updating inventory**: Modify ingredient quantities to ensure accurate inventory tracking.
   - **Submitting feedback**: Submit a customer suggestion or allergy concern.

## Contributing
For contributions, fork this repository, make your changes, and submit a pull request. Contributions should follow Python coding standards and include documentation for any new features or bug fixes.

## License
This project is licensed under the MIT License.
