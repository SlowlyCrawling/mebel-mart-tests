class APIConfig:
    BASE_URL = "https://apimocker.com"  # Публичное API, без регистрации
    
    ENDPOINTS = {
        "users": "/users",
        "posts": "/posts",
        "comments": "/comments",
        "products": "/products",  # Не существует, но можешь добавить свой мок
        "cart": "/cart"
    }