LESSONS = {
    1: {
        "module": "Foundations of LLM Safety Engineering",
        "title": "LLM Safety چیست؟",
        "content": """
🛡️ LESSON 1
━━━━━━━━━━━━━━━━━━

🤖 LLM Safety چیست؟

LLM Safety به مجموعه‌ای از اصول و روش‌های
مهندسی برای کاهش رفتارهای ناخواسته،
خطرناک یا غیرقابل‌اعتماد در سیستم‌های
مبتنی بر مدل‌های زبانی گفته می‌شود.

Safety فقط جلوگیری از تولید محتوای
خطرناک نیست.

یک سیستم LLM باید بتواند:

✅ رفتار قابل پیش‌بینی داشته باشد
✅ در برابر ورودی‌های مخرب مقاوم باشد
✅ اطلاعات حساس را محافظت کند
✅ محدودیت‌های تعریف‌شده را رعایت کند
✅ در شرایط غیرعادی قابل کنترل باشد

━━━━━━━━━━━━━━━━━━

🔑 SYSTEM SAFETY

یک مدل ممکن است به‌تنهایی نسبتاً امن باشد،
اما وقتی به Web، Files، Database، Tools
یا Agents متصل می‌شود، Attack Surface
افزایش پیدا می‌کند.

━━━━━━━━━━━━━━━━━━

🎯 نکته کلیدی:

LLM Safety یک مسئله System Engineering
است، نه فقط یک ویژگی مدل.
"""
    },

    2: {
        "module": "Foundations of LLM Safety Engineering",
        "title": "Safety vs Security",
        "content": """
🛡️ LESSON 2
━━━━━━━━━━━━━━━━━━

⚔️ Safety vs Security

دو مفهوم مهم در AI Safety:

🟢 Safety
🔴 Security

━━━━━━━━━━━━━━━━━━

🟢 SAFETY

تمرکز روی جلوگیری از رفتارهای
ناخواسته یا آسیب‌زا.

مثلاً:

• رفتار غیرقابل پیش‌بینی
• تصمیم اشتباه
• Failure
• خروج از محدودیت‌های تعریف‌شده

━━━━━━━━━━━━━━━━━━

🔴 SECURITY

تمرکز روی مقاومت سیستم در برابر
تهدیدها و حملات.

مثلاً:

• Prompt Injection
• Data Leakage
• Unauthorized Access
• Tool Abuse

━━━━━━━━━━━━━━━━━━

🧠 مفاهیم مرتبط:

Reliability
= عملکرد پایدار در شرایط مورد انتظار

Robustness
= حفظ رفتار مناسب در شرایط دشوار

━━━━━━━━━━━━━━━━━━

🎯 نتیجه:

Safety + Security +
Reliability + Robustness

باید با هم بررسی شوند.
"""
    },

    3: {
        "module": "Foundations of LLM Safety Engineering",
        "title": "Reliability & Robustness",
        "content": """
🛡️ LESSON 3
━━━━━━━━━━━━━━━━━━

🔧 Reliability & Robustness

📌 Reliability

توانایی سیستم برای انجام پایدار
وظیفه مورد انتظار.

📌 Robustness

توانایی سیستم برای حفظ رفتار مناسب
در برابر تغییرات، نویز و ورودی‌های دشوار.

━━━━━━━━━━━━━━━━━━

⚠️ Distribution Shift

وقتی داده‌های دنیای واقعی با داده‌هایی
که مدل در زمان توسعه دیده متفاوت باشند،
ممکن است عملکرد مدل کاهش پیدا کند.

━━━━━━━━━━━━━━━━━━

🎯 نکته:

Robustness یعنی سیستم فقط در شرایط
ایده‌آل کار نکند؛ بلکه در شرایط دشوار
نیز قابل اعتماد باقی بماند.
"""
    },

    4: {
        "module": "Foundations of LLM Safety Engineering",
        "title": "Threat Modeling برای LLM",
        "content": """
🛡️ LESSON 4
━━━━━━━━━━━━━━━━━━

🎯 Threat Modeling

قبل از طراحی دفاع باید بدانیم:

❓ چه چیزی را محافظت می‌کنیم؟
❓ مهاجم چه توانایی‌هایی دارد؟
❓ Attack Surface کجاست؟
❓ چه پیامدهایی ممکن است رخ دهد؟

━━━━━━━━━━━━━━━━━━

🔹 ASSET

چیزی که باید محافظت شود.

🔐 API Key
📁 Private Data
🧠 System Instructions
🗄️ Database
🔧 Tool Permissions

━━━━━━━━━━━━━━━━━━

🔹 THREAT

تهدیدی که می‌تواند به Asset آسیب بزند.

━━━━━━━━━━━━━━━━━━

🔹 ATTACK SURFACE

نقاطی که مهاجم می‌تواند از طریق آنها
با سیستم تعامل کند.

━━━━━━━━━━━━━━━━━━

🔹 ATTACKER MODEL

مثلاً:

Black-box
White-box
Adaptive

━━━━━━━━━━━━━━━━━━

🎯 هدف:

قبل از دفاع کردن، تهدید را درست مدل کنیم.
"""
    },

    5: {
        "module": "Foundations of LLM Safety Engineering",
        "title": "Trust Boundary & System Safety",
        "content": """
🛡️ LESSON 5
━━━━━━━━━━━━━━━━━━

🔐 TRUST BOUNDARY

در یک سیستم LLM همه داده‌ها
به یک اندازه قابل اعتماد نیستند.

مثلاً:

👤 User
↓
🤖 LLM
↓
📚 RAG
↓
🔧 Tool
↓
🌐 External System

━━━━━━━━━━━━━━━━━━

🟢 TRUSTED

داده یا component مورد اعتماد.

🔴 UNTRUSTED

داده‌ای که ممکن است توسط مهاجم
کنترل یا تغییر داده شود.

مثلاً:

🌐 Web Page
📄 Document
📧 Email
💬 User Input
📚 Retrieved Content

━━━━━━━━━━━━━━━━━━

⚠️ اصل مهم:

DATA ≠ INSTRUCTION

هر چیزی که وارد Context می‌شود
نباید به‌عنوان دستور معتبر تلقی شود.
"""
    },

    6: {
        "module": "Prompt & Context Safety",
        "title": "Prompt Security",
        "content": """
🔐 LESSON 6
━━━━━━━━━━━━━━━━━━

PROMPT SECURITY

Prompt فقط یک متن ساده نیست.

در یک سیستم LLM ممکن است چند نوع
Instruction وجود داشته باشد:

🟣 System
🔵 Developer
🟢 User
🟡 External Context

هر کدام می‌توانند نقش متفاوتی داشته باشند.

━━━━━━━━━━━━━━━━━━

🧠 INSTRUCTION HIERARCHY

یک سیستم امن باید بتواند تفاوت بین
منابع مختلف دستور را درک کند.

مثلاً:

SYSTEM
  ↓
DEVELOPER
  ↓
USER
  ↓
EXTERNAL DATA

━━━━━━━━━━━━━━━━━━

⚠️ مشکل زمانی ایجاد می‌شود که یک ورودی
غیرقابل اعتماد تلاش کند خود را به‌عنوان
Instruction معتبر معرفی کند.

━━━━━━━━━━━━━━━━━━

🎯 هدف Prompt Security:

جلوگیری از تغییر غیرمجاز رفتار مدل
توسط ورودی‌ها.
"""
    },

    7: {
        "module": "Prompt & Context Safety",
        "title": "Prompt Injection",
        "content": """
💉 LESSON 7
━━━━━━━━━━━━━━━━━━

PROMPT INJECTION

Prompt Injection زمانی رخ می‌دهد که
ورودی مهاجم تلاش کند رفتار یا اهداف
مدل را تحت تأثیر قرار دهد.

━━━━━━━━━━━━━━━━━━

🎯 اهداف احتمالی:

• تغییر رفتار مدل
• تغییر هدف
• افشای اطلاعات
• دور زدن محدودیت‌ها
• تغییر نحوه استفاده از Tool

━━━━━━━━━━━━━━━━━━

🧠 دو دسته مهم:

Direct Injection
Indirect Injection

━━━━━━━━━━━━━━━━━━

Direct Injection:

مهاجم مستقیماً ورودی را کنترل می‌کند.

Indirect Injection:

دستور مخرب از یک منبع خارجی
وارد Context می‌شود.

━━━━━━━━━━━━━━━━━━

🔑 اصل:

ورودی کاربر همیشه قابل اعتماد نیست.
"""
    },

    8: {
        "module": "Prompt & Context Safety",
        "title": "Indirect Prompt Injection",
        "content": """
🕵️ LESSON 8
━━━━━━━━━━━━━━━━━━

INDIRECT PROMPT INJECTION

در این نوع حمله، مهاجم لزوماً
مستقیماً با مدل صحبت نمی‌کند.

دستور مخرب ممکن است داخل:

🌐 Web Page
📄 Document
📧 Email
📚 Retrieved Data
🗂️ Knowledge Base

قرار داشته باشد.

━━━━━━━━━━━━━━━━━━

مثلاً:

User
 ↓
Agent
 ↓
Web Page
 ↓
Malicious Content
 ↓
LLM

Agent محتوای خارجی را می‌خواند و ممکن
است مدل آن را به‌عنوان Instruction تفسیر کند.

━━━━━━━━━━━━━━━━━━

🛡️ اصول دفاعی:

• Trust Boundaries
• Context Isolation
• Input Validation
• Least Privilege
• Output Validation
• Human Approval

━━━━━━━━━━━━━━━━━━

🎯 DATA باید DATA باقی بماند.
"""
    },

    9: {
        "module": "Prompt & Context Safety",
        "title": "Instruction Conflict",
        "content": """
⚔️ LESSON 9
━━━━━━━━━━━━━━━━━━

INSTRUCTION CONFLICT

یک LLM ممکن است همزمان چند Instruction
دریافت کند.

مثلاً:

System
↓
Developer
↓
User
↓
External Context

━━━━━━━━━━━━━━━━━━

اگر این دستورها با هم تعارض داشته
باشند چه می‌شود؟

مثلاً:

SYSTEM:
اطلاعات خصوصی را افشا نکن.

USER:
اطلاعات خصوصی را نمایش بده.

دو هدف متناقض هستند.

━━━━━━━━━━━━━━━━━━

🧠 Instruction Priority

سیستم باید مشخص کند:

کدام Instruction معتبرتر است؟

و:

کدام Instruction باید نادیده گرفته شود؟

━━━━━━━━━━━━━━━━━━

⚠️ مشکل اصلی:

LLM یک Interpreter احتمالاتی است،
نه یک Policy Engine کامل.

بنابراین طراحی سیستم باید
Conflict Resolution را جدی بگیرد.

━━━━━━━━━━━━━━━━━━

🎯 اصل:

Instructionها باید:

✔️ واضح
✔️ قابل تفکیک
✔️ قابل اولویت‌بندی
✔️ قابل اعتبارسنجی

باشند.
"""
    },

    10: {
        "module": "Prompt & Context Safety",
        "title": "Untrusted Context & Context Manipulation",
        "content": """
🧩 LESSON 10
━━━━━━━━━━━━━━━━━━

UNTRUSTED CONTEXT

هر چیزی که وارد Context مدل می‌شود
نباید Trusted فرض شود.

━━━━━━━━━━━━━━━━━━

🔴 نمونه‌های Untrusted Context:

🌐 Web
📄 Document
📧 Email
💬 User Input
📚 Retrieved Content

━━━━━━━━━━━━━━━━━━

⚠️ CONTEXT MANIPULATION

مهاجم ممکن است تلاش کند محتوای Context
را طوری تغییر دهد که مدل تصمیم متفاوتی بگیرد.

━━━━━━━━━━━━━━━━━━

مثلاً:

Trusted Instruction
        +
Untrusted Content
        ↓
       LLM
        ↓
Unexpected Behavior

━━━━━━━━━━━━━━━━━━

🛡️ دفاع‌ها:

• Context Separation
• Provenance
• Validation
• Access Control
• Content Filtering
• Least Privilege
• Output Validation

━━━━━━━━━━━━━━━━━━

🔑 اصل طلایی:

UNTRUSTED DATA

نباید بتواند به‌سادگی تبدیل شود به:

TRUSTED INSTRUCTION
"""
    },

    11: {
        "module": "RAG & Knowledge Safety",
        "title": "RAG چیست؟",
        "content": """
🟩 LESSON 11
━━━━━━━━━━━━━━━━━━

📚 RAG چیست؟

RAG مخفف:

Retrieval-Augmented Generation

است.

در یک سیستم RAG، مدل قبل از تولید پاسخ،
اطلاعات مرتبط را از یک منبع خارجی بازیابی
می‌کند.

━━━━━━━━━━━━━━━━━━

🔄 RAG PIPELINE

👤 User
   ↓
🔎 Retriever
   ↓
📚 Knowledge Base
   ↓
📄 Retrieved Context
   ↓
🤖 LLM
   ↓
💬 Answer

━━━━━━━━━━━━━━━━━━

اجزای مهم:

🔎 Retriever
پیدا کردن اطلاعات مرتبط.

🧠 Embedding
تبدیل متن به نمایش عددی.

🗄️ Vector Database
ذخیره و جستجوی embeddingها.

🤖 Generator
مدل زبانی تولیدکننده پاسخ.

━━━━━━━━━━━━━━━━━━

⚠️ نکته امنیتی:

اضافه کردن Knowledge Base
به معنی Trusted شدن خودکار اطلاعات نیست.

━━━━━━━━━━━━━━━━━━

🎯 اصل:

RAG مشکل Knowledge را کاهش می‌دهد،
اما یک Security Boundary جدید نیز ایجاد
می‌کند.
"""
    },

    12: {
        "module": "RAG & Knowledge Safety",
        "title": "Retrieval Risk",
        "content": """
🟩 LESSON 12
━━━━━━━━━━━━━━━━━━

🔎 RETRIEVAL RISK

در RAG، مدل به اطلاعاتی وابسته است
که Retriever انتخاب می‌کند.

سؤال مهم:

❓ آیا اطلاعات بازیابی‌شده واقعاً
مناسب و قابل اعتماد است؟

━━━━━━━━━━━━━━━━━━

مشکلات احتمالی:

❌ Irrelevant Retrieval
اطلاعات نامرتبط

❌ Incomplete Retrieval
اطلاعات ناقص

❌ Malicious Retrieval
محتوای مخرب

❌ Sensitive Retrieval
اطلاعاتی که کاربر نباید ببیند

━━━━━━━━━━━━━━━━━━

🔐 Retrieval باید علاوه بر شباهت معنایی،
موارد زیر را نیز در نظر بگیرد:

• Relevance
• Trust
• Permissions
• Provenance

━━━━━━━━━━━━━━━━━━

🎯 هدف:

اطلاعات درست،
از منبع درست،
برای کاربر درست.
"""
    },

    13: {
        "module": "RAG & Knowledge Safety",
        "title": "Knowledge Poisoning",
        "content": """
🟩 LESSON 13
━━━━━━━━━━━━━━━━━━

☠️ KNOWLEDGE POISONING

Knowledge Poisoning زمانی رخ می‌دهد
که اطلاعات مخرب یا نادرست وارد منبع
دانش سیستم شود.

━━━━━━━━━━━━━━━━━━

مثلاً:

Attacker
   ↓
Malicious Document
   ↓
Knowledge Base
   ↓
Retriever
   ↓
LLM
   ↓
Incorrect / Unsafe Response

━━━━━━━━━━━━━━━━━━

ممکن است مهاجم تلاش کند:

• اطلاعات نادرست وارد کند
• اسناد مخرب اضافه کند
• Retrieval را تحت تأثیر قرار دهد
• محتوای قابل بازیابی ایجاد کند

━━━━━━━━━━━━━━━━━━

🧠 تفاوت:

Model Poisoning
≠
Knowledge Base Poisoning

در Model Poisoning هدف خود مدل
یا پارامترهای آن است.

در Knowledge Poisoning هدف می‌تواند
منبع اطلاعاتی مورد استفاده سیستم باشد.

━━━━━━━━━━━━━━━━━━

🛡️ دفاع‌ها:

✔️ Source Validation
✔️ Provenance
✔️ Document Review
✔️ Access Control
✔️ Integrity Checking
✔️ Monitoring
"""
    },

    14: {
        "module": "RAG & Knowledge Safety",
        "title": "Malicious Documents",
        "content": """
🟩 LESSON 14
━━━━━━━━━━━━━━━━━━

📄 MALICIOUS DOCUMENTS

در سیستم‌های RAG، Document می‌تواند
بخشی از ورودی مدل باشد.

بنابراین یک Document مخرب می‌تواند
به Security Risk تبدیل شود.

━━━━━━━━━━━━━━━━━━

منابع احتمالی:

📄 PDF
📝 Word
🌐 Web Page
📧 Email
📋 Wiki
🗃️ Knowledge Base

━━━━━━━━━━━━━━━━━━

یک Document ممکن است شامل:

⚠️ اطلاعات نادرست
⚠️ دستورهای مخفی
⚠️ محتوای گمراه‌کننده
⚠️ داده‌های حساس

باشد.

━━━━━━━━━━━━━━━━━━

🛡️ دفاع:

• Document Sanitization
• Content Validation
• Provenance
• Access Control
• Content Classification
• Output Validation

━━━━━━━━━━━━━━━━━━

🎯 اصل:

Retrieved Content نباید بدون بررسی
Trusted Instruction تلقی شود.
"""
    },

    15: {
        "module": "RAG & Knowledge Safety",
        "title": "Provenance & Access Control",
        "content": """
🟩 LESSON 15
━━━━━━━━━━━━━━━━━━

🔐 PROVENANCE & ACCESS CONTROL

دو مفهوم بسیار مهم در Knowledge Safety.

━━━━━━━━━━━━━━━━━━

📌 PROVENANCE

یعنی بدانیم:

این اطلاعات از کجا آمده؟

مثلاً:

Document
   ↓
Source
   ↓
Author
   ↓
Timestamp
   ↓
Verification

━━━━━━━━━━━━━━━━━━

🔐 ACCESS CONTROL

حتی اگر یک Document معتبر باشد،
ممکن است همه کاربران اجازه دسترسی
به آن را نداشته باشند.

مثلاً:

👤 User A
   ↓
📄 Public Document
   ✅ Allowed

👤 User B
   ↓
🔐 Private Document
   ❌ Denied

━━━━━━━━━━━━━━━━━━

⚠️ یک خطای خطرناک:

Retriever فقط دنبال «مرتبط‌ترین»
Document بگردد.

در حالی که باید بپرسد:

❓ آیا این User اجازه دیدن
این Document را دارد؟

━━━━━━━━━━━━━━━━━━

🛡️ اصول مهم:

✔️ Authentication
✔️ Authorization
✔️ Document-level Permissions
✔️ User Isolation
✔️ Provenance Tracking

━━━━━━━━━━━━━━━━━━

🎯 اصل طلایی:

RELEVANT ≠ AUTHORIZED

یک Document می‌تواند مرتبط باشد،
اما کاربر مجاز به دیدن آن نباشد.
"""
    }
}