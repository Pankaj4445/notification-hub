# NotificationHub API

**A backend that includes**: 
Authentication,
Redis,
Caching,
Background Jobs,
Rate Limiting,
Email Service,
Docker,
PostgreSQL,
API Design,
System Design

## System Design

Client/Browser/Postman
   ↓
FastAPI
   ↓
Services
   ↓
Repositories
   ↓
PostgreSQL

Redis
├── OTP
├── Cache
├── Rate Limiter
├── Email Queue
└── Notifications


## structure
notification-hub/
│
├──app/
│   │
│   ├── api/
│   │   └── v1/
│   │       ├── auth.py
│   │       ├── users.py
│   │       ├── notifications.py
│   │       └── admin.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── logging.py
│   │   └── security.py
│   │
│   ├── database/
│   │   ├── base.py
│   │   ├── dependency.py
│   │   └── session.py
│   │
│   ├── models/
│   │
│   ├── schemas/
│   │
│   ├── repositories/
│   │
│   ├── services/
│   │
│   ├── security/
│   │
│   ├── redis/
│   │
│   ├── workers/
│   │
│   ├── exceptions/
│   │
│   ├── enums/
│   │
│   ├── constants/
│   │
│   ├── utils/
│   │
│   ├── static/
│   │
│   └── templates/
├── docker/
├── requirements.txt
├── docker-compose.yml
├── .env
└── README.md

## App folder
mkdir app\api app\core app\database app\models app\schemas app\repositories app\services app\redis app\workers app\utils app\templates app\static

## User Management
    User Registration
    Login
    Logout
    Access Token
    Refresh Token
    Role-Based Authorization (Admin/User)
**Endpoints**
GET /users/me
PUT /users/me

GET /admin/users
PATCH /admin/users/{id}/status
GET /admin/email-queue
## otp service
    Email Verification
    Forgot Password
    Resend OTP
**redis ttl**
    otp:user@gmail.com
    Expires in 5 minutes

## Redis Features
    OTP Storage
    User Profile Cache
    Dashboard Cache
    Rate Limiting
    Background Email Queue

## Admin Features
    View Users
    Activate/Deactivate Users
    Send Notifications
    View Email Queue Statistics

## Frontend
    HTML/Jinja templates
    Login page
    Register page
    Dashboard
    Admin panel

## rate limiting
Login:
5 requests/minute

OTP:
3 requests/minute

Register:
10 requests/minute

## Cache API
Cache user profile
Cache dashboard response

## Background Email Queue
API
↓
Push to Redis Queue
↓
Return Response
↓
Background Worker Sends Email

## git branch
main
│
develop
│
├── feature/auth
├── feature/otp
├── feature/cache
├── feature/rate-limiter
├── feature/email-queue
├── feature/frontend
└── feature/docker


# Technologies
| Component        | Technology       |
| ---------------- | ---------------- |
| Backend          | FastAPI          |
| Database         | PostgreSQL       |
| Cache & Queue    | Redis            |
| ORM              | SQLAlchemy Async |
| Migrations       | Alembic          |
| Authentication   | JWT              |
| Containerization | Docker           |
| Testing          | Pytest           |
| Frontend         | Jinja2           |


## Authentication Flow
Register
   ↓
Generate OTP
   ↓
Store OTP in Redis
   ↓
Send Email via Queue
   ↓
Verify Email
   ↓
Login
   ↓
Access Token + Refresh Token

**Endpoints**
POST /auth/register
POST /auth/verify-email
POST /auth/login
POST /auth/refresh
POST /auth/logout
POST /auth/forgot-password
POST /auth/reset-password

## Forgot Password
Forgot Password
      ↓
Generate OTP
      ↓
Store in Redis
      ↓
Email Queue
      ↓
Verify OTP
      ↓
Reset Password

## Outcomes

After this project I'll know:

FastAPI architecture
Redis fundamentals
Caching
Queues
Rate limiting
JWT
Background workers
Production folder structure
Docker
API documentation
System design concepts