QUIZZES = {

    # =====================================================
    # MODULE 1 — FOUNDATIONS
    # =====================================================

    1: [
        {
            "question": "LLM Safety بیشتر به چه چیزی مربوط است؟",
            "options": [
                "افزایش سرعت اینترنت",
                "کاهش رفتارهای ناخواسته و آسیب‌زا",
                "افزایش حجم مدل",
                "افزایش تعداد پارامترها"
            ],
            "answer": 1
        },
        {
            "question": "چرا Safety باید در سطح سیستم بررسی شود؟",
            "options": [
                "چون مدل‌ها اینترنت ندارند",
                "چون اتصال به Tools و Data سطح حمله را افزایش می‌دهد",
                "چون LLM فقط متن تولید می‌کند",
                "چون Training اهمیتی ندارد"
            ],
            "answer": 1
        },
        {
            "question": "کدام مورد می‌تواند Attack Surface را افزایش دهد؟",
            "options": [
                "Tool",
                "RAG",
                "External API",
                "همه موارد"
            ],
            "answer": 3
        }
    ],

    2: [
        {
            "question": "Security بیشتر روی چه چیزی تمرکز دارد؟",
            "options": [
                "تهدیدها و حملات",
                "طراحی رابط کاربری",
                "افزایش پارامترها",
                "سرعت پردازش"
            ],
            "answer": 0
        },
        {
            "question": "Reliability یعنی چه؟",
            "options": [
                "سیستم همیشه سریع باشد",
                "سیستم در شرایط مورد انتظار پایدار عمل کند",
                "مدل بزرگ‌تر باشد",
                "مدل همیشه یک پاسخ داشته باشد"
            ],
            "answer": 1
        },
        {
            "question": "Robustness چیست؟",
            "options": [
                "مقاومت در شرایط دشوار",
                "افزایش حجم مدل",
                "افزایش Token",
                "افزایش سرعت GPU"
            ],
            "answer": 0
        }
    ],

    3: [
        {
            "question": "Reliability بیشتر به چه چیزی اشاره دارد؟",
            "options": [
                "پایداری عملکرد",
                "توانایی حمله",
                "اندازه Dataset",
                "تعداد کاربران"
            ],
            "answer": 0
        },
        {
            "question": "Robustness چیست؟",
            "options": [
                "حفظ رفتار مناسب در شرایط دشوار",
                "سرعت آموزش",
                "اندازه مدل",
                "تعداد پارامترها"
            ],
            "answer": 0
        },
        {
            "question": "Distribution Shift چیست؟",
            "options": [
                "تغییر زبان",
                "تفاوت توزیع داده واقعی با داده توسعه",
                "تغییر GPU",
                "تغییر API"
            ],
            "answer": 1
        }
    ],

    4: [
        {
            "question": "Threat Modeling برای چه کاری استفاده می‌شود؟",
            "options": [
                "شناخت دارایی‌ها و تهدیدها",
                "افزایش سرعت مدل",
                "افزایش تعداد پارامترها",
                "تغییر GPU"
            ],
            "answer": 0
        },
        {
            "question": "کدام مورد یک Asset محسوب می‌شود؟",
            "options": [
                "API Key",
                "Private Data",
                "Tool Permission",
                "همه موارد"
            ],
            "answer": 3
        },
        {
            "question": "Attack Surface چیست؟",
            "options": [
                "نقاط قابل تعامل یا سوءاستفاده در سیستم",
                "تعداد کاربران",
                "اندازه مدل",
                "سرعت شبکه"
            ],
            "answer": 0
        }
    ],

    5: [
        {
            "question": "Trust Boundary چیست؟",
            "options": [
                "مرز تغییر سطح اعتماد",
                "مرز GPU",
                "مرز Dataset",
                "مرز Token"
            ],
            "answer": 0
        },
        {
            "question": "کدام مورد معمولاً Untrusted Context است؟",
            "options": [
                "System Policy",
                "Trusted Configuration",
                "External Web Page",
                "Security Policy"
            ],
            "answer": 2
        },
        {
            "question": "کدام اصل در Context Safety مهم است؟",
            "options": [
                "DATA = INSTRUCTION",
                "DATA ≠ INSTRUCTION",
                "USER = ADMIN",
                "TOOL = TRUSTED"
            ],
            "answer": 1
        }
    ],


    # =====================================================
    # MODULE 2 — PROMPT & CONTEXT SAFETY
    # =====================================================

    6: [
        {
            "question": "کدام مورد معمولاً بالاترین سطح Instruction را دارد؟",
            "options": [
                "User",
                "External Data",
                "System",
                "Random Text"
            ],
            "answer": 2
        },
        {
            "question": "هدف اصلی Prompt Security چیست؟",
            "options": [
                "افزایش سرعت مدل",
                "جلوگیری از تغییر غیرمجاز رفتار مدل",
                "افزایش Dataset",
                "کاهش Token"
            ],
            "answer": 1
        },
        {
            "question": "کدام مورد می‌تواند Untrusted باشد؟",
            "options": [
                "External Context",
                "System Policy",
                "Verified Configuration",
                "Security Policy"
            ],
            "answer": 0
        }
    ],

    7: [
        {
            "question": "Prompt Injection چیست؟",
            "options": [
                "افزایش سرعت مدل",
                "تلاش ورودی برای تغییر رفتار یا اهداف مدل",
                "تغییر GPU",
                "افزایش Context Window"
            ],
            "answer": 1
        },
        {
            "question": "Direct Prompt Injection معمولاً از کجا می‌آید؟",
            "options": [
                "ورودی مستقیم مهاجم",
                "GPU",
                "System Clock",
                "Database Engine"
            ],
            "answer": 0
        },
        {
            "question": "دو دسته مهم Prompt Injection کدام‌اند؟",
            "options": [
                "Direct و Indirect",
                "Local و GPU",
                "Fast و Slow",
                "Static و Binary"
            ],
            "answer": 0
        }
    ],

    8: [
        {
            "question": "Indirect Prompt Injection معمولاً از کجا وارد می‌شود؟",
            "options": [
                "External Content",
                "CPU",
                "RAM",
                "Operating System"
            ],
            "answer": 0
        },
        {
            "question": "کدام مورد می‌تواند منبع Indirect Injection باشد؟",
            "options": [
                "Web Page",
                "Document",
                "Email",
                "همه موارد"
            ],
            "answer": 3
        },
        {
            "question": "کدام مورد یک اصل دفاعی مهم است؟",
            "options": [
                "Least Privilege",
                "افزایش پارامتر",
                "کاهش RAM",
                "افزایش Temperature"
            ],
            "answer": 0
        }
    ],

    9: [
        {
            "question": "Instruction Conflict یعنی چه؟",
            "options": [
                "تعارض بین دستورها",
                "افزایش Token",
                "تغییر GPU",
                "افزایش Dataset"
            ],
            "answer": 0
        },
        {
            "question": "در Instruction Conflict چه چیزی باید مشخص باشد؟",
            "options": [
                "Instruction Priority",
                "GPU Temperature",
                "Network Speed",
                "Dataset Size"
            ],
            "answer": 0
        },
        {
            "question": "چرا Conflict Resolution مهم است؟",
            "options": [
                "برای جلوگیری از رفتار غیرمنتظره",
                "برای افزایش حجم مدل",
                "برای کاهش RAM",
                "برای افزایش سرعت اینترنت"
            ],
            "answer": 0
        }
    ],

    10: [
        {
            "question": "Untrusted Context چیست؟",
            "options": [
                "Context کاملاً معتبر",
                "Contextی که نباید بدون بررسی Trusted فرض شود",
                "System Policy",
                "Verified Configuration"
            ],
            "answer": 1
        },
        {
            "question": "کدام مورد می‌تواند Untrusted Context باشد؟",
            "options": [
                "Web Content",
                "System Policy",
                "Security Policy",
                "Verified Configuration"
            ],
            "answer": 0
        },
        {
            "question": "اصل مهم Context Safety چیست؟",
            "options": [
                "Untrusted Data نباید به‌سادگی Trusted Instruction شود",
                "همه Dataها Trusted هستند",
                "User همیشه Admin است",
                "Tool همیشه Trusted است"
            ],
            "answer": 0
        }
    ],


    # =====================================================
    # MODULE 3 — RAG & KNOWLEDGE SAFETY
    # =====================================================

    11: [
        {
            "question": "RAG مخفف چیست؟",
            "options": [
                "Random AI Generation",
                "Retrieval-Augmented Generation",
                "Real-time AI Gateway",
                "Recursive Agent Generation"
            ],
            "answer": 1
        },
        {
            "question": "وظیفه Retriever چیست؟",
            "options": [
                "تولید Token",
                "پیدا کردن اطلاعات مرتبط",
                "آموزش مدل",
                "مدیریت GPU"
            ],
            "answer": 1
        },
        {
            "question": "آیا Knowledge Base الزاماً Trusted است؟",
            "options": [
                "بله",
                "خیر",
                "فقط در مدل‌های کوچک",
                "فقط در GPT"
            ],
            "answer": 1
        }
    ],

    12: [
        {
            "question": "Retrieval Risk به چه چیزی مربوط است؟",
            "options": [
                "خطرات ناشی از اطلاعات بازیابی‌شده",
                "سرعت GPU",
                "اندازه مدل",
                "تعداد Token"
            ],
            "answer": 0
        },
        {
            "question": "کدام مورد یک Retrieval Failure است؟",
            "options": [
                "Relevant Retrieval",
                "Irrelevant Retrieval",
                "Correct Retrieval",
                "Authorized Retrieval"
            ],
            "answer": 1
        },
        {
            "question": "آیا Relevance به‌تنهایی برای Retrieval کافی است؟",
            "options": [
                "بله",
                "خیر",
                "همیشه",
                "فقط برای PDF"
            ],
            "answer": 1
        }
    ],

    13: [
        {
            "question": "Knowledge Poisoning چیست؟",
            "options": [
                "آلودگی منبع دانش با اطلاعات مخرب یا نادرست",
                "افزایش سرعت مدل",
                "تغییر GPU",
                "افزایش Context Window"
            ],
            "answer": 0
        },
        {
            "question": "هدف Knowledge Poisoning چیست؟",
            "options": [
                "تأثیرگذاری بر اطلاعاتی که سیستم بازیابی می‌کند",
                "افزایش RAM",
                "کاهش Latency",
                "افزایش تعداد کاربران"
            ],
            "answer": 0
        },
        {
            "question": "کدام مورد یک دفاع مناسب است؟",
            "options": [
                "Source Validation",
                "افزایش Temperature",
                "افزایش Token",
                "حذف Retriever"
            ],
            "answer": 0
        }
    ],

    14: [
        {
            "question": "کدام مورد می‌تواند یک Malicious Document باشد؟",
            "options": [
                "PDF",
                "Web Page",
                "Email",
                "همه موارد"
            ],
            "answer": 3
        },
        {
            "question": "چرا Document می‌تواند Security Risk باشد؟",
            "options": [
                "ممکن است محتوای مخرب وارد Context کند",
                "چون همیشه بزرگ است",
                "چون GPU را خاموش می‌کند",
                "چون Token ندارد"
            ],
            "answer": 0
        },
        {
            "question": "کدام مورد یک دفاع مناسب است؟",
            "options": [
                "Document Sanitization",
                "افزایش پارامترها",
                "افزایش Temperature",
                "حذف Authentication"
            ],
            "answer": 0
        }
    ],

    15: [
        {
            "question": "Provenance به چه معناست؟",
            "options": [
                "منبع و تاریخچه داده",
                "اندازه مدل",
                "تعداد Token",
                "سرعت GPU"
            ],
            "answer": 0
        },
        {
            "question": "چرا Access Control در RAG مهم است؟",
            "options": [
                "هر Document مرتبط لزوماً برای هر User مجاز نیست",
                "برای افزایش سرعت GPU",
                "برای افزایش Context",
                "برای کاهش Dataset"
            ],
            "answer": 0
        },
        {
            "question": "کدام عبارت صحیح است؟",
            "options": [
                "RELEVANT = AUTHORIZED",
                "RELEVANT ≠ AUTHORIZED",
                "USER = ADMIN",
                "DOCUMENT = TRUSTED"
            ],
            "answer": 1
        }
    ]
}


def get_quiz(lesson_id):
    return QUIZZES.get(lesson_id, [])