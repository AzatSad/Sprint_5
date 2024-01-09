class Locators:
    personal_area_button = ".//p[text()='Личный Кабинет']" #кнопка для перехода в "Личный кабинет"
    register_link = ".//a[text()='Зарегистрироваться']" #линк "Зарегистрироваться" для перехода на страницу ввода кредов для регистрации
    entry_field_user_name = "(//input[@name= 'name'])[1]" #поле регистрации имя
    entry_field_user_email = "(//input[@name= 'name'])[2]" #поле регистрации емайл
    entry_field_user_password = "//input[@name= 'Пароль']" #поле регистрации пароль
    register_button = "//button[text()='Зарегистрироваться']" #кнопка зарегистировать нового пользователя
    enter_button = "//button[text()='Войти']" #кнопка войти в личный кабинет
    enter_to_account_button = "//button[contains(text(), 'Войти в аккаунт')]" #кнопка "Войти в аккаунт" на главной странице
    enter_link = ".//a[@href='/login']" #линк "Войти" на странице регистрации
    password_recovery_link = "//a[text()='Восстановить пароль']" #линк "Восстановить пароль"
    authorization_field_login = ".//input[@name='name']" #поле авторизации логин
    authorization_field_password = ".//input[@name='Пароль']" #поле авторизации пароль
    exit_button = ".//button[text()='Выход']" #кнопка выхода из ЛК
    design_order = ".//button[text()='Оформить заказ']"  # кнопка оформления заказа на главной странице
    registration_message_error = ".//p[text()='Некорректный пароль']" #сообщение о ошибке "Некорректный пароль"
    profile_header = "//a[text()='Профиль']" #заголовок "Профиль" на странице профиля
    logo_image_button = 'AppHeader_header__logo__2D0X2' #кнопка логотипа главная страница
    constructor_button = ".//p[text()='Конструктор']" #кнопка перехода в раздел конструктор
    constructor_header = ".//h2[text()='Соберите бургер']" #заголовок "Соберите бургер" конструктора
    tab_filling = ".//span[text()='Начинки']" #таб начинки
    tab_sauce = ".//span[text()='Соусы']" #таб соусы
    tab_buns = ".//span[text()='Булки']" #таб булки
    tab_active_current = "//div[contains(@class, 'tab_tab_type_current')]"#таб в активном состоянии(класс изменяется когда таб активный)




