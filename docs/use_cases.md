# Розроблення функціональних вимог до системи

## Модель прецедентів

### Загальна схема

![general-use-case-diagram.png](../src/images/general-use-case-diagram.png)

### Користувач

![user-use-case-diagram.png](../src/images/user-use-case-diagram.png)

### Адміністратор

![admin-use-case-diagram.png](../src/images/admin-use-case-diagram.png)


## Сценарії використання

| ID:                | ` CreateAccount ` |
| :------------------| :--------------|     
| Назва:             | Створення акаунту |
| Учасники:          | Користувач, система |
| Передумови:        | Користувач не має акаунту в системі |
| Результат:         |  <div style="width:300px">Створено новий акаунт</div> |
| Виключні ситуації: | - Обов’язкові поля не заповнені — ` NullReferenceException `<br>- Акаунт вже існує — ` UserAlreadyExistsException `<br>- Пароль не відповідає вимогам — ` NotStrongPasswordException ` |
| Основний сценарій: | 1. Користувач відкриває форму реєстрації<br>2. Вводить необхідні дані<br>3. Натискає "Зареєструватися"<br>4. Перевіряється коректність введених даних<br>5. Якщо всі перевірки пройдені, створюється акаунт |

![CreateAccount Diagram](www.plantuml.com/plantuml/png/ZLBDIW9H5Dxx51TRjn8t6c4Bjn953s1wCs6QaPah6Sp2qSnD9CGmGX3X6zYWP9EZht3E6tNk6KOdA4ZG-tFFztC-JyLHTLjrRuoS2o-mmJwiqCC13Y64EOxTdA0FrvHvMnBmZ04i8DAbNEGBl6Va6eU2bYNwJD6djmSCSBf7Kls6i2jwVHGGmvAExpXYmXW3GSjSRtQ8L-8OQ4iGiH8jCM6s495M7gPqcH7KhbC0Jl892_-uC4iQ8yarpDsK_ut0H00X1WIVeA-TQR1Msl1JHA2OdZqsJG8XNIxe6nFZAB7CsqJEj9GKThjrhSI1R1GBnG9V7rqUw_vNHFk5JpZcTj7ZA8PfKALTwQ6eTGtZJ5v9MveDMUqrP4UrBJDJSE58-yImPRrvL-sr7UNyLbIprBcoBRDrMdUSMyjk_YoIPfCDyo7DP4ODXxfvykaBpZiauvz2_rdaFe1eV_L1tMzrjDcm_vwaVUGuoeo27XmlbTNH_bVFKLQddAjG7pJ2tm00) 

| ID:                | ` EditAccount ` |
| :------------------| :--------------|      
| Назва:             | Редагування інформації акаунту |
| Учасники:          | Користувач, система |
| Передумови:        | Користувач авторизований |
| Результат:         | <div style="width:500px">Оновлена інформація про акаунт</div> |
| Виключні ситуації: | - Некоректний формат даних — ` InvalidDataException ` |
| Основний сценарій: | 1. Користувач переходить у налаштування акаунту<br>2. Вносить зміни<br>3. Натискає "Зберегти"<br>4. Перевіряється коректність введених даних<br>5. Якщо все коректно, оновлюється інформація про акаунт |

![EditAccount Diagram](www.plantuml.com/plantuml/png/VLBDJi9W4BptARxWsHFX0iPmq8EFKQ5H4Ym4g_7G0pyY7emaXa1YeiOtg1LZKsXzXTatShxlWv9uiCtNR7TdPsQthLy6RY-ukcWx8PwHIn-936Ge8yI8P18wYfV1r4nOLNZ3b_HvniYnH4BmWvAHGeO8ApRTRzkPoMIg6AIy8oOpNIg8dWZ8PR2Xm3VMCcSgAG0lR1fgGwPzfafOuCEgurDNIXPg7Y7UhNSMruZ2FtOHorpwCfMPLYEEnbBaffIoAMDvO8t4Y9bSyj2CZ1N3o8PMpky4dkgrpiu3jUSrAkLAsQGFJW_rJ0bIhEHH9ffIRSORqVyT5HRL0hglJlnhjzrg7hc1UtpJyBf1g-ERikStZSXsX5UzACI6TcTVBqjkpGXhIyyaVlYQAqIxZTSSm_Flz-rqQqwTilmHVW40)

| ID:                | ` DeleteAccount ` |
| :------------------| :--------------|
| Назва:             | Видалення акаунту |
| Учасники:          | Користувач, система |
| Передумови:        | Користувач авторизований |
| Результат:         | Акаунт видалено |
| Виключні ситуації: | - Користувач не підтвердив видалення — ` CancelledOperationException ` |
| Основний сценарій: | 1. Користувач переходить у налаштування<br>2. Обирає "Видалити акаунт"<br>3. Підтверджує дію<br>4. Видаляється акаунт |

![DeleteAccount Diagram](www.plantuml.com/plantuml/png/VP51IiDW48NtESLGrwvADwr8GLnxXfZ-Q24c8KPmaKNQe7KXBOX4SA5uWrXI2Qtj6TxSoETV4dSc15w6xysRV_xXTUB6oSsLxwHunKupr3hHgUPOejHPwWWVomoix0lUiTACtnrsg50JVXJD1LkKsD3qqDXPsUgYzRtXatH6ubawU4ADoZhO0RLGhlcMcjCqxVobQO6AnDAcLlZId7wM2ftleI1CZCJZYyj43epNw_QwjdnqVYmsPOsDpdN6jeNen0wSC-UU7LxwBNee9sxW6TytexF8n6uo3eFJMyz4ly9I9XZPBCV-fVZOhmehVADCctdRS-c2SrAqPneqnd_s74O3PyWWNiWF)

| ID:                |<div style="width:500px">` CreateProject `</div>   |
| :------------------| :--------------|      
| Назва:             | Створення проєкту |
| Учасники:          | Користувач, система |
| Передумови:        | Користувач авторизований |
| Результат:         | Створено новий проєкт |
| Виключні ситуації: | - Некоректно введені дані — ` InvalidDataException ` |
| Основний сценарій: | 1. Користувач натискає "Створити проєкт"<br>2. Заповнює необхідні поля<br>3. Підтверджує дію<br>4. Перевіряється коректність введених даних<br>5. Якщо все коректно, створюється проєкт |

![CreateProject Diagram](www.plantuml.com/plantuml/png/VL7FIW9n4BxlKmnsxYHUDC937NgCJPSIR1Nx5HtsO8fv2OKGXI32DzWM3T7KL_ZcZVgShHzqIL36-VvyC_Ehthgmu-vkca62L-oqYvK-Qa_xo93gC0c47-DKh2mBtWZq3ZIiMKsaW3d_PpzY8e8zonsMM6klu7KpfDYpdM6h8-gm9ME73nte50isfsBuHiTUytw0p7sfNP8-jKybMrCTvIJxIJ3FvwRZ5zB4oqssH4P-LySwuMRFv8q5QvlNHZn4iqb86CGeBFZTqd4WBDEypEFYbekaqxYwTd8KrKh5Kj7Q9vUdWXUiQBlXSaFRXXTQsIbJVMB2hEofnt8HtuVDHlqiTE7vGorgkqOhDZYAwnRokuA_BMtz-7ykN0cC--_xjTgLe4fhFlGt)


