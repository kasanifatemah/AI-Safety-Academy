import os
import requests

from dotenv import load_dotenv

from lessons import LESSONS
from quiz import get_quiz

from users import (
    create_user,
    get_user,
    add_xp,
    complete_lesson,
    add_quiz_result,
    add_badge,
    get_level_name,
    record_answer,
    get_quiz_results
)


# =========================================================
# CONFIG
# =========================================================

load_dotenv(override=True)

TOKEN = os.getenv("BALE_BOT_TOKEN")

if not TOKEN:
    raise ValueError(
        "BALE_BOT_TOKEN پیدا نشد. فایل .env را بررسی کنید."
    )

BASE_URL = f"https://tapi.bale.ai/bot{TOKEN}"


# =========================================================
# BALE API
# =========================================================

def send_message(chat_id, text, reply_markup=None):

    url = f"{BASE_URL}/sendMessage"

    data = {
        "chat_id": chat_id,
        "text": text
    }

    if reply_markup is not None:
        data["reply_markup"] = reply_markup

    response = requests.post(
        url,
        json=data,
        timeout=30
    )

    if response.status_code != 200:
        print(
            "SEND ERROR:",
            response.status_code,
            response.text
        )

    return response


# =========================================================
# MAIN MENU
# =========================================================

def main_menu():

    return {
        "keyboard": [
            [
                {"text": "📚 مسیر یادگیری"},
                {"text": "🧠 Quiz Center"}
            ],
            [
                {"text": "🧪 Safety Lab"},
                {"text": "🏆 پروفایل من"}
            ],
            [
                {"text": "ℹ️ درباره آکادمی"}
            ]
        ],
        "resize_keyboard": True
    }


# =========================================================
# LESSON MENU
# =========================================================

def lessons_menu():

    keyboard = []

    for lesson_id, lesson in LESSONS.items():

        keyboard.append([
            {
                "text": (
                    f"📖 درس {lesson_id}: "
                    f"{lesson['title']}"
                )
            }
        ])

    keyboard.append([
        {"text": "🔙 بازگشت به منوی اصلی"}
    ])

    return {
        "keyboard": keyboard,
        "resize_keyboard": True
    }


# =========================================================
# QUIZ MENU
# =========================================================

def quiz_menu():

    keyboard = []

    for lesson_id in LESSONS:

        quiz = get_quiz(lesson_id)

        if quiz:

            keyboard.append([
                {
                    "text": f"🧠 Quiz درس {lesson_id}"
                }
            ])

    keyboard.append([
        {"text": "🔙 بازگشت به منوی اصلی"}
    ])

    return {
        "keyboard": keyboard,
        "resize_keyboard": True
    }


# =========================================================
# WELCOME
# =========================================================

WELCOME_MESSAGE = """
🛡️ AI SAFETY ACADEMY
━━━━━━━━━━━━━━━━━━

سلام، پژوهشگر! 👋

به آکادمی امنیت هوش مصنوعی خوش آمدی.

اینجا فقط قرار نیست AI Safety را بخوانی؛
قرار است یاد بگیری، امتحان بدهی،
XP بگیری و Level خودت را بالا ببری. 🧠

📚 Lessons
🧠 Interactive Quizzes
⭐ XP System
🏆 Levels
🎖️ Badges
🧪 Safety Labs

━━━━━━━━━━━━━━━━━━

🚀 مسیر یادگیری خودت را شروع کن!
"""


# =========================================================
# ABOUT
# =========================================================

ABOUT_MESSAGE = """
ℹ️ ABOUT AI SAFETY ACADEMY
━━━━━━━━━━━━━━━━━━

AI Safety Academy یک محیط آموزشی
تعاملی برای یادگیری امنیت و ایمنی
سیستم‌های هوش مصنوعی است.

در این مسیر با مفاهیمی مانند:

🤖 Large Language Models
🎯 Alignment
🛡️ Refusal Behavior
💉 Prompt Injection

آشنا می‌شوی.

━━━━━━━━━━━━━━━━━━

🎮 امکانات:

📚 Lessons
🧠 Interactive Quizzes
⭐ XP
🏆 Levels
🎖️ Badges
🧪 Safety Labs

🚀 مسیر تازه شروع شده است!
"""


# =========================================================
# SAFETY LAB
# =========================================================

LAB_MESSAGE = """
🧪 SAFETY LAB
━━━━━━━━━━━━━━━━━━

🔬 آزمایشگاه AI Safety

این بخش در حال توسعه است.

به‌زودی می‌توانی سناریوهای آموزشی
امنیت LLMها را تحلیل کنی.

🔍 Analyze
🧠 Predict
🛡️ Defend
⚔️ Challenge

━━━━━━━━━━━━━━━━━━

🔒 STATUS: UNDER DEVELOPMENT
"""


