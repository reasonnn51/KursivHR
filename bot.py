from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    ContextTypes, ConversationHandler, filters
)
import csv
from datetime import datetime

CHOOSING_COMPANY, ENTER_NAME, ENTER_POSITION, ENTER_BIRTHDATE, ENTER_ABOUT = range(5)

COMPANY_LIST = [
    "Kursiv Media",
    "Qalam",
    "Clover Street Production",
    "Tatler Kazakhstan",
    "URTG",
    "Oninvestment",
    "Kursiv Media Holding"
]

MANAGER_CHAT_ID = -1002516885172
manager_menu = ReplyKeyboardMarkup([
    [KeyboardButton("Как открыть вакансию")],
    [KeyboardButton("Как нанять сотрудника")],
    [KeyboardButton("Как уволить сотрудника")],
    [KeyboardButton("Как утвердить отпуск сотруднику")],
    [KeyboardButton("Как согласовать премию сотруднику")],
    [KeyboardButton("🔙 Назад в главное меню")]
], resize_keyboard=True)

feedback_full_menu = ReplyKeyboardMarkup([
    [KeyboardButton("📬 Написать в HR")],
    [KeyboardButton("📬 Написать в IT")],
    [KeyboardButton("🔙 Назад в главное меню")]
], resize_keyboard=True)

main_menu = ReplyKeyboardMarkup([
    [KeyboardButton("🆕 Я новый сотрудник")],
    [KeyboardButton("👨‍💼 Я действующий сотрудник")],
    [KeyboardButton("🧑‍💼 Я руководитель")],
    [KeyboardButton("📬 Обратная связь")],
    [KeyboardButton("🔗 Полезные ссылки")],
], resize_keyboard=True)

new_employee_menu = ReplyKeyboardMarkup([
    [KeyboardButton("📥 Давай знакомиться")],
    [KeyboardButton("ℹ️ Полезная информация")],
    [KeyboardButton("🔙 Назад в главное меню")]
], resize_keyboard=True)

current_employee_menu = ReplyKeyboardMarkup([
    [KeyboardButton("🏖 Отпуск")],
    [KeyboardButton("🤒 Больничный"), KeyboardButton("📄 Справки")],
    [KeyboardButton("📝 Изменение личных данных")],
    [KeyboardButton("🛠 Техподдержка"), KeyboardButton("📉 Проблема с Битрикс")],
    [KeyboardButton("🏠 Удалёнка"), KeyboardButton("🎓 Обучение")],
    [KeyboardButton("🔙 Назад в главное меню")]
], resize_keyboard=True)

company_menu = ReplyKeyboardMarkup(
    [[KeyboardButton(c)] for c in COMPANY_LIST] + [[KeyboardButton("🔙 Назад в главное меню")]],
    resize_keyboard=True
)

back_only_keyboard = ReplyKeyboardMarkup([
    [KeyboardButton("🔙 Назад в главное меню")]
], resize_keyboard=True)

context_menu = ReplyKeyboardMarkup([
    [KeyboardButton("ℹ️ Полезная информация")],
    [KeyboardButton("📬 Обратная связь"), KeyboardButton("🔗 Полезные ссылки")],
    [KeyboardButton("🔙 Назад в главное меню")]
], resize_keyboard=True)

info_block_menu = ReplyKeyboardMarkup([
    [KeyboardButton("❓ Что нужно сделать в первую неделю?")],
    [KeyboardButton("📄 Где найти документы?")],
    [KeyboardButton("🔐 Как получить доступы?")],
    [KeyboardButton("👥 Контакты HR, IT и бухгалтерии")],
    [KeyboardButton("🔁 Основные процессы")],
    [KeyboardButton("🔙 Назад в главное меню")]
], resize_keyboard=True)

