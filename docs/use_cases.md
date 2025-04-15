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

| ID:                | <div style="width:500px">` EditProject `</div> |
| :------------------| :--------------|      
| Назва:             | Редагування проєкту |
| Учасники:          | Користувач, система |
| Передумови:        | Користувач має дозвіл на редагування |
| Результат:         | Оновлена інформація про проєкт |
| Виключні ситуації: | - Доступ заборонено — ` AccessDeniedException ` |
| Основний сценарій: | 1. Користувач відкриває проєкт<br>2. Вносить зміни<br>3. Натискає "Зберегти"<br>4. Перевіряється коректність введених даних<br>5. Якщо все коректно, зберігаються зміни |

![EditProject Diagram](www.plantuml.com/plantuml/png/VL5DIiDG4Dxd58-wTbMwQKKgw44qVMX0az94S955awBTI0jIKX14l45C3OROr2jySoFdJPAA6nC8apVVV3zlXdvmFWbkRwwj4C_OqHG5HHJJ31bIceUMuaSm0odx2a-Ku0EbWGfefV3DFplaV1Z_mb0nNuI2sHuLFh7bkGh57l32ix6HGoai7QpnZfofScnCfrD3vHFYhNR6pItIi2LvRGOoIcXAIrePDSOj5Kg98wPGSJkgZMJyvXmWDsReNd6PrcKjvtg1LXFdyYfG1zhkTNjTEJwwE3QP2gRzeWND3QLguitO_mChhFjxwA4wiMtj-wVQTVJexCxMuy3nNEbhToGgJOOsDYNOCD6YJV3dpWJxxugyyS0QCZNlyWS0)

| ID:                | <div style="width:500px">` DeleteProject `</div> |
| :------------------| :--------------|      
| Назва:             | Видалення проєкту |
| Учасники:          | Користувач, система |
| Передумови:        | Користувач має права на видалення |
| Результат:         | Проєкт видалено |
| Виключні ситуації: | - Доступ заборонено — ` AccessDeniedException ` |
| Основний сценарій: | 1. Користувач відкриває проєкт<br>2. Натискає "Видалити"<br>3. Підтверджує дію<br>4. Видаляється проєкт |

![DeleteProject Diagram](www.plantuml.com/plantuml/png/VP11IiDW48NtESLGrwvADur81Js8fZyQqAGql-0Y2qt1RgI5KY888juWb4H2glKARsxa_5FyLs8M8VFcotlC6sNsV6flRww372_OyJrQVk22PzYWudaUa3pAXFev9AouH8tEeGgj2TyoxD28M7ZiLLQ5SqEdK0yhjAXHOOlMRNeUVNEE8ctGY56D3vx93oALl0X9gIIrXgRnvPMb0nCD-eE-oaSNnwI-7RQyu3c-k2I9RDq94lie5iz3ZnxIIHIPB3irIMp6PtUHcTWuJNHlal4-XGATSxplkq23JrIvF__t2bxoMcAUX5d-KO6-_YqrdOJ1I6Ab_Hy0)

| ID:                | <div style="width:500px">` AddMembers `</div> |
| :------------------| :--------------|
| Назва:             | Додавання учасників у проєкт |
| Учасники:          | Адміністратор, система |
| Передумови:        | Користувач має права на додавання |
| Результат:         | Додані нові учасники |
| Виключні ситуації: | - Доступ заборонено — ` AccessDeniedException `<br>- Користувач уже в команді — ` UserAlreadyInTeamException ` |
| Основний сценарій: | 1. Адміністратор відкриває налаштування команди<br>2. Додає нових учасників, вводячи їхню пошту або ID<br>3. Перевіряється коректність введених даних<br>4. Якщо все коректно, додаються учасники |

![AddMembers Diagram](www.plantuml.com/plantuml/png/ZLB1Ql9W4BpdAHR-wz-JU36bADY3z_O1RFne1OsIfD123b6nxK6q5D5ZwHlO4E53JVeAks_K-H8CjQSAmcPsTcTcaxeVjBtWlj-pGdxbX0-oubHMCfAnHBoHCMSIXHRXbpFjlAmHlu6Oy0uapJ68I-AKDxn7-OBPYG61fB8Wtd761_E82LrkM09DZfCP-5gc91Dv1ZO2f7a7ZVW_eHKRhYpGqoHhcMBldFYBiqACiFoJCserRI8h5mZvWxM9mLkZ7HvLttah4R0O8IDiN69-1bvXqxGWEovlCClL0IRufxb5OxeeYoZk853aTM_l0lgdd6gbMidXyviBNCcauBtCuHmh2S6qCOo8Jr1Orqhg6JKSH_b-KxbTrRbySDGmw0xS7_rhNtcDdgVQdSUMUwNQ_LEISZk5bT_tdPS9Ju_BsYvEzOStFnZQLXqA-52-0G00)



