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

Browser
    ↓
FastAPI
    ↓
Service Layer
    ↓
Repository Layer
    ↓
PostgreSQL

Redis
├── OTP
├── Cache
├── Queue
└── Rate Limiter


## structure
notification-hub/

app/
│
├── api/
│   ├── auth.py
│   ├── users.py
│   ├── otp.py
│   └── admin.py
│
├── core/
│   ├── config.py
│   ├── security.py
│   └── dependencies.py
│
├── database/
│   ├── session.py
│   └── base.py
│
├── models/
│   ├── user.py
│   └── refresh_token.py
│
├── repositories/
├── services/
├── redis/
├── workers/
├── schemas/
├── templates/
├── static/
├── utils/
└── main.py



## User Management
    User Registration
    Login
    Logout
    Access Token
    Refresh Token
    Role-Based Authorization (Admin/User)

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