# =========================================================
# PROFILE
# =========================================================

def profile_message(chat_id):

    user = get_user(chat_id)

    level = user["level"]
    xp = user["xp"]

    level_name = get_level_name(level)

    lessons_count = len(
        user["lessons_completed"]
    )

    quizzes_count = user["quizzes_completed"]

    correct = user["correct_answers"]

    total = user["total_answers"]

    if total > 0:
        accuracy = (correct / total) * 100
    else:
        accuracy = 0

    badges = user["badges"]

    if badges:

        badge_text = "\n".join(
            f"🏅 {badge}"
            for badge in badges
        )

    else:

        badge_text = (
            "🔒 هنوز Badge دریافت نکرده‌ای."
        )

    return f"""
🏆 YOUR PROFILE
━━━━━━━━━━━━━━━━━━

{level_name}

⭐ XP: {xp}

🏆 LEVEL: {level}

📚 Lessons:
{lessons_count} / {len(LESSONS)}

🧠 Quiz Attempts:
{quizzes_count}

✅ Correct Answers:
{correct}

📝 Total Answers:
{total}

📊 Accuracy:
{accuracy:.1f}%

━━━━━━━━━━━━━━━━━━

🎖️ BADGES

{badge_text}

━━━━━━━━━━━━━━━━━━

🚀 ادامه بده تا Level بعدی را باز کنی!
"""


# =========================================================
# QUIZ STATE
# =========================================================

QUIZ_STATE = {}


# =========================================================
# START QUIZ
# =========================================================

def start_quiz(chat_id, lesson_id):

    quiz = get_quiz(lesson_id)

    if not quiz:

        send_message(
            chat_id,
            "❌ برای این درس Quiz وجود ندارد.",
            main_menu()
        )

        return

    QUIZ_STATE[chat_id] = {
        "lesson_id": lesson_id,
        "question": 0,
        "score": 0
    }

    send_quiz_question(chat_id)


# =========================================================
# SEND QUESTION
# =========================================================

def send_quiz_question(chat_id):

    state = QUIZ_STATE.get(chat_id)

    if not state:
        return

    lesson_id = state["lesson_id"]
    question_index = state["question"]

    quiz = get_quiz(lesson_id)

    if question_index >= len(quiz):

        finish_quiz(chat_id)

        return

    question = quiz[question_index]

    letters = [
        "🅰️",
        "🅱️",
        "🅲️",
        "🅳️"
    ]

    keyboard = []

    for index, option in enumerate(
        question["options"]
    ):

        keyboard.append([
            {
                "text":
                f"{letters[index]} {option}"
            }
        ])

    keyboard.append([
        {"text": "❌ خروج از Quiz"}
    ])

    markup = {
        "keyboard": keyboard,
        "resize_keyboard": True
    }

    text = f"""
🧠 QUIZ CENTER
━━━━━━━━━━━━━━━━━━

📚 Lesson {lesson_id}

❓ Question {question_index + 1}
از {len(quiz)}

━━━━━━━━━━━━━━━━━━

{question['question']}

👇 پاسخ خود را انتخاب کن:
"""

    send_message(
        chat_id,
        text,
        markup
    )


# =========================================================
# HANDLE QUIZ ANSWER
# =========================================================

def handle_quiz_answer(chat_id, text):

    state = QUIZ_STATE.get(chat_id)

    if not state:
        return False

    lesson_id = state["lesson_id"]
    question_index = state["question"]

    quiz = get_quiz(lesson_id)

    if question_index >= len(quiz):
        return False

    question = quiz[question_index]

    options = question["options"]

    selected = None

    for index, option in enumerate(options):

        if option in text:

            selected = index

            break

    if selected is None:
        return False

    correct = (
        selected == question["answer"]
    )

    # -----------------------------------------------------
    # SAVE EXACT ANSWER
    # -----------------------------------------------------

    record_answer(
        chat_id=chat_id,
        lesson_id=lesson_id,
        question_number=question_index + 1,
        question=question["question"],
        selected_answer=options[selected],
        correct_answer=options[question["answer"]],
        is_correct=correct
    )

    # -----------------------------------------------------
    # UPDATE USER STATISTICS
    # -----------------------------------------------------

    add_quiz_result(
        chat_id,
        correct
    )

    # -----------------------------------------------------
    # CORRECT ANSWER
    # -----------------------------------------------------

    if correct:

        state["score"] += 1

        result = add_xp(
            chat_id,
            50
        )

        send_message(
            chat_id,
            f"""
🔥 CORRECT!

+50 XP ⭐

━━━━━━━━━━━━━━━━━━

⭐ XP: {result['xp']}
🏆 LEVEL: {result['level']}

{get_level_name(result['level'])}
"""
        )

        # First Defender Badge

        if lesson_id == 1:

            if add_badge(
                chat_id,
                "First Defender"
            ):

                send_message(
                    chat_id,
                    """
🎖️ NEW BADGE UNLOCKED!

🛡️ First Defender

اولین قدم امنیتی تو ثبت شد! 🔥
"""
                )

    # -----------------------------------------------------
    # WRONG ANSWER
    # -----------------------------------------------------

    else:

        correct_answer = options[
            question["answer"]
        ]

        send_message(
            chat_id,
            f"""
❌ NOT QUITE!

پاسخ درست:

✅ {correct_answer}

اشکالی ندارد!
یادگیری یعنی آزمون و خطا. 🧠
"""
        )

    # -----------------------------------------------------
    # NEXT QUESTION
    # -----------------------------------------------------

    state["question"] += 1

    send_quiz_question(chat_id)

    return True


