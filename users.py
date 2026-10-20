import json
import os


# =========================
# Storage
# =========================

DATA_DIR = "data"

USERS_FILE = os.path.join(
    DATA_DIR,
    "users.json"
)

RESULTS_FILE = os.path.join(
    DATA_DIR,
    "quiz_results.json"
)


# =========================
# Ensure Storage
# =========================

def ensure_storage():

    os.makedirs(
        DATA_DIR,
        exist_ok=True
    )

    if not os.path.exists(USERS_FILE):

        with open(
            USERS_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                {},
                file,
                ensure_ascii=False,
                indent=4
            )

    if not os.path.exists(RESULTS_FILE):

        with open(
            RESULTS_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                [],
                file,
                ensure_ascii=False,
                indent=4
            )


# =========================
# Load Users
# =========================

def load_users():

    ensure_storage()

    try:

        with open(
            USERS_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except (
        json.JSONDecodeError,
        FileNotFoundError
    ):

        return {}


# =========================
# Save Users
# =========================

def save_users(users):

    ensure_storage()

    with open(
        USERS_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            users,
            file,
            ensure_ascii=False,
            indent=4
        )


# =========================
# Load Quiz Results
# =========================

def load_results():

    ensure_storage()

    try:

        with open(
            RESULTS_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except (
        json.JSONDecodeError,
        FileNotFoundError
    ):

        return []


# =========================
# Save Quiz Results
# =========================

def save_results(results):

    ensure_storage()

    with open(
        RESULTS_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            results,
            file,
            ensure_ascii=False,
            indent=4
        )


# =========================
# Create / Migrate User
# =========================

def create_user(
    chat_id,
    name=None,
    username=None
):

    users = load_users()

    user_id = str(chat_id)

    # -------------------------
    # New User
    # -------------------------

    if user_id not in users:

        users[user_id] = {

            "chat_id": chat_id,

            "name": (
                name
                or "Unknown"
            ),

            "username": (
                username
                or ""
            ),

            "xp": 0,

            "level": 1,

            "lessons_completed": [],

            "quizzes_completed": 0,

            "correct_answers": 0,

            "total_answers": 0,

            "badges": []
        }

        save_users(users)

    # -------------------------
    # Existing User
    # -------------------------

    else:

        user = users[user_id]

        changed = False

        if name:

            user["name"] = name

            changed = True

        if username:

            user["username"] = username

            changed = True

        # =========================
        # Migration
        # =========================

        if "xp" not in user:

            user["xp"] = 0

            changed = True

        if "level" not in user:

            user["level"] = 1

            changed = True

        if "lessons_completed" not in user:

            user["lessons_completed"] = []

            changed = True

        if "quizzes_completed" not in user:

            user["quizzes_completed"] = 0

            changed = True

        if "correct_answers" not in user:

            user["correct_answers"] = 0

            changed = True

        if "total_answers" not in user:

            user["total_answers"] = 0

            changed = True

        if "badges" not in user:

            user["badges"] = []

            changed = True

        if changed:

            save_users(users)

    return users[user_id]


# =========================
# Get User
# =========================

def get_user(chat_id):

    users = load_users()

    user_id = str(chat_id)

    if user_id not in users:

        create_user(chat_id)

        users = load_users()

    # Safety migration

    user = users[user_id]

    changed = False

    defaults = {

        "name": "Unknown",

        "username": "",

        "xp": 0,

        "level": 1,

        "lessons_completed": [],

        "quizzes_completed": 0,

        "correct_answers": 0,

        "total_answers": 0,

        "badges": []
    }

    for key, value in defaults.items():

        if key not in user:

            user[key] = value

            changed = True

    if changed:

        save_users(users)

    return user


# =========================
# Add XP
# =========================

def add_xp(
    chat_id,
    amount
):

    users = load_users()

    user_id = str(chat_id)

    if user_id not in users:

        create_user(chat_id)

        users = load_users()

    user = users[user_id]

    user.setdefault(
        "xp",
        0
    )

    user["xp"] += amount

    update_level(user)

    save_users(users)

    return user


# =========================
# Update Level
# =========================

def update_level(user):

    xp = user.get(
        "xp",
        0
    )

    if xp >= 1000:

        user["level"] = 6

    elif xp >= 750:

        user["level"] = 5

    elif xp >= 500:

        user["level"] = 4

    elif xp >= 300:

        user["level"] = 3

    elif xp >= 150:

        user["level"] = 2

    else:

        user["level"] = 1


# =========================
# Complete Lesson
# =========================

def complete_lesson(
    chat_id,
    lesson_id
):

    users = load_users()

    user_id = str(chat_id)

    if user_id not in users:

        create_user(chat_id)

        users = load_users()

    user = users[user_id]

    user.setdefault(
        "lessons_completed",
        []
    )

    lessons = user[
        "lessons_completed"
    ]

    if lesson_id not in lessons:

        lessons.append(
            lesson_id
        )

        save_users(users)

        return True

    return False


# =========================
# Add Quiz Result
# =========================

def add_quiz_result(
    chat_id,
    correct
):

    users = load_users()

    user_id = str(chat_id)

    if user_id not in users:

        create_user(chat_id)

        users = load_users()

    user = users[user_id]

    # Safety defaults
    user.setdefault(
        "quizzes_completed",
        0
    )

    user.setdefault(
        "total_answers",
        0
    )

    user.setdefault(
        "correct_answers",
        0
    )

    user[
        "quizzes_completed"
    ] += 1

    user[
        "total_answers"
    ] += 1

    if correct:

        user[
            "correct_answers"
        ] += 1

    save_users(users)


# =========================
# Record Individual Answer
# =========================

def record_answer(
    chat_id,
    lesson_id,
    question_number,
    question,
    selected_answer,
    correct_answer,
    is_correct
):

    results = load_results()

    user = get_user(chat_id)

    record = {

        "chat_id": chat_id,

        "name": user.get(
            "name",
            "Unknown"
        ),

        "username": user.get(
            "username",
            ""
        ),

        "lesson_id": lesson_id,

        "question_number":
            question_number,

        "question":
            question,

        "selected_answer":
            selected_answer,

        "correct_answer":
            correct_answer,

        "is_correct":
            is_correct
    }

    results.append(record)

    save_results(results)


# =========================
# Get Quiz Results
# =========================

def get_quiz_results():

    return load_results()


# =========================
# Add Badge
# =========================

def add_badge(
    chat_id,
    badge
):

    users = load_users()

    user_id = str(chat_id)

    if user_id not in users:

        create_user(chat_id)

        users = load_users()

    user = users[user_id]

    user.setdefault(
        "badges",
        []
    )

    if badge not in user["badges"]:

        user["badges"].append(
            badge
        )

        save_users(users)

        return True

    return False


# =========================
# Level Name
# =========================

def get_level_name(level):

    levels = {

        1:
            "👤 AI Explorer",

        2:
            "🔍 Safety Scout",

        3:
            "🛡️ Safety Defender",

        4:
            "🧠 AI Security Analyst",

        5:
            "⚔️ AI Red Teamer",

        6:
            "🔬 AI Safety Researcher"
    }

    return levels.get(
        level,
        "👤 AI Explorer"
    )