Flask User Management API

A simple RESTful API built using **Flask** that allows you to perform basic CRUD (Create, Read, Update, Delete) operations on user data stored in-memory.

---

📌 Features

- Add a new user (POST)
- Retrieve all users or a specific user (GET)
- Update existing user details (PUT)
- Delete a user by ID (DELETE)
- Testable with Postman or Curl

---

🔧 Technologies Used

- Python 3.x
- Flask
- Postman (for API testing)

---

▶️ How to Run the Project

Step 1: Clone or Download the Project
If you cloned it via Git:
bash
git clone https://github.com/YOUR_USERNAME/flask-user-api.git
cd flask-user-api
`

Or download the `.zip` and extract it.

Step 2: Install Flask

bash
pip install flask


Step 3: Run the App

bash
python app.py


The app will start on:


http://127.0.0.1:5000/


---

 🛠 API Endpoints

| Method | Endpoint      | Description             |
| ------ | ------------- | ----------------------- |
| GET    | `/users`      | Get all users           |
| GET    | `/users/<id>` | Get a specific user     |
| POST   | `/users`      | Add a new user          |
| PUT    | `/users/<id>` | Update an existing user |
| DELETE | `/users/<id>` | Delete a user           |

---

📦 Sample JSON for POST/PUT

json
{
  "id": "1",
  "name": "John"
}


---

🧪 API Testing with Postman

1. Open Postman
2. Create a new request
3. Use `http://127.0.0.1:5000/users`
4. Select the appropriate method (GET, POST, PUT, DELETE)
5. For POST and PUT, go to the **Body** tab → raw → JSON

Example POST body:

json
{
  "id": "2",
  "name": "Alice"
}


---
 ✅ Status

* [x] Project setup
* [x] Flask routes created
* [x] CRUD operations working
* [x] Postman tested
* [x] Uploaded to GitHub

---

📄 License

This project is for learning purposes and does not require a license.
