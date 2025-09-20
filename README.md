# 🍭Sweet Shop Management System 🍫🍬

A full-stack web application for managing a sweet shop's inventory, built with FastAPI (Python) backend and React (TypeScript) frontend.

## 🚀 Features

### Backend (FastAPI)
- **User Authentication**: JWT-based authentication with user registration and login
- **Role-based Access Control**: Admin and user roles with different permissions
- **Sweet Management**: CRUD operations for sweets (Create, Read, Update, Delete)
- **Search & Filter**: Search sweets by name, category, and price range
- **Inventory Management**: Purchase and restock functionality
- **Database**: PostgreSQL with SQLAlchemy ORM
- **API Documentation**: Auto-generated Swagger/OpenAPI docs

### Frontend (React + TypeScript)
- **Modern UI**: Clean, responsive design with CSS Grid and Flexbox
- **Authentication**: Login and registration forms with validation
- **Sweet Catalog**: Display all available sweets with purchase functionality
- **Search & Filter**: Real-time search and filtering capabilities
- **Admin Panel**: Full CRUD interface for managing sweets (admin only)
- **State Management**: React Context for authentication and sweet management

## 🛠️ Technology Stack

### Backend
- **Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Authentication**: JWT with python-jose
- **Password Hashing**: bcrypt
- **Migrations**: Alembic
- **Testing**: pytest with TestClient

### Frontend
- **Framework**: React 18 with TypeScript
- **Build Tool**: Vite
- **Routing**: React Router DOM
- **HTTP Client**: Axios
- **Styling**: CSS3 with modern features

### DevOps
- **Containerization**: Docker & Docker Compose
- **Database**: PostgreSQL 15
- **Environment**: Development and production configurations

## 📋 Prerequisites

- Node.js 18+ and npm
- Python 3.11+
- Docker and Docker Compose (optional)
- PostgreSQL (if not using Docker)

## 🚀 Quick Start

### Option 1: Using Docker Compose (Recommended)

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd sweetshop
   ```

2. **Start the application**
   ```bash
   docker-compose up --build
   ```

3. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

### Option 2: Manual Setup

1. **Start Backend**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   python setup_admin.py  # Creates admin user and sample data
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

2. **Start Frontend**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

3. **Access the application**
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:8000/docs

## 📋 Prerequisites

- Node.js 18+ and npm
- Python 3.11+
- Docker and Docker Compose (optional)
- PostgreSQL (if not using Docker)

## 🧪 Testing

### Backend Tests
```bash
cd backend
python -m pytest --tb=short -v
```

### Frontend Tests
```bash
cd frontend
npm test
```

## 📚 API Documentation

### Authentication Endpoints
- `POST /api/auth/register` - Register a new user
- `POST /api/auth/login` - Login with email/username and password

### Sweet Management Endpoints
- `GET /api/sweets` - Get all sweets
- `POST /api/sweets` - Create a new sweet (Admin only)
- `GET /api/sweets/search` - Search sweets with filters
- `PUT /api/sweets/{id}` - Update a sweet (Admin only)
- `DELETE /api/sweets/{id}` - Delete a sweet (Admin only)

### Inventory Endpoints
- `POST /api/sweets/{id}/purchase` - Purchase a sweet
- `POST /api/sweets/{id}/restock` - Restock a sweet (Admin only)

## 🎯 Usage

### For Regular Users
1. Register an account or login
2. Browse the sweet catalog
3. Use search and filters to find specific sweets
4. Purchase sweets (quantity will decrease automatically)

### For Admin Users
1. Login with admin credentials
2. Access the admin panel
3. Add, edit, or delete sweets
4. Restock inventory as needed

## 🔧 Configuration

### Environment Variables

#### Backend (.env)
```env
DATABASE_URL=postgres://username:password@localhost:5432/sweetshop
SECRET_KEY=your-secret-key-here
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

#### Frontend (.env.local)
```env
VITE_API_URL=http://localhost:8000/api
```

## 🏗️ Project Structure

```
sweetshop/
├── backend/
│   ├── app/
│   │   ├── api/           # API endpoints
│   │   ├── core/          # Security and configuration
│   │   ├── db/            # Database configuration
│   │   ├── models/        # SQLAlchemy models
│   │   ├── schemas/       # Pydantic schemas
│   │   └── main.py        # FastAPI application
│   ├── tests/             # Test files
│   ├── alembic/           # Database migrations
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/    # React components
│   │   ├── pages/         # Page components
│   │   ├── api/           # API client functions
│   │   ├── hooks/         # Custom React hooks
│   │   └── contexts/      # React contexts
│   └── package.json
├── docker-compose.yml
└── README.md
```

## 🚀 Deployment

### Using Docker
```bash
docker-compose -f docker-compose.prod.yml up -d
```

### Manual Deployment
1. Build the frontend: `npm run build`
2. Serve the backend with a production WSGI server
3. Configure reverse proxy (nginx) for production

## 🤖 My AI Usage

### AI Tools Used
- **Claude (Anthropic)**: Primary AI assistant for code generation, debugging, and project guidance
- **GitHub Copilot**: Code completion and suggestions during development

### How AI Was Used

#### Code Generation
- **Backend API Structure**: Used Claude to generate the initial FastAPI application structure, including authentication endpoints, sweet management, and inventory operations
- **Database Models**: Generated SQLAlchemy models for User and Sweet entities with proper relationships and constraints
- **Pydantic Schemas**: Created request/response schemas for API validation and serialization
- **Test Cases**: Generated comprehensive test suites covering authentication, CRUD operations, and edge cases

#### Problem Solving
- **Database Issues**: Resolved async/sync database driver conflicts in test setup
- **Authentication Flow**: Fixed JWT token handling and user authentication between frontend and backend
- **API Integration**: Debugged and fixed frontend API calls to match backend expectations
- **Test Configuration**: Resolved TestClient vs AsyncClient issues in pytest setup

#### Code Quality
- **Error Handling**: Implemented proper error handling and validation throughout the application
- **Security**: Added proper password hashing, JWT token validation, and role-based access control
- **Documentation**: Generated comprehensive README and inline code documentation

### AI Impact on Workflow

**Positive Impacts:**
- **Rapid Prototyping**: AI significantly accelerated the initial development phase, allowing quick iteration on core features
- **Best Practices**: AI suggestions helped implement modern patterns like proper error handling, validation, and security measures
- **Comprehensive Testing**: AI-generated test cases provided excellent coverage and helped catch edge cases early
- **Code Consistency**: AI assistance ensured consistent coding patterns and naming conventions throughout the project

**Challenges and Learning:**
- **Context Management**: Required careful management of AI context to maintain consistency across different parts of the application
- **Validation**: Had to thoroughly test and validate AI-generated code to ensure it met specific requirements
- **Integration**: Some AI-generated code needed manual adjustment to work properly with existing components

**Reflection:**
The use of AI tools was instrumental in building a robust, full-stack application efficiently. The combination of code generation, debugging assistance, and best practice suggestions allowed for rapid development while maintaining high code quality. The key was using AI as a collaborative partner rather than a replacement for critical thinking and testing.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📞 Support

For support, email support@sweetshop.com or create an issue in the repository.

---

**Note**: This project was developed as part of a technical assessment, demonstrating full-stack development skills with modern technologies and AI-assisted development practices.