# =========================================================
# FINISH QUIZ
# =========================================================

def finish_quiz(chat_id):

    state = QUIZ_STATE.get(chat_id)

    if not state:
        return

    lesson_id = state["lesson_id"]

    score = state["score"]

    quiz = get_quiz(lesson_id)

    total = len(quiz)

    del QUIZ_STATE[chat_id]

    if total > 0:

        percentage = (
            score / total
        ) * 100

    else:

        percentage = 0

    if percentage == 100:

        result_message = "🏆 PERFECT SCORE!"

    elif percentage >= 70:

        result_message = "🔥 GREAT JOB!"

    elif percentage >= 50:

        result_message = "👍 GOOD EFFORT!"

    else:

        result_message = "💪 KEEP LEARNING!"

    user = get_user(chat_id)

    send_message(
        chat_id,
        f"""
🏁 QUIZ COMPLETE!
━━━━━━━━━━━━━━━━━━

📚 Lesson: {lesson_id}

🎯 Score:
{score} / {total}

📊 Result:
{percentage:.1f}%

{result_message}

━━━━━━━━━━━━━━━━━━

⭐ Total XP:
{user['xp']}

🏆 Level:
{user['level']}

{get_level_name(user['level'])}

━━━━━━━━━━━━━━━━━━

🚀 آماده‌ای برای مرحله بعد؟
""",
        main_menu()
    )


# =========================================================
# HANDLE MESSAGE
# =========================================================

