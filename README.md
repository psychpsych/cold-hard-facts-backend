
# 📚 FastAPI Backend for Question Management System

This project is a simple FastAPI backend to manage questions in a quiz system. It includes functionalities like reading, updating, and managing the status of questions in the database.

## 🚀 Features

- **CRUD Operations** for handling quiz questions.
- **Database integration** using SQLModel (SQLAlchemy-based).
- Lightweight and fast using **FastAPI**.
- Easy to expand and integrate with other systems.

## 🛠️ Technologies Used

- **FastAPI**: For creating APIs quickly and efficiently.
- **SQLModel**: ORM for handling database models and operations.
- **SQLite**: Embedded database for development and testing.
- **Python 3.9+**: The language used for developing the project.

## ⚙️ Setup Instructions

To get started with this project, follow these steps:

### 1. Clone the repository
```bash
git clone https://github.com/psychpsych/cold-hard-facts-backend
cd cold-hard-facts-backend
```

### 2. Create and activate a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
uvicorn main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

## 🧑‍💻 API Endpoints

### Get a question by ID
```http
GET /question/{id}
```
- **Parameters**:
  - `id`: ID of the question (integer)
- **Response**:
  - Returns the question with the given ID or a 404 error if not found.

### Update the "seen" status of a question
```http
PUT /question/{id}
```
- **Parameters**:
  - `id`: ID of the question (integer)
  - `is_seen`: Boolean value to update the seen status.
- **Response**:
  - Returns the updated question status.

## 🛣️ Roadmap

### ✔️ Completed
- Basic CRUD operations (read and update).
- FastAPI integration for API creation.
- SQLite database implementation.

### 🟢 Next Steps
- Add full database update functionality.
- Implement `POST /questions/` endpoint for adding new questions.
- Add detailed API documentation using FastAPI's built-in tools.

### 🟡 Planned Enhancements
- JWT-based authentication for secure API access.
- Question categories and filter by category.
- Performance optimization for large datasets.

### 🔵 Future Vision
- Frontend integration using modern frameworks (React.js or Vue.js).
- Third-party integrations (e.g., Slack, Discord) for wider reach.
- Frontend animations for event-driven interactions (e.g., button clicks, page transitions).

## 🗂️ Project Structure

```bash
backend-fastapi/
│
├── main.py             # FastAPI app and API endpoints
├── db.py               # Database setup and session management
├── database.db         # SQLite database file
├── .gitignore          # Git ignore file
├── .venv/              # Python virtual environment
└── requirements.txt    # Python dependencies
```

## 🐛 Known Issues
- The `update_question` endpoint doesn't fully update the database. This feature needs proper implementation.

## 🤝 Contributing

Feel free to fork the repository and submit pull requests. For major changes, please open an issue first to discuss what you'd like to change.

## 📝 License

This project is licensed under the MIT License.
