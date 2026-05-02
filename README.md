# OMS - Order Management System

### Статус проекта: даже не MVP:<

![Python](https://img.shields.io/badge/Python-3.12%2B-blue)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?logo=fastapi) 
![Pydantic](https://img.shields.io/badge/Pydantic-E92063?logo=pydantic) 
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?logo=sqlalchemy) 
![Uvicorn](https://img.shields.io/badge/Uvicorn-499848?logo=uvicorn) 

### Установка зависимостей <3

![install req](assets/install_r.gif)

## 📂 Структура проекта

```python
OMS/
├── api/
│   ├── dto/
│   │   ├── schema/
│   │   │   ├── order.py
│   │   │   ├── orderItem.py
│   │   │   ├── product.py
│   │   │   └── user.py
│   │   ├── __init__.py
│   │   └── dependency.py
│   └── __init__.py
├── repository/
│   ├── model/
│   │   ├── dependency.py
│   │   ├── order.py
│   │   ├── orderItem.py
│   │   ├── product.py
│   │   └── user.py
│   ├── repo/
│   │   └── user.py
│   └── __init__.py
├── service/
│   └── __init__.py
├── .env
├── .gitignore
├── config.py
├── core.py
├── exception.py
├── README.md
└── requirements.txt

```
