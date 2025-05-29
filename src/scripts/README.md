# Реалізація доступу до бази даних

# ✅ TaskBoard API  
Чистий Web API на .NET 8 для управління користувачами, проєктами, дошками, колонками, задачами та коментарями — без Identity, DTO чи AutoMapper.  
Побудовано з використанням EF Core, JWT, BCrypt та OpenAPI.

---

## 🚀 Можливості
- 🔐 Аутентифікація через JWT (без Identity)
- ✅ Повний CRUD для всіх основних сутностей
- 🔁 Зв'язки між задачами та колонками
- 🔎 Документація через Swagger / OpenAPI
- 📦 Підтримка міграцій та початкових даних (Seed)

---

## 🧰 Технології
- ASP.NET Core Web API (.NET 8)
- Entity Framework Core + MySQL
- BCrypt для хешування паролів
- JWT Bearer аутентифікація
- Swagger / OpenAPI

---

## ⚙️ Як запустити

### 1. Клонувати репозиторій
```bash
git clone https://github.com/unxwn/stantsiya-sykhiv.git
cd stantsiya-sykhiv/src/scripts/StantsiyaSykhivApi
```

### 2. Налаштувати UserSecrets
```bash
dotnet user-secrets init
dotnet user-secrets set "ConnectionStrings:DefaultConnection" "your_mysql_conn_string"
dotnet user-secrets set "JwtSettings:SecretKey" "your_super_secret_key"
```
❗ Вкажіть ваш реальний MySQL connection string та SecretKey.

### 3. Застосувати міграції та запустити
```bash
dotnet ef database update
dotnet run
```
API буде доступний за адресою:
https://localhost:{PORT}/swagger

### 👤 Автор
- [unxwn](https://github.com/unxwn)