def save_user_data_to_csv(user_data):
    filename = "hr_data.csv"
    fieldnames = ["Дата", "Компания", "ФИО", "Должность", "Дата рождения", "О себе"]
    row = {
        "Дата": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Компания": user_data.get("company"),
        "ФИО": user_data.get("name"),
        "Должность": user_data.get("position"),
        "Дата рождения": user_data.get("birthdate"),
        "О себе": user_data.get("about")
    }
    try:
        with open(filename, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(row)
    except Exception as e:
        print(f"Ошибка при сохранении CSV: {e}")

def format_user_data(user_data):
    return (
        f"📩 *Новая анкета сотрудника:*"

        f"🏢 Компания: {user_data.get('company')}"
        f"👤 ФИО: {user_data.get('name')}"
        f"💼 Должность: {user_data.get('position')}"
        f"🎂 Дата рождения: {user_data.get('birthdate')}"
        f"📝 О себе: {user_data.get('about')}"
    )


manager_menu = ReplyKeyboardMarkup([
    [KeyboardButton("Как открыть вакансию")],
    [KeyboardButton("Как нанять сотрудника")],
    [KeyboardButton("Как уволить сотрудника")],
    [KeyboardButton("Как утвердить отпуск сотруднику")],
    [KeyboardButton("Как согласовать премию сотруднику")],
    [KeyboardButton("🔙 Назад в главное меню")]
], resize_keyboard=True)

feedback_full_menu = ReplyKeyboardMarkup([
    [KeyboardButton("📬 Написать в HR")],
    [KeyboardButton("📬 Написать в IT")],
    [KeyboardButton("🔙 Назад в главное меню")]
], resize_keyboard=True)

main_menu = ReplyKeyboardMarkup([
    [KeyboardButton("🆕 Я новый сотрудник")],
    [KeyboardButton("👨‍💼 Я действующий сотрудник")],
    [KeyboardButton("🧑‍💼 Я руководитель")],
    [KeyboardButton("📬 Обратная связь")],
    [KeyboardButton("🔗 Полезные ссылки")],
], resize_keyboard=True)

new_employee_menu = ReplyKeyboardMarkup([
    [KeyboardButton("📥 Давай знакомиться")],
    [KeyboardButton("ℹ️ Полезная информация")],
    [KeyboardButton("🔙 Назад в главное меню")]
], resize_keyboard=True)

current_employee_menu = ReplyKeyboardMarkup([
    [KeyboardButton("🏖 Отпуск")],
    [KeyboardButton("🤒 Больничный"), KeyboardButton("📄 Справки")],
    [KeyboardButton("📝 Изменение личных данных")],
    [KeyboardButton("🛠 Техподдержка"), KeyboardButton("📉 Проблема с Битрикс")],
    [KeyboardButton("🏠 Удалёнка"), KeyboardButton("🎓 Обучение")],
    [KeyboardButton("🔙 Назад в главное меню")]
], resize_keyboard=True)

company_menu = ReplyKeyboardMarkup(
    [[KeyboardButton(c)] for c in COMPANY_LIST] + [[KeyboardButton("🔙 Назад в главное меню")]],
    resize_keyboard=True
)

back_only_keyboard = ReplyKeyboardMarkup([
    [KeyboardButton("🔙 Назад в главное меню")]
], resize_keyboard=True)

context_menu = ReplyKeyboardMarkup([
    [KeyboardButton("ℹ️ Полезная информация")],
    [KeyboardButton("📬 Обратная связь"), KeyboardButton("🔗 Полезные ссылки")],
    [KeyboardButton("🔙 Назад в главное меню")]
], resize_keyboard=True)

info_block_menu = ReplyKeyboardMarkup([
    [KeyboardButton("❓ Что нужно сделать в первую неделю?")],
    [KeyboardButton("📄 Где найти документы?")],
    [KeyboardButton("🔐 Как получить доступы?")],
    [KeyboardButton("👥 Контакты HR, IT и бухгалтерии")],
    [KeyboardButton("🔁 Основные процессы")],
    [KeyboardButton("🔙 Назад в главное меню")]
], resize_keyboard=True)

def save_user_data_to_csv(user_data):
    filename = "hr_data.csv"
    fieldnames = ["Дата", "Компания", "ФИО", "Должность", "Дата рождения", "О себе"]
    row = {
        "Дата": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Компания": user_data.get("company"),
        "ФИО": user_data.get("name"),
        "Должность": user_data.get("position"),
        "Дата рождения": user_data.get("birthdate"),
        "О себе": user_data.get("about")
    }
    try:
        with open(filename, mode="a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(row)
    except Exception as e:
        print(f"Ошибка при сохранении CSV: {e}")


manager_menu = ReplyKeyboardMarkup([
    [KeyboardButton("Как открыть вакансию")],
    [KeyboardButton("Как нанять сотрудника")],
    [KeyboardButton("Как уволить сотрудника")],
    [KeyboardButton("Как утвердить отпуск сотруднику")],
    [KeyboardButton("Как согласовать премию сотруднику")],
    [KeyboardButton("🔙 Назад в главное меню")]
], resize_keyboard=True)

feedback_menu = ReplyKeyboardMarkup([
    [KeyboardButton("📬 Написать в HR")],
    [KeyboardButton("📬 Написать в IT")],
    [KeyboardButton("🔙 Назад в главное меню")]
], resize_keyboard=True)


main_menu = ReplyKeyboardMarkup([
    [KeyboardButton("🆕 Я новый сотрудник")],
    [KeyboardButton("👨‍💼 Я действующий сотрудник")],
    [KeyboardButton("🧑‍💼 Я руководитель")],
    [KeyboardButton("📬 Обратная связь")],
    [KeyboardButton("🔗 Полезные ссылки")],
], resize_keyboard=True)

new_employee_menu = ReplyKeyboardMarkup([
    [KeyboardButton("📥 Давай знакомиться")],
    [KeyboardButton("ℹ️ Полезная информация")],
    [KeyboardButton("🔙 Назад в главное меню")]
], resize_keyboard=True)

current_employee_menu = ReplyKeyboardMarkup([
    [KeyboardButton("🏖 Отпуск"), ],
    [KeyboardButton("🤒 Больничный"), KeyboardButton("📄 Справки")],
    [KeyboardButton("📝 Изменение личных данных")],
    [KeyboardButton("🛠 Техподдержка"), KeyboardButton("📉 Проблема с Битрикс")],
    [KeyboardButton("🏠 Удалёнка"), KeyboardButton("🎓 Обучение")],
    [KeyboardButton("🔙 Назад в главное меню")]
], resize_keyboard=True)

company_menu = ReplyKeyboardMarkup([[KeyboardButton(c)] for c in COMPANY_LIST] + [[KeyboardButton("🔙 Назад в главное меню")]], resize_keyboard=True)

back_only_keyboard = ReplyKeyboardMarkup([
    [KeyboardButton("🔙 Назад в главное меню")]
], resize_keyboard=True)

feedback_menu = ReplyKeyboardMarkup([
    [KeyboardButton("🔙 Назад в главное меню")]
], resize_keyboard=True)

context_menu = ReplyKeyboardMarkup([
    [KeyboardButton("ℹ️ Полезная информация")],
    [KeyboardButton("📬 Обратная связь"), KeyboardButton("🔗 Полезные ссылки")],
    [KeyboardButton("🔙 Назад в главное меню")]
], resize_keyboard=True)

info_block_menu = ReplyKeyboardMarkup([
    [KeyboardButton("❓ Что нужно сделать в первую неделю?")],
    [KeyboardButton("📄 Где найти документы?")],
    [KeyboardButton("🔐 Как получить доступы?")],
    [KeyboardButton("👥 Контакты HR, IT и бухгалтерии")],
    [KeyboardButton("🔁 Основные процессы")],
    [KeyboardButton("🔙 Назад в главное меню")]
], resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.clear()
    await update.message.reply_text(
        "Привет! Я HR-бот нашего холдинга. Чем могу помочь? 😊",
        reply_markup=main_menu
    )
    return ConversationHandler.END

async def choose_company(update: Update, context: ContextTypes.DEFAULT_TYPE):
    company = update.message.text
    if company == "🔙 Назад в главное меню":
        return await cancel(update, context)
    if company not in COMPANY_LIST:
        await update.message.reply_text("Пожалуйста, выберите компанию из списка ⬇️", reply_markup=company_menu)
        return CHOOSING_COMPANY
    context.user_data['company'] = company
    context.user_data['survey_step'] = "ENTER_NAME"
    await update.message.reply_text("Введите ваше ФИО:", reply_markup=back_only_keyboard)
    return ENTER_NAME

async def enter_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == "🔙 Назад в главное меню":
        return await cancel(update, context)
    context.user_data['name'] = update.message.text
    context.user_data['survey_step'] = "ENTER_POSITION"
    await update.message.reply_text("Введите вашу должность:")
    return ENTER_POSITION

async def enter_position(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == "🔙 Назад в главное меню":
        return await cancel(update, context)
    context.user_data['position'] = update.message.text
    context.user_data['survey_step'] = "ENTER_BIRTHDATE"
    await update.message.reply_text("Введите дату рождения (ДД.ММ.ГГГГ):")
    return ENTER_BIRTHDATE

async def enter_birthdate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == "🔙 Назад в главное меню":
        return await cancel(update, context)
    context.user_data['birthdate'] = update.message.text
    context.user_data['survey_step'] = "ENTER_ABOUT"
    await update.message.reply_text("Кратко расскажите о себе:")
    return ENTER_ABOUT

async def enter_about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == "🔙 Назад в главное меню":
        return await cancel(update, context)

    context.user_data['about'] = update.message.text
    context.user_data.pop('survey_step', None)

    # Сохраняем в CSV
    save_user_data_to_csv(context.user_data)

    # Формируем текст
    message_text = format_user_data(context.user_data)

    # Отправка в канал
    await context.bot.send_message(
        chat_id=MANAGER_CHAT_ID,
        text=message_text,
        parse_mode="Markdown"
    )

    # Ответ пользователю
    summary = (
        f"✅ Данные собраны:\n"
        f"🏢 Компания: {context.user_data['company']}\n"
        f"👤 ФИО: {context.user_data['name']}\n"
        f"💼 Должность: {context.user_data['position']}\n"
        f"🎂 Дата рождения: {context.user_data['birthdate']}\n"
        f"📝 О себе: {context.user_data['about']}"
    )
    await update.message.reply_text(summary)
    await update.message.reply_text("Спасибо за информацию!\nЧем могу помочь?", reply_markup=context_menu)
    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data.pop('survey_step', None)
    await update.message.reply_text("Отмена. Возвращаюсь в главное меню ⬅️", reply_markup=main_menu)
    return ConversationHandler.END

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    text = update.message.text

    if text == "Назад в меню":
        await update.message.reply_text("Главное меню:", reply_markup=context_menu)
        return


    if text == "🆕 Я новый сотрудник":
        await update.message.reply_text("Выберите действие ⬇️", reply_markup=new_employee_menu)
    elif text == "👨‍💼 Я действующий сотрудник":
        await update.message.reply_text("Выберите интересующий раздел ⬇️", reply_markup=current_employee_menu)
    elif text == "📥 Давай знакомиться":
        await update.message.reply_text("Выберите компанию из списка ⬇️", reply_markup=company_menu)
        return CHOOSING_COMPANY
    elif text == "🧑‍💼 Я руководитель":
        await update.message.reply_text("Выберите интересующий раздел ⬇️", reply_markup=manager_menu)
    elif text == "ℹ️ Полезная информация":
        await update.message.reply_text("Выберите пункт информационного блока ⬇️", reply_markup=info_block_menu)
    elif text == "🔙 Назад в главное меню":
        return await cancel(update, context)
    elif text == "❓ Что нужно сделать в первую неделю?":
        await update.message.reply_text(
            "📝 *Чек-лист первой недели:*\n"
            "1️⃣ Подпишите все документы — HR-отдел (506 кабинет, +7 701 191 1296)\n"
            "2️⃣ Получите доступы — IT-отдел (512 кабинет, +7 775 505 2351)\n"
            "3️⃣ Заполните профиль в Битрикс\n"
            "4️⃣ Ознакомьтесь с рабочим местом\n"
            "5️⃣ Познакомьтесь с командой\n"
            "6️⃣ Пройдите вводный инструктаж\n"
            "7️⃣ Ознакомьтесь с внутренними политиками",
            parse_mode="Markdown",
            reply_markup=back_only_keyboard
        )
        
    elif text == "📄 Где найти документы?":
        await update.message.reply_text("📄 Документы можно получить в HR-отделе (506 кабинет) или запросить по WhatsApp/Telegram: +7 701 191 1296", reply_markup=back_only_keyboard)
    elif text == "🔐 Как получить доступы?":
        await update.message.reply_text("🔐 По вопросам доступов обратитесь в IT-отдел (512 кабинет) или позвоните: +7 775 505 2351", reply_markup=back_only_keyboard)
    elif text == "👥 Контакты HR, IT и бухгалтерии":
        await update.message.reply_text(
            "📇 Контакты:\n\n"
            "HR: Малика Абдиманап — m.abdimanap@kursiv.media | +7 701 191 1296\n"
            "IT: Дени Умаев — +7 775 505 2351 | Арафат Иминжан — @arafat_blaugrana\n"
            "Офис-менеджер: Даминика Вавулиди — @anteliya0\n"
            "Бухгалтерия: Алина Нураликызы — chiefbuh@kursiv.media\n"
            "Tatler: Алма Айтмуратова — a.aitmuratova@tatlerasia.kz\n"
            "Qalam, Clover, Oninvestment: Арман Немасипов — buh@cloverstreet.pro",
            reply_markup=back_only_keyboard
        )
    elif text == "🔁 Основные процессы":
       await update.message.reply_text("🗂️ Основные процессы: рабочее время(Пн–Пт, с 9:00 до 18:00 или с 10:00 до 19:00, время согласовывется, исходя из работы вашего дерартамента / отдела, а удаленку можно оформить по согласованию с руководителем через Битрикс)\n Коммуникации(Битрикс, рабочие чаты в WhatsApp и Telegram)\n Имеется корпоративный Telegram канал холдинга\n Техника (предоставляется, запрос через руководителя и IT)\n Обычно принято обращаться по имени, стиль одежды - не ограничивается, но важно учитывать офисный формат работы.", reply_markup=back_only_keyboard)
    elif text == "🏖 Отпуск":
        await update.message.reply_text(
            "🏖 *Инструкция по отпуску:*\n"
            "1) Уточните в отделе кадров (506 кабинет, WhatsApp/Telegram: +7 701 191 1296) количество отпускных дней\n"
            "2) Согласуйте с руководителем даты\n"
            "3) Заполните заявку в Битрикс: Заявления -> Отпуск -> Создать\n"
            "4) Ожидайте сообщения от отдела кадров\n"
            "5) Отпуск считается оформленным после подписания вами соответствующего Приказа",
            parse_mode="Markdown",
            reply_markup=back_only_keyboard
        )
    elif text == "📬 Обратная связь": 
        await update.message.reply_text("Выберите действие ⬇️", reply_markup=feedback_menu)
        await update.message.reply_text(
                "📬 *Обратная связь:*\n"
                "1) Напишите в HR-отдел (WhatsApp/Telegram: +7 701 191 1296 / @@dinaraurozbayeva) или IT-отдел (WhatsApp/Telegram: +7 775 505 2351 / @reasonnn51)\n"
                "2) Форма для анонимного сообщения https://forms.gle/RDnkdi9abLAVj8s19\n"
                "3) Ожидайте ответа",
                parse_mode="Markdown",
                reply_markup=feedback_menu
            )

        # Кнопки руководителя
    elif text == "Как открыть вакансию":
        await update.message.reply_text(
            "📌 *Как открыть вакансию:*\n"
            "1️⃣ Убедитесь, что вакансия есть в штатном расписании (доступ к ШР можно получить у HR-директора)\n"
            "2️⃣ Если в вашем отделе уже есть сотрудники с аналогичной должностью, зарплата должна совпадать\n"
            "3️⃣ Заполните заявку на вакансию по ссылке: [форма заявки](https://forms.gle/Q5wKm7e9xxQViTvT6)\n"
            "4️⃣ Ваша вакансия будет опубликована на ресурсах компании в течение 1 рабочего дня",
            parse_mode="Markdown",
            reply_markup=back_only_keyboard
        )
    elif text == "Как нанять сотрудника":
        await update.message.reply_text(
            "👥 *Как нанять сотрудника* \n "    
            "1️⃣ После того, как вы выбрали кандидата,уведомите отдел кадров (WhatsApp/Telegram: + 7 701 191 1296), они свяжутся с новым сотрудником, запросят необходимые документы и проверят возможность трудоустройства \n"
            "2️⃣ Запустите служебную записку (СЗ) через Битрикс: Заявления -> Прием сотрудника -> Создать \n"
            "3️⃣ После согласования СЗ вам придет уведомление о формировании Приказа \n"
            "4️⃣ В первую неделю помогите сотруднику разобраться в основных процессах",
            reply_markup=back_only_keyboard
            )
    elif text == "Как уволить сотрудника":
        await update.message.reply_text(
            "📤 *Как уволить сотрудника* \n"
            "1️⃣ Перед принятием решения об увольнении помните, что для этого должны быть веские основания - убедитесь, что ситуацию нельзя решить иным способом (разговором, предупреждением, выговором и т.д.)\n"
            "2️⃣ Обсудите ситуацию с HR-директором\n"
            "3️⃣ После принятия решения сотрудник напишет заявление по собственному желанию / соглашению сторон через Битриксь",
            reply_markup=back_only_keyboard
            )
    elif text == "Как утвердить отпуск сотруднику":
        await update.message.reply_text(
            "🏖 *Как утвердить отпуск* \n" 
            "1️⃣ Уточните в отделе кадров (506 кабинет, WhatsApp/Telegram: + 7 701 191 1296) количество отпускных дней\n"
            "2️⃣ Согласуйте даты отпуска\n"
            "3️⃣ Заполните заявку в Битрикс: Заявления -> Отпуск -> Создать \n"
            "4️⃣ Ожидайте сообщения от отдела кадров\n"
            "5️⃣ Отпуск считается оформленным после подписания Приказа",
            reply_markup=back_only_keyboard
            )
    elif text == "Как согласовать премию сотруднику":
        await update.message.reply_text(
            "💰 *Как согласовать премию сотруднику:*\n" \
            " 1️⃣ Убедитесь, что в бюджете заложена сумма\n" 
            " 2️⃣ Согласуйте премию с финансовым менеджером \n"
            " 3️⃣ Запустите СЗ в Битрикс: Согласования -> Премирование  -> Создать \n"
            " 4️⃣ После согласования СЗ вам придет уведомление",
            reply_markup=back_only_keyboard)

    elif text == "🤒 Больничный":
        await update.message.reply_text(
            "🤒 *Инструкция при болезни:*\n"
            "1) Уведомьте руководителя и отдел кадров (WhatsApp/Telegram: +7 701 191 1296)\n"
            "2) При закрытии больничного листа принесите справку в отдел кадров\n"
            "3) Отдел кадров передаст информацию в бухгалтерию",
            parse_mode="Markdown",
            reply_markup=back_only_keyboard
        )
    elif text == "📄 Справки":
        await update.message.reply_text(
            "📄 *Получение справок:*\n"
            "1) Напишите на номер отдела кадров (WhatsApp/Telegram: +7 701 191 1296), что вам нужна справка с места работы, укажите:\n"
            "  — Период\n"
            "  — Цель (банк, виза и т.д.)\n"
            "  — Формат (PDF, оригинал на бумаге)\n"
            "  — На каком языке\n"
            "2) Ожидайте сообщения от отдела кадров о готовности справки",
            parse_mode="Markdown",
            reply_markup=back_only_keyboard
        )
    elif text == "🛠 Техподдержка":
        await update.message.reply_text(
            "🛠 *Техподдержка:*\n"
            "1) Пишите IT-поддержке: WhatsApp/Telegram: +7 775 505 2351, 512 кабинет\n"
            "2) Укажите: модель устройства, суть проблемы\n"
            "3) Желательно приложить скриншот",
            parse_mode="Markdown",
            reply_markup=back_only_keyboard
        )
    elif text == "📉 Проблема с Битрикс":
        await update.message.reply_text(
            "📉 *Проблемы с Битрикс:*\n"
            "1) Пишите IT-поддержке (WhatsApp/Telegram: +7 775 505 2351) или администратору Битрикс (y.galinskaya@kursiv.media, +7 701 932 59 26)\n"
            "2) Укажите суть проблемы\n"
            "3) Желательно приложить скриншот",
            parse_mode="Markdown",
            reply_markup=back_only_keyboard
        )
    elif text == "📝 Изменение личных данных":
        await update.message.reply_text(
            "📝 *Изменение личных данных:*\n"
            "1) Напишите на номер отдела кадров (WhatsApp/Telegram: +7 701 191 1296), что у вас были изменены данные\n"
            "2) Приложите новую информацию\n"
            "3) Отдел кадров подтвердит изменение",
            parse_mode="Markdown",
            reply_markup=back_only_keyboard
        )
    elif text == "🏠 Удалёнка":
        await update.message.reply_text(
            "🏠 *Оформление удалёнки:*\n"
            "1) Обсудите заранее с руководителем (минимум за 1 день до даты удаленной работы)\n"
            "2) Оформите заявку через Битрикс: Заявления -> Удаленка -> Создать\n"
            "3) В Битриксе придет уведомление с подтверждением",
            parse_mode="Markdown",
            reply_markup=back_only_keyboard
        )
    elif text == "🎓 Обучение":
        await update.message.reply_text(
            "🎓 *Обучение и развитие:*\n"
            "1) Скидки от партнеров: Freedom Media, Lerna (за подробностями telegram: @dinaraurozbayeva)\n"
            "2) Корпоративная книжная библиотека\n"
            "3) Возможность пройти внешний курс — уточняйте у руководителя и HR-директора (WhatsApp: +7 701 191 1296)",
            parse_mode="Markdown",
            reply_markup=back_only_keyboard
        )
    else:
        await update.message.reply_text("Пожалуйста, выберите пункт из меню ⬇️")
        

    
async def main():
    app = ApplicationBuilder().token("Здесь вставить ваш токен").build()

    conv_handler = ConversationHandler(
        entry_points=[MessageHandler(filters.Regex("^📥 Давай знакомиться$"), choose_company)],
        states={
            CHOOSING_COMPANY: [MessageHandler(filters.TEXT & ~filters.COMMAND, choose_company)],
            ENTER_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, enter_name)],
            ENTER_POSITION: [MessageHandler(filters.TEXT & ~filters.COMMAND, enter_position)],
            ENTER_BIRTHDATE: [MessageHandler(filters.TEXT & ~filters.COMMAND, enter_birthdate)],
            ENTER_ABOUT: [MessageHandler(filters.TEXT & ~filters.COMMAND, enter_about)],
        },
        fallbacks=[MessageHandler(filters.Regex("^🔙 Назад в главное меню$"), cancel)],
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(conv_handler)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущен...")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    import nest_asyncio

    nest_asyncio.apply()
    asyncio.run(main())