def handle_message(
    chat_id,
    text,
    user_name=None,
    username=None
):

    text = text.strip()

    # Create/update user

    create_user(
        chat_id,
        name=user_name,
        username=username
    )

    # -----------------------------------------------------
    # ACTIVE QUIZ
    # -----------------------------------------------------

    if chat_id in QUIZ_STATE:

        if text == "❌ خروج از Quiz":

            del QUIZ_STATE[chat_id]

            send_message(
                chat_id,
                """
🛑 Quiz متوقف شد.

هر زمان آماده بودی دوباره شروع کن! 🧠
""",
                main_menu()
            )

            return

        if handle_quiz_answer(
            chat_id,
            text
        ):

            return

    # -----------------------------------------------------
    # START
    # -----------------------------------------------------

    if text == "/start":

        send_message(
            chat_id,
            WELCOME_MESSAGE,
            main_menu()
        )

        return

    # -----------------------------------------------------
    # LEARNING PATH
    # -----------------------------------------------------

    if text == "📚 مسیر یادگیری":

        lesson_overview = "\n".join(
            f"{lesson_id}. {lesson['title']}"
            for lesson_id, lesson in LESSONS.items()
        )

        send_message(
            chat_id,
            f"""
📚 LEARNING PATH
━━━━━━━━━━━━━━━━━━

{len(LESSONS)} درس برای شروع AI Safety:

{lesson_overview}

👇 یک درس را انتخاب کن:
""",
            lessons_menu()
        )

        return

    # -----------------------------------------------------
    # QUIZ CENTER
    # -----------------------------------------------------

    if text == "🧠 Quiz Center":

        send_message(
            chat_id,
            """
🧠 QUIZ CENTER
━━━━━━━━━━━━━━━━━━

وقتشه دانشت رو امتحان کنیم! 🔥

هر Quiz شامل چند سؤال است.

پاسخ درست:

⭐ +50 XP

با پیشرفت بیشتر:

🏆 Level Up
🎖️ Badges
🔓 Challenges

━━━━━━━━━━━━━━━━━━

👇 یک Quiz را انتخاب کن:
""",
            quiz_menu()
        )

        return

    # -----------------------------------------------------
    # SAFETY LAB
    # -----------------------------------------------------

    if text == "🧪 Safety Lab":

        send_message(
            chat_id,
            LAB_MESSAGE,
            main_menu()
        )

        return

    # -----------------------------------------------------
    # PROFILE
    # -----------------------------------------------------

    if text == "🏆 پروفایل من":

        send_message(
            chat_id,
            profile_message(chat_id),
            main_menu()
        )

        return

    # -----------------------------------------------------
    # ABOUT
    # -----------------------------------------------------

    if text == "ℹ️ درباره آکادمی":

        send_message(
            chat_id,
            ABOUT_MESSAGE,
            main_menu()
        )

        return

    # -----------------------------------------------------
    # BACK
    # -----------------------------------------------------

    if text == "🔙 بازگشت به منوی اصلی":

        send_message(
            chat_id,
            WELCOME_MESSAGE,
            main_menu()
        )

        return

    # -----------------------------------------------------
    # QUIZ SELECTION
    # -----------------------------------------------------

    if text.startswith("🧠 Quiz درس"):

        try:

            lesson_id = int(
                text.split()[-1]
            )

            start_quiz(
                chat_id,
                lesson_id
            )

        except ValueError:

            send_message(
                chat_id,
                "❌ خطا در شروع Quiz.",
                main_menu()
            )

        return

    # -----------------------------------------------------
    # LESSONS
    # -----------------------------------------------------

    for lesson_id, lesson in LESSONS.items():

        button = (
            f"📖 درس {lesson_id}: "
            f"{lesson['title']}"
        )

        if text == button:

            first_time = complete_lesson(
                chat_id,
                lesson_id
            )

            if first_time:

                result = add_xp(
                    chat_id,
                    100
                )

                extra = f"""

🎉 LESSON COMPLETE!

+100 XP ⭐

━━━━━━━━━━━━━━━━━━

⭐ XP: {result['xp']}
🏆 LEVEL: {result['level']}

{get_level_name(result['level'])}
"""

            else:

                extra = """

🔁 این درس را قبلاً کامل کرده‌ای.
"""

            send_message(
                chat_id,
                lesson["content"] + extra,
                lessons_menu()
            )

            return

    # -----------------------------------------------------
    # UNKNOWN COMMAND
    # -----------------------------------------------------

    send_message(
        chat_id,
        """
🤖 دستور را متوجه نشدم.

از منوی پایین استفاده کن 👇
""",
        main_menu()
    )


# =========================================================
# GET UPDATES
# =========================================================

def get_updates(offset=None):

    url = f"{BASE_URL}/getUpdates"

    params = {}

    if offset is not None:

        params["offset"] = offset

    response = requests.get(
        url,
        params=params,
        timeout=60
    )

    response.raise_for_status()

    return response.json()


# =========================================================
# MAIN LOOP
# =========================================================

def main():

    print("=================================")
    print("🛡️ AI SAFETY ACADEMY")
    print("🤖 Bot is running...")
    print("🧠 QUIZ SYSTEM: ACTIVE")
    print("📊 ANSWER TRACKING: ACTIVE")
    print("⭐ XP SYSTEM: ACTIVE")
    print("🏆 LEVEL SYSTEM: ACTIVE")
    print("=================================")

    offset = None

    while True:

        try:

            data = get_updates(
                offset
            )

            if not data.get("ok"):

                print(
                    "API ERROR:",
                    data
                )

                continue

            updates = data.get(
                "result",
                []
            )

            for update in updates:

                offset = (
                    update["update_id"] + 1
                )

                message = update.get(
                    "message"
                )

                if not message:
                    continue

                chat = message.get(
                    "chat"
                )

                if not chat:
                    continue

                chat_id = chat.get(
                    "id"
                )

                text = message.get(
                    "text",
                    ""
                )

                if not text:
                    continue

                # User information

                user_name = (
                    message.get("from", {})
                    .get("first_name")
                )

                username = (
                    message.get("from", {})
                    .get("username")
                )

                print(
                    f"Message from "
                    f"{chat_id}: {text}"
                )

                handle_message(
                    chat_id,
                    text,
                    user_name,
                    username
                )

        except requests.exceptions.RequestException as e:

            print(
                "NETWORK ERROR:",
                e
            )

        except Exception as e:

            print(
                "ERROR:",
                e
            )


# =========================================================
# RUN
# =========================================================

if __name__ == "__main__":

    main()