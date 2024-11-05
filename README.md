# 🍫 Welcome to the Chocolate House App!

Hey there, chocolate lovers! This Python-powered application is designed to help you run your very own chocolate shop, keeping track of seasonal flavors, managing ingredient inventory, and collecting valuable customer feedback.

## ✨ What’s Inside?
The Chocolate House app is perfect for small businesses and uses SQLite to store all the tasty data.

### Key Features
1. **Seasonal Flavors**: Easily manage your rotating chocolate delights.
2. **Ingredient Inventory**: Keep an eye on your stock of essential ingredients.
3. **Customer Feedback**: Gather suggestions and allergy notes to delight your customers.

---

## 🛠 Prerequisites
Before you start, ensure you have:
- Python 3.x
- SQLite3
- Docker (optional, for easy deployment)

---

## 🚀 Getting Started

### 1. Clone the Repository
First, grab the code by running:
```bash
git clone https://github.com/KHU2403/chocolate_app.git
cd chocolate_app
```

### 2. Install Dependencies
Using a virtual environment is a good idea:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🎉 Running Your Chocolate House

### 1. Set Up the Database
Let’s get your database ready:
```bash
python database.py
```

### 2. Start the Application
Bring your app to life:
```bash
python app.py
```
You can now explore the API at `localhost:5000`.

---

## 🧑‍💻 Using the App

- **Manage Seasonal Flavors**: Add, view, update, and delete flavors as needed.
- **Track Ingredients**: Check your ingredient stocks, add new items, and update quantities.
- **Collect Customer Feedback**: Record suggestions and allergy concerns to enhance your offerings.

---

## 🐳 Deploying with Docker

Want to deploy with Docker? It’s easy:
1. **Build the Image**
   ```bash
   docker build -t chocolate_house_app .
   ```

2. **Run the Container**
   ```bash
   docker run -p 5000:5000 chocolate_house_app
   ```
Access the app at `localhost:5000`.

---

## 📂 Project Structure

Here’s what’s inside the app:
- **`app.py`**: The main code and API routes.
- **`database.py`**: Initializes the SQLite database.
- **`models.py`**: Contains the database models for flavors and inventory.
- **`requirements.txt`**: Lists the needed packages.
- **`Dockerfile`**: Sets up the app for containerization.

---

## 🔍 How We Use SQLAlchemy ORM
SQLAlchemy ORM makes it easy to:
- Add, retrieve, and update flavors and ingredients.
- Keep track of customer feedback, including suggestions and allergies.

---

## 🔄 Handling Edge Cases
We’ve built in protections for:
- Duplicate entries.
- Data validation to prevent errors.
- Graceful handling of empty lists for flavors and ingredients.

---

## 🧪 Testing Your App

To check everything works smoothly:
1. Start the app with `python app.py`.
2. Test each feature:
   - **Flavors**: Add and update flavors.
   - **Inventory**: Adjust ingredient quantities.
   - **Feedback**: Submit customer suggestions or allergy notes.

---
Enjoy running your Chocolate House! 🍫
