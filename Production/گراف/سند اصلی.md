# شبکه توزیع‌شده و غیرمتمرکز هوش مصنوعی
## Decentralized Distributed AI Network

**نسخه سند:** 1.0  
**تاریخ:** 22 November 2026  
**پلتفرم نسخه اولیه:** Windows  
**نوع پروژه:** Open-Source Software

---

## راهنمای سند و محدوده آن

این سند، مشخصات یکپارچه محصول، معماری، رابط کاربری، شبکه محاسباتی، بازار خدمات، بلاک‌چین، کیف پول، اعتبارسنجی، Reputation، تحویل پروژه و تسویه مالی را در یک جریان پیوسته گردآوری می‌کند. بخش‌هایی که در نسخه اولیه به‌صورت الحاقیه مطرح شده بودند، در جای منطقی خود در ساختار اصلی قرار گرفته‌اند تا اجزای پروژه جدا از یکدیگر خوانده نشوند.

این بازآرایی به‌معنای حذف قابلیت‌ها یا قطعی‌کردن تصمیم‌های باز نیست. هرجا مقدار، روش، فرمول یا سیاست هنوز تعیین نشده، همان موضوع به‌عنوان «تصمیم باز» یا «نیازمند تعیین در مشخصات نهایی» حفظ شده است. مواردی که در متن با عنوان «پیشنهادی» آمده‌اند، همچنان پیشنهاد محسوب می‌شوند و تصمیم نهایی تلقی نمی‌شوند.

## فهرست مطالب

1. معرفی پروژه، هدف و معماری پایه  
2. پلتفرم و اصول کلی  
3. معماری رابط کاربری و ساختار اپلیکیشن  
4. کاتالوگ مدل‌های هوش مصنوعی و سیاست مجوز  
5. اجرای مدل به‌صورت محلی  
6. سیستم تعریف خدمات و وظایف هوش مصنوعی  
7. تاریخچه وظایف و سفارش‌ها  
8. سیستم پاداش، موجودی و Reputation  
9. ساخت شبکه محاسباتی توزیع‌شده  
10. پیوستن به شبکه موجود  
11. داشبورد و مدیریت شبکه محاسباتی  
12. Explore و بازار خدمات  
13. چرخه سفارش، پرداخت و تحویل  
14. معماری کلان و ارتباط دو شبکه  
15. بلاک‌چین اختصاصی و رمزارز بومی  
16. Blockchain & Wallet در رابط کاربری  
17. نقش‌های نود و تفکیک مسئولیت‌ها  
18. Validator Center و چرخه اعتبارسنج بلاک‌چین  
19. Task Verification Center و انتخاب کمیته‌ها  
20. Popularity Percentage و محاسبه Reputation  
21. تحویل فایل و ذخیره‌سازی خصوصی  
22. بازخورد مشتری و اثر آن بر Reputation  
23. Project Settlement Record  
24. اعتبارسنجی مرحله اول: نسبت ۸۰ به ۲۰  
25. اعتبارسنجی مرحله دوم: نسبت ۹۰ به ۱۰  
26. Final Settlement و پرداخت نهایی  
27. پاداش پروتکلی و برنامه انتشار ۲۰ ساله  
28. امنیت و حریم خصوصی  
29. محدودیت‌ها و ریسک‌های فنی اصلی  
30. مراحل پیشنهادی توسعه  
31. تصمیم‌های باز و موارد نیازمند نهایی‌سازی  
32. چشم‌انداز و اصل نهایی سیستم

---

# ۱. معرفی پروژه، هدف و معماری پایه

هدف پروژه، ساخت یک نرم‌افزار متن‌باز برای ویندوز است که به کاربران اجازه می‌دهد مدل‌های هوش مصنوعی دارای وزن قابل دریافت و مجوز مناسب را دانلود و اجرا کنند.

کاربر می‌تواند مدل را به‌صورت کامل روی کامپیوتر شخصی خود اجرا کند یا با ایجاد و پیوستن به یک شبکه توزیع‌شده، از توان محاسباتی چندین کامپیوتر برای اجرای مدل‌های بزرگ‌تر استفاده کند.

در معماری توزیع‌شده، مدل به بخش‌های اجرایی تقسیم می‌شود و هر کامپیوتر متناسب با توان سخت‌افزاری خود بخشی از مدل را اجرا می‌کند. خروجی محاسبات هر بخش به بخش بعدی منتقل می‌شود تا پاسخ نهایی تولید شود.

هدف نهایی، ایجاد زیرساختی جهانی و مشارکتی برای استفاده از منابع محاسباتی پراکنده و کاهش وابستگی کامل به دیتاسنترهای متمرکز است.

## ۱.۱. معماری محاسباتی اصلی

معماری پایه اجرای توزیع‌شده، **Pipeline Parallelism** است. در این روش، هر دستگاه تعدادی لایه یا بلوک متوالی از مدل را اجرا می‌کند و خروجی را به دستگاه بعدی می‌فرستد.

تقسیم درون یک لایه، موضوعی متفاوت به نام **Tensor Parallelism** است و به ارتباطات بیشتری میان دستگاه‌ها نیاز دارد. بنابراین، Tensor Parallelism نباید با تقسیم متوالی لایه‌ها در Pipeline Parallelism یکی فرض شود.

## ۱.۲. مرز میان محاسبات هوش مصنوعی و مدیریت شبکه

شبکه محاسباتی هوش مصنوعی مسئول اجرای مدل و انتقال داده‌های میانی است. در کنار آن، یک لایه مدیریتی و مالکیتی وجود دارد که هویت شبکه، تنظیمات، نقشه تقسیم مدل، وظایف، پرامپت‌ها، پاداش‌ها و سوابق لازم را مدیریت می‌کند. این لایه مدیریتی بخشی از معماری داخلی مدل نیست.

پروژه در سطح کلان دو زیرساخت مستقل اما مرتبط دارد: شبکه محاسبات هوش مصنوعی و شبکه بلاک‌چین. استقلال این دو به این معناست که عضویت در شبکه محاسباتی به‌خودی‌خود نقش اعتبارسنج بلاک‌چین ایجاد نمی‌کند.

---

# ۲. پلتفرم و اصول کلی

- نسخه اولیه فقط برای **Windows** توسعه داده می‌شود.
- زبان تمام رابط‌های کاربری انگلیسی است.
- پروژه متن‌باز خواهد بود.
- مدل‌ها باید از مخازن رسمی و تأییدشده دریافت شوند.
- مجوز هر نسخه مدل باید جداگانه بررسی شود.
- مدل‌ها باید برای استفاده موردنظر پروژه، از جمله توزیع وزن‌ها میان نودها، مجوز مناسب داشته باشند.
- معماری شبکه باید امکان اجرای محلی و اجرای توزیع‌شده را فراهم کند.
- دریافت‌پذیر بودن وزن‌های یک مدل به‌تنهایی به‌معنای مجاز بودن استفاده تجاری یا توزیع مجدد آن نیست.
- وضعیت مجوز وزن‌ها، کد، شرایط استفاده و امکان توزیع مدل باید برای همان نسخه مشخص بررسی شود.

به‌عنوان نمونه، در مشخصات اولیه پروژه ذکر شده است که مخزن رسمی Qwen3.6 مجوز Apache 2.0 را برای مدل‌های وزن‌باز خود اعلام کرده است؛ در عین حال، برخی نسخه‌های قدیمی‌تر Qwen مجوزها و شرایط جداگانه داشته‌اند. بنابراین، نباید تمام مدل‌های یک خانواده را دارای مجوز یکسان فرض کرد. این مثال باید هنگام پیاده‌سازی کاتالوگ با وضعیت دقیق همان نسخه تطبیق داده شود.

---

# ۳. معماری رابط کاربری و ساختار اپلیکیشن

تمام صفحات اپلیکیشن باید از یک ساختار یکپارچه پیروی کنند تا کاربر میان بخش‌های مدل، شبکه، خدمات، سفارش و بلاک‌چین تجربه‌ای منسجم داشته باشد.

## ۳.۱. ساختار پنجره اصلی

- **Navigation Sidebar:** منوی کناری برای دسترسی به بخش‌های مختلف.
- **Top Bar:** عنوان صفحه، مسیر دسترسی، وضعیت شبکه و بلاک‌چین، موجودی رمزارز و اعلان‌ها.
- **Main Content Area:** فضای اصلی نمایش صفحات و قابلیت‌ها.

نوار کناری باید امکان جمع‌شدن داشته باشد و رابط کاربری با تغییر اندازه پنجره ویندوز تطبیق پیدا کند.

## ۳.۲. منوی اصلی و ساختار گسترش‌یافته

ساختار پایه منوی اصلی پروژه شامل چهار بخش است:

1. **AI Workspace**
2. **Explore**
3. **Blockchain & Wallet**
4. **Settings**

در ساختار تفصیلی رابط کاربری، صفحات مدیریتی و عملیاتی زیر نیز در نظر گرفته می‌شوند:

- **Dashboard**
  - Overview
- **AI Workspace**
  - Run Model Locally
  - Create a Network
  - Join an Existing Network
  - Defined Tasks
  - Completed Tasks History
  - Rewards
- **Explore**
  - Discover Services
  - Categories
  - Search and Filters
- **Orders & Deliveries**
  - My Orders
  - Incoming Orders
  - Deliveries
  - Disputes
- **Blockchain & Wallet**
  - Overview
  - Wallet
  - Send
  - Receive
  - Transaction History
  - Reputation
  - Reputation Bonds
  - Validator Center
  - Task Verification Center
  - Coin Rules
  - Blockchain Explorer
- **Settings**
  - Account
  - Security
  - Wallet Security
  - Notifications
  - Privacy
  - Storage
  - Application Preferences

Dashboard و Orders & Deliveries در ساختار تفصیلی، صفحات سراسری و مدیریتی رابط کاربری هستند و قابلیت‌های اصلی AI Workspace، Explore، Blockchain & Wallet و Settings را جایگزین نمی‌کنند.

## ۳.۳. مسیرهای AI Workspace

در AI Workspace سه مسیر اصلی وجود دارد:

- **Run Model Locally**
- **Create a Network**
- **Join an Existing Network**

مسیر سوم برای مشارکت کامپیوترهای دیگر در شبکه‌هایی که قبلاً ساخته شده‌اند ضروری است. علاوه بر این مسیرها، Defined Tasks، Completed Tasks History و Rewards در همین فضای کاری در دسترس هستند.

## ۳.۴. نوار بالایی

نوار بالایی شامل موارد زیر است:

- Page Title
- Breadcrumb Navigation
- Internet Status
- Blockchain Synchronization Status
- Wallet Balance
- Notifications
- Account Menu

در صورت فعال بودن چند شبکه، انتخاب‌گر **Network** نیز نمایش داده شود.

## ۳.۵. داشبورد اصلی

صفحه Dashboard باید خلاصه‌ای از وضعیت کاربر را نمایش دهد.

**Account Overview**
- Available Balance
- Locked Reputation
- Locked Validator Stake
- Pending Rewards

**AI Overview**
- Active Models
- Active Networks
- Active Tasks
- Network Health

**Orders Overview**
- Incoming Orders
- Active Orders
- Completed Orders
- Orders Requiring Attention

**Recent Activity**
- Latest Transactions
- Latest Rewards
- Latest Orders
- Latest Network Events

**Quick Actions**
- Run Model
- Create Network
- Join Network
- Explore Services
- Open Wallet

اطلاعات مربوط به نقش‌هایی که کاربر فعال نکرده است، نباید به‌صورت غیرضروری نمایش داده شوند.

---

# ۴. کاتالوگ مدل‌های هوش مصنوعی و سیاست مجوز

مدل‌ها باید از مدل‌های سبک و کم‌مصرف تا مدل‌های بسیار بزرگ و قدرتمند دسته‌بندی شوند.

اطلاعات هر مدل در کاتالوگ:

- Model Name and Version
- Developer
- Official Repository
- Model Architecture
- Parameter Count
- Model Size
- Model Type
- Supported Tasks
- Minimum Hardware Requirements
- Recommended Hardware Requirements
- RAM and VRAM Requirements
- Download Size
- Supported Quantizations
- Supported Inference Engines
- Context Length
- License
- License Restrictions

## ۴.۱. سیاست دریافت و مجوز

مدل‌ها باید از مخازن رسمی و تأییدشده دریافت شوند. نسخه دقیق مدل و صحت فایل‌های دریافتی باید قابل بررسی باشد. مجوز مدل باید برای همان نسخه ثبت شود و شامل بررسی وزن‌ها، کد، شرایط استفاده و امکان توزیع وزن‌ها میان نودهای شبکه باشد.

قابل‌دانلود بودن مدل به‌معنای مجاز بودن استفاده تجاری، بازتوزیع وزن‌ها یا استفاده در تمام شکل‌های معماری پروژه نیست. کاتالوگ باید محدودیت‌های مجوز را به کاربر نمایش دهد و مدل ناسازگار با شیوه استفاده موردنظر پروژه را به‌عنوان گزینه مجاز شبکه معرفی نکند.

---

# ۵. اجرای مدل به‌صورت محلی

در صورت انتخاب **Run Model Locally**، فهرست مدل‌ها نمایش داده می‌شود. پس از انتخاب مدل، کاربر مشخصات سخت‌افزاری موردنیاز را مشاهده می‌کند و می‌تواند گزینه **Hardware Compatibility Test** را اجرا کند.

## ۵.۱. موارد آزمایش سخت‌افزار

- CPU
- GPU
- RAM
- VRAM
- Storage
- GPU Drivers
- Runtime Compatibility
- ظرفیت حافظه موردنیاز برای Context و اجرای مدل

## ۵.۲. نتیجه آزمایش

- **Compatible:** منابع حیاتی حداقل ۲۰ درصد بیشتر از نیاز تعیین‌شده باشند.
- **Compatible with Performance Warning:** حداقل منابع تأمین شده باشند، اما حاشیه اطمینان ۲۰ درصدی وجود نداشته باشد.
- **Not Compatible:** حداقل یکی از منابع ضروری تأمین نشده باشد.

معیار ۲۰ درصدی یک قاعده اولیه است و باید با Benchmark واقعی تکمیل شود؛ نتیجه تست سخت‌افزار نباید جایگزین اندازه‌گیری عملکرد واقعی مدل شود.

## ۵.۳. مراحل اجرای محلی

پس از تأیید سازگاری:

1. مدل از مخزن رسمی دریافت شود.
2. نسخه و صحت فایل‌ها بررسی شود.
3. موتور اجرای مدل نصب یا آماده شود.
4. مدل بارگذاری شود.
5. کاربر در همان اپلیکیشن و بدون نیاز به نرم‌افزار جداگانه با مدل گفتگو کند.

در این حالت، گفتگو و اجرای مدل به‌صورت محلی انجام می‌شود و برای پردازش مدل نیازی به شبکه محاسباتی دیگران نیست.

---

# ۶. سیستم تعریف خدمات و وظایف هوش مصنوعی

کاربر می‌تواند برای مدل محلی خود خدمات مشخصی تعریف کند و آن‌ها را در Explore عرضه کند. در صفحه **Defined Tasks**، فهرست وظایف تعریف‌شده و گزینه **Add New Task** نمایش داده می‌شود.

با انتخاب Add New Task، ابتدا نام وظیفه دریافت می‌شود و سپس سه بخش اصلی در اختیار مدیر وظیفه قرار می‌گیرد.

## ۶.۱. Input Parameters

مدیر وظیفه مشخص می‌کند مشتری چه اطلاعاتی باید وارد کند.

قواعد:

- حداکثر ۱۰۰ پارامتر برای هر وظیفه.
- نوع پارامتر: پاسخ تشریحی یا سؤال چهارگزینه‌ای.
- هر پارامتر دارای Keyword یکتا با حداکثر ۳۲ کاراکتر است.
- پارامترها می‌توانند اجباری یا اختیاری باشند.
- سؤال چهارگزینه‌ای دارای چهار گزینه تعریف‌شده است.
- مشتری باید تمام پارامترهای اجباری را تکمیل کند تا بتواند به مرحله بعد برود.

## ۶.۲. Main Prompt

مدیر وظیفه پرامپت اصلی را می‌نویسد و می‌تواند از اطلاعات دریافتی مشتری در آن استفاده کند.

روش درج متغیر به شکل زیر است:

`/keyword`

رفتار ویرایشگر:

- Keywordها آبی‌رنگ باشند.
- Keywordها از متن عادی متمایز باشند.
- با تایپ `/` فهرست Keywordهای موجود نمایش داده شود.
- امکان انتخاب و درج متغیر وجود داشته باشد.
- حذف یا تغییر نام Keyword در محل‌های استفاده‌شده شناسایی شود.

هنگام ثبت سفارش، مقدار واقعی پارامتر مشتری در محل متغیر مربوطه قرار می‌گیرد و پرامپت نهایی ساخته می‌شود.

ورودی مشتری باید به‌عنوان داده از دستورالعمل اصلی جدا باشد تا خطر **Prompt Injection** کاهش یابد. جای‌گذاری متغیرها نباید باعث شود متن ورودی مشتری به‌عنوان دستور قابل اعتماد سیستم تلقی شود.

## ۶.۳. General Information

اطلاعات عمومی هر وظیفه:

- Category
- Specialty
- Expected Response Time
- Contact Method
- Service Price (USD)
- Accepts External Payment (Yes / No)

زمان پاسخ، تخمینی است و نباید تضمین قطعی تلقی شود.

برای تبدیل قیمت دلاری به رمزارز، سیستم به منبع نرخ تبدیل معتبر نیاز دارد. تا زمانی که چنین منبعی وجود نداشته باشد، قیمت دلاری و ارزش رمزارز نباید معادل قطعی فرض شوند.

---

# ۷. تاریخچه وظایف و سفارش‌ها

در **Completed Tasks History**، وظایف تعریف‌شده به‌صورت بخش‌های جداگانه نمایش داده می‌شوند. با ورود به هر بخش، تاریخچه سفارش‌های مرتبط با آن وظیفه نمایش داده می‌شود.

اطلاعات هر سفارش:

- Task ID
- Date and Time
- Execution Status
- Start and Completion Time
- Payment Amount
- Approved Reward
- Payment Status
- Final Result

در حالت اجرای محلی، اطلاعات کامپیوترهای مشارکت‌کننده وجود ندارد.

در حالت ساخت شبکه، شناسه و لقب کامپیوترهایی که در انجام وظیفه شرکت کرده‌اند، به همراه کامپیوترهای غیرفعال یا دارای نقص نمایش داده می‌شوند.

در ساختار گسترش‌یافته اپلیکیشن، سوابق سفارش‌ها علاوه بر تاریخچه وظایف از طریق **Orders & Deliveries** نیز قابل دسترسی هستند؛ این بخش شامل My Orders، Incoming Orders، Deliveries و Disputes است.

---

# ۸. سیستم پاداش، موجودی و Reputation

تمام رابط کاربری این قسمت به زبان انگلیسی است. پاداش‌ها باید بر اساس منشأ خود تفکیک شوند و درآمد پرداختی مشتری نباید با انتشار رمزارز جدید یکسان در نظر گرفته شود.

## ۸.۱. وضعیت پاداش در حالت محلی

- Total Rewards Received
- Network-Approved Amount
- System Reward
- Available for Withdrawal
- Total Withdrawn

**Reputation**
- Reputation
- Good Reputation
- Bad Reputation
- Popularity Percentage

فرمول اولیه Reputation:

`Reputation = Bad Reputation / Good Reputation`

مقدار به‌صورت اعشاری نمایش داده می‌شود. اگر Good Reputation صفر باشد، مقدار **N/A** نمایش داده شود.

محدوده Popularity Percentage بین ۱۰ تا ۷۰ درصد است؛ فرمول آن در نسخه اولیه هنوز مشخص نشده بود. تعریف و فرمول تخصیص Popularity Percentage که در بخش ۲۰ این سند آمده، جزئیات بعدی همین مفهوم است.

## ۸.۲. وضعیت پاداش در حالت شبکه

- Total Rewards Received by Network
- Network-Approved Amount
- System Reward to Owner
- System Reward to Network Members
- Amount Distributed to Members
- Owner's Available for Withdrawal
- Owner's Total Withdrawn

بخش Reputation نیز شامل موارد زیر است:

- Good Reputation
- Bad Reputation
- Reputation
- Popularity Percentage

## ۸.۳. تفکیک انواع پاداش

سه نوع پاداش باید از یکدیگر مستقل باقی بمانند:

1. **Compute Rewards:** پاداش اجرای محاسبات مدل.
2. **Verification Rewards:** پاداش بررسی و تأیید صحت وظایف هوش مصنوعی.
3. **Blockchain Rewards:** رمزارز تولیدشده طبق قوانین بلاک‌چین و اجماع.

درآمد حاصل از پرداخت مشتری نباید با انتشار رمزارز جدید یکسان در نظر گرفته شود. Compute Rewards و پاداش‌های مرتبط با سفارش از منابع اقتصادی سفارش تأمین می‌شوند؛ Blockchain Rewards و پاداش انتشار پروتکلی تابع قوانین خود بلاک‌چین هستند.

---

# ۹. ساخت شبکه محاسباتی توزیع‌شده

با انتخاب **Create a Network**، کاربر وارد فرایند ساخت شبکه می‌شود. در این حالت صفحه چت وجود ندارد و پس از راه‌اندازی، داشبورد مدیریت شبکه نمایش داده می‌شود.

## ۹.۱. انتخاب مدل

مدل‌ها مشابه بخش محلی نمایش داده می‌شوند، اما باید قابلیت تقسیم به بخش‌های اجرایی سازگار با معماری خود را داشته باشند.

برای هر مدل، حداقل منابع موردنیاز کوچک‌ترین واحد اجرایی قابل‌پشتیبانی نمایش داده می‌شود. منظور از کوچک‌ترین واحد اجرایی، کوچک‌ترین بخشی است که موتور پروژه بتواند آن را مستقل به یک کامپیوتر اختصاص دهد و خروجی معتبر تولید کند؛ نه لزوماً کوچک‌ترین جزء ریاضی مدل.

## ۹.۲. ارزیابی سخت‌افزار

پس از **Hardware Compatibility Test**، اپلیکیشن ظرفیت کامپیوتر را برای اجرای بخش‌های متوالی مدل تخمین می‌زند.

موارد بررسی:

- RAM و VRAM
- CPU و GPU
- فضای ذخیره‌سازی
- سرعت و پایداری ارتباط
- سازگاری Runtime
- حاشیه اطمینان ۲۰ درصدی

تعداد بخش‌های قابل اجرا باید با Benchmark عملی نیز بررسی شود.

## ۹.۳. لایه مدیریتی و مالکیتی

کامپیوتر سازنده شبکه نقش **Network Owner** را بر عهده دارد.

موارد زیر باید به‌شکل امن در اختیار این نقش باشد:

- Network Identity
- Network Configuration
- Model Manifest
- Model Partition Map
- Defined Tasks
- Prompts
- Reward Settings
- Payout Addresses
- Ownership and Management Records
- Required Logs and Backups

این لایه، بخشی از معماری مدل نیست؛ بلکه لایه مالکیت و مدیریت شبکه است.

اطلاعات حساس باید رمزگذاری و پشتیبان‌گیری شوند. کامپیوتر مدیر نباید تنها محل نگهداری اطلاعات حیاتی شبکه باشد.

## ۹.۴. راه‌اندازی شبکه

پس از تأیید منابع:

1. ساخت شبکه.
2. ایجاد Network ID.
3. ایجاد هویت مدیر.
4. ثبت مدل و نقشه تقسیم آن.
5. ذخیره تنظیمات مدیریتی.
6. ثبت کامپیوتر مدیر به‌عنوان اولین عضو.

---

# ۱۰. پیوستن به شبکه موجود

کاربران دیگر باید بتوانند از طریق **Join an Existing Network** به شبکه‌های موجود بپیوندند.

مراحل:

1. وارد کردن شناسه یا دریافت دعوت‌نامه شبکه.
2. مشاهده اطلاعات مدل و منابع موردنیاز.
3. بررسی سخت‌افزار.
4. تخمین تعداد بخش‌های قابل اجرا.
5. تعیین میزان منابع قابل‌اختصاص.
6. ارسال درخواست عضویت.
7. تأیید مدیر و ثبت نود.

هر نود باید هویت فنی قابل‌تأیید داشته باشد. لقب نود صرفاً برای نمایش است.

کاربر باید بتواند محدودیت منابع CPU، GPU، RAM، VRAM و پهنای باند را مشخص کند و در صورت نیاز مشارکت خود را متوقف کند.

---

# ۱۱. داشبورد و مدیریت شبکه محاسباتی

پس از نصب و راه‌اندازی شبکه، داشبورد مدیریت شبکه نمایش داده می‌شود.

## ۱۱.۱. اطلاعات اصلی

- Selected AI Model
- Network ID
- Network Status
- Start / Stop Network
- Network Test

## ۱۱.۲. Network Test

آزمون شبکه باید موارد زیر را بررسی کند:

- ارتباط نودها
- سرعت انتقال داده
- تأخیر
- Packet Loss
- سازگاری مدل و Runtime
- ترتیب بخش‌ها
- اجرای آزمایشی یک درخواست کامل
- وجود بخش‌های بدون پوشش

## ۱۱.۳. پوشش مدل

درصد بخش‌های اجرایی تخصیص‌یافته نمایش داده شود. پوشش عادی و پوشش پشتیبان باید جدا باشند؛ زیرا تخصیص یک بخش به یک نود به‌تنهایی پایداری آن بخش را تضمین نمی‌کند.

## ۱۱.۴. اعضای شبکه

اطلاعات هر کامپیوتر:

- Node ID
- Node Alias
- Assigned Model Stages
- Resource Contribution
- Connection Status
- Last Seen

وضعیت‌ها:

- Active
- Inactive
- Weak Connection
- Unavailable

## ۱۱.۵. کامپیوترهای پشتیبان

اطلاعات:

- Node ID
- Node Alias
- Assigned Backup Role
- Connection Status
- Availability

در صورت قطع یا افت عملکرد نود اصلی، وظیفه با بررسی وضعیت محاسبات به نود جایگزین منتقل شود. انتقال وظیفه باید وضعیت آخرین محاسبات معتبر را در نظر بگیرد تا از دوباره‌کاری یا استفاده از خروجی ناسازگار جلوگیری شود.

---

# ۱۲. Explore و بازار خدمات

Explore فهرست خدمات هوش مصنوعی فعال را نمایش می‌دهد؛ چه خدمات محلی و چه خدمات شبکه‌ای.

اطلاعات هر آگهی:

- Service Name
- Provider
- Category
- Specialty
- AI Type: Local / Network
- Model
- Price
- Expected Response Time
- Availability
- Reputation
- Popularity Percentage

با کلیک روی هر خدمت، ابتدا اطلاعات عمومی کامل نمایش داده می‌شود. با انتخاب **Continue**، تمام Input Parameters تعریف‌شده توسط مدیر نمایش داده می‌شوند و مشتری باید اطلاعات اجباری را تکمیل کند.

## ۱۲.۱. کشف ارائه‌دهندگان

برای جست‌وجوی خدمات، یک سیستم کشف و فهرست‌کردن ارائه‌دهندگان لازم است. در معماری نهایی می‌توان از رجیستری توزیع‌شده استفاده کرد. استفاده از فهرست مرکزی در نسخه اولیه، بخشی از سیستم را متمرکز خواهد کرد.

## ۱۲.۲. پرداخت درون‌برنامه‌ای

در **In-App Payment**، پرداخت با رمزارز بومی پروژه انجام می‌شود. پس از تأیید نهایی تراکنش در بلاک‌چین، سفارش به‌صورت خودکار وارد صف اجرا می‌شود.

برای سفارش‌هایی که از سازوکار نگهداری موقت وجه استفاده می‌کنند، وضعیت Escrow و شرایط آزادسازی وجه باید مطابق قواعد مصوب مشخص باشد.

## ۱۲.۳. پرداخت خارج از برنامه

در **External Payment**، اگر مدیر روش پرداخت خارج از برنامه را پذیرفته باشد، سفارش وارد **Payment Verification Queue** می‌شود و پس از تأیید مدیر به صف اجرا منتقل می‌شود.

نحوه اتصال پرداخت خارجی به سند تسویه، قیمت ثبت‌شده، Reputation و بازپرداخت باید در سیاست نهایی سفارش‌های External Payment تعیین شود.

## ۱۲.۴. وضعیت‌های سفارش

- Draft
- Awaiting Payment
- Payment Pending
- Payment Verification
- Queued
- Running
- Completed
- Failed
- Cancelled
- Disputed
- Refunded

سیستم باید سازوکار حل اختلاف و بازپرداخت داشته باشد. برای پرداخت رمزارزی نیز باید وضعیت نگهداری موقت وجه و شرایط آزادسازی آن طراحی شود.

---

# ۱۳. چرخه سفارش، پرداخت و تحویل

چرخه سفارش باید میان ثبت درخواست مشتری، پرداخت، اجرای وظیفه، آماده‌سازی خروجی، تحویل، بازخورد، اعتبارسنجی و تسویه نهایی پیوستگی داشته باشد.

جریان پایه سفارش:

1. مشتری خدمت را در Explore پیدا می‌کند.
2. اطلاعات عمومی خدمت را بررسی می‌کند.
3. با انتخاب Continue، پارامترهای ورودی را تکمیل می‌کند.
4. سفارش و قرارداد آن ایجاد می‌شود.
5. پرداخت درون‌برنامه‌ای یا خارجی طبق روش پذیرفته‌شده انجام و بررسی می‌شود.
6. پس از تحقق شرط پرداخت، سفارش وارد صف اجرا می‌شود.
7. وظیفه توسط مدل محلی یا شبکه محاسباتی اجرا می‌شود.
8. ارائه‌دهنده فایل یا خروجی نهایی را بارگذاری می‌کند.
9. مشتری خروجی را دریافت و بررسی می‌کند.
10. مشتری Satisfied یا Not Satisfied را انتخاب می‌کند؛ در صورت عدم پاسخ، وضعیت No Feedback ثبت می‌شود.
11. سند سفارش و تسویه وارد اعتبارسنجی مرحله اول و سپس مرحله دوم می‌شود.
12. پس از قبولی بررسی‌ها، Final Settlement اجرا می‌شود.
13. پرداخت‌ها، Reputation، پاداش‌ها و وضعیت نهایی در سوابق ثبت می‌شوند.

این جریان باید وضعیت‌های خطا، لغو، اختلاف و بازپرداخت را نیز پوشش دهد. سفارش نباید صرفاً به دلیل گذشت زمان یا نبود پاسخ مشتری، به‌صورت خودکار دارای بازخورد مثبت یا منفی تلقی شود.

---

# ۱۴. معماری کلان و ارتباط دو شبکه

پروژه دارای دو شبکه مستقل اما مرتبط است.

## ۱۴.۱. AI Compute Network

اجزای اصلی:

- Compute Nodes
- Model Runtime
- Model Partition Manager
- Task Scheduler
- Node Discovery
- Network Coordinator
- Backup Node Manager
- Task Verification System

این بخش مسئول اجرای مدل‌ها، تقسیم مدل به بخش‌های اجرایی، تخصیص بخش‌ها به نودها، انتقال داده، مدیریت درخواست‌ها و بازیابی از خرابی نودهاست.

## ۱۴.۲. Blockchain Network

اجزای اصلی:

- Blockchain Core
- P2P Network
- Transaction System
- Consensus Mechanism
- Blockchain Validators
- Native Coin
- Wallet
- Explorer
- RPC / API
- Network Governance

این بخش دفترکل، تراکنش‌ها، اجماع، رمزارز بومی، کیف پول، ثبت سوابق مالی و قواعد حاکمیتی را مدیریت می‌کند.

## ۱۴.۳. استقلال نقش‌ها

یک نود محاسباتی لزوماً اعتبارسنج بلاک‌چین نیست. نود محاسباتی، Blockchain Full Node، Blockchain Validator و AI Task Verification Node نقش‌های جداگانه‌ای هستند. یک کامپیوتر ممکن است چند نقش را هم‌زمان داشته باشد، اما هویت، وثیقه، صلاحیت، پاداش و جریمه هر نقش باید جداگانه ثبت و مدیریت شود.

---

# ۱۵. بلاک‌چین اختصاصی و رمزارز بومی

هدف، ایجاد رمزارز **Native Coin** روی بلاک‌چین اختصاصی پروژه است، نه صرفاً امتیاز داخلی یا توکن روی شبکه دیگر.

## ۱۵.۱. اجزای بلاک‌چین

1. Blockchain Core
2. P2P Network
3. Consensus Mechanism
4. Transaction Validation
5. Native Coin
6. Block Rewards
7. Transaction Fees
8. Blockchain Explorer
9. RPC / API
10. Network Governance

## ۱۵.۲. کیف پول

کیف پول درون اپلیکیشن ویندوزی قرار می‌گیرد و قابلیت‌های زیر را دارد:

- ایجاد آدرس
- مدیریت کلید خصوصی
- امضای تراکنش
- ارسال و دریافت رمزارز
- نمایش موجودی
- نمایش سابقه تراکنش
- پشتیبان‌گیری و بازیابی

کلیدهای کیف پول، هویت نود، اعتبارسنج بلاک‌چین، مدیر شبکه و خزانه باید جداگانه مدیریت شوند.

## ۱۵.۳. پاداش‌ها و کارمزدها

سه نوع پاداش مستقل وجود دارد:

- Compute Rewards
- AI Task Verification Rewards
- Blockchain Validator / Block Rewards

تأیید خروجی یک وظیفه هوش مصنوعی با اجماع بلاک‌چین متفاوت است. صرفاً انتخاب ۱۰۰ نود و رأی‌گیری اکثریت، امنیت کافی ایجاد نمی‌کند؛ مقابله با هویت‌های جعلی، تبانی و رأی‌سازی ضروری است.

## ۱۵.۴. اقتصاد رمزارز

مواردی که باید در Tokenomics تعیین شوند:

- سقف عرضه ثابت یا انتشار مستمر
- نرخ انتشار رمزارز
- پاداش بلاک
- سهم مدیر
- سهم اعضای شبکه
- بودجه اعتبارسنجی وظایف
- کارمزد تراکنش
- خزانه شبکه
- جریمه رفتار مخرب

## ۱۵.۵. صرافی

برای ایجاد بلاک‌چین و رمزارز بومی، صرافی اختصاصی ضروری نیست. کاربران می‌توانند بدون صرافی:

- پاداش دریافت کنند.
- رمزارز را در کیف پول نگهداری کنند.
- به دیگران انتقال دهند.
- هزینه خدمات داخل اکوسیستم را پرداخت کنند.

صرافی فقط در صورت نیاز به مبادله رمزارز با دارایی‌های دیگر مطرح می‌شود و می‌تواند به مراحل آینده موکول شود.

وجود رمزارز به‌تنهایی قیمت بازار، ارزش اقتصادی یا نقدشوندگی ایجاد نمی‌کند. الزامات قانونی خدمات دارایی مجازی نیز باید پیش از عرضه عمومی بررسی شوند.

---

# ۱۶. Blockchain & Wallet در رابط کاربری

بلاک‌چین و کیف پول باید یک بخش مستقل و کامل در اپلیکیشن باشند و صرفاً به چند گزینه ساده ارسال و دریافت رمزارز محدود نشوند.

## ۱۶.۱. Blockchain Overview

این صفحه شامل دو قسمت اصلی است.

**Wallet Overview**
- Total Balance
- Available Balance
- Good Reputation Balance
- Bad Reputation Balance
- Locked Reputation
- Locked Validator Stake
- Pending Rewards
- Unbonding Balance

**Blockchain Overview**
- Blockchain Status
- Current Block Height
- Latest Finalized Block
- Connected Peers
- Active Blockchain Validators
- Average Transaction Fee
- Synchronization Status

در پایین صفحه:

- Recent Transactions
- Recent Rewards
- Recent Staking Events
- Recent Reputation Events

## ۱۶.۲. Wallet

امکانات:

- Create New Wallet
- Import / Restore Wallet
- Wallet Address
- Total Balance
- Available Balance
- Locked Balance
- Good Reputation
- Bad Reputation
- Transaction History
- Backup Status
- Recovery Status

کیف پول درون اپلیکیشن ویندوزی قرار می‌گیرد. در معماری **Self-Custody**، کلید خصوصی تحت کنترل کاربر باقی می‌ماند و نباید به‌صورت متن قابل‌خواندن روی سرور اپلیکیشن ذخیره شود.

### فرایند ایجاد کیف پول

1. Create New Wallet
2. Generate Wallet Keys
3. Secure Wallet Setup
4. Backup and Recovery Setup
5. Backup Confirmation
6. Wallet Activated

## ۱۶.۳. Send

اطلاعات لازم:

- Recipient Address
- Amount
- Network
- Transaction Fee
- Optional Memo

پیش از تأیید، موارد زیر نمایش داده شوند:

- Sender Address
- Recipient Address
- Transfer Amount
- Network Fee
- Total Amount

پس از امضای کاربر، وضعیت تراکنش نمایش داده شود:

- Signed
- Broadcast
- Pending
- Confirmed
- Finalized
- Failed

## ۱۶.۴. Receive

- Wallet Address
- QR Code
- Copy Address
- Selected Network
- Incoming Transactions
- Confirmation Status

## ۱۶.۵. Transaction History

تراکنش‌ها بر اساس نوع طبقه‌بندی شوند:

- Incoming
- Outgoing
- Compute Reward
- Verification Reward
- Blockchain Reward
- Reputation Lock
- Reputation Release
- Validator Stake
- Validator Unstake
- Refund
- Penalty

هر تراکنش باید صفحه جزئیات مستقل داشته باشد.

---

# ۱۷. نقش‌های نود و تفکیک مسئولیت‌ها

در پروژه سه نقش زیر مستقل هستند. یک کامپیوتر ممکن است هر سه نقش را اجرا کند، اما هویت، وثیقه، صلاحیت، پاداش و جریمه هر نقش باید جداگانه ثبت شود.

## ۱۷.۱. Blockchain Full Node

این نود:

- بلاک‌ها و تراکنش‌ها را دریافت می‌کند.
- اعتبار تراکنش‌ها را طبق قوانین پروتکل بررسی می‌کند.
- وضعیت دفترکل را نگهداری می‌کند.
- بلاک نامعتبر را طبق قوانین پروتکل رد می‌کند.

## ۱۷.۲. Blockchain Validator

این نود در سازوکار اجماع بلاک‌چین مشارکت می‌کند.

وظایف:

- مشارکت در اجماع.
- اعتبارسنجی وظایف تعیین‌شده توسط پروتکل.
- پیشنهاد یا تأیید بلاک، مطابق سازوکار انتخاب‌شده.
- حفظ امنیت دفترکل.
- دریافت پاداش پروتکلی و کارمزدهای مربوط به نقش خود.

## ۱۷.۳. AI Task Verification Node

این نود وظیفه بررسی اسناد مربوط به پروژه‌های هوش مصنوعی را بر عهده دارد.

وظایف:

- بررسی اطلاعات قرارداد سفارش.
- بررسی مبلغ پرداختی و درصد Popularity Percentage.
- بررسی سند تحویل.
- بررسی بازخورد مشتری.
- بررسی محاسبات Good Reputation و Bad Reputation.
- بررسی سهم پاداش‌ها.
- امضای دیجیتال نتیجه بررسی.

تأیید خروجی محاسبات مدل، اعتبارسنجی سند سفارش و اجماع بلاک‌چین سه مفهوم متفاوت‌اند و نباید در پیاده‌سازی یک عملیات واحد تلقی شوند.

---

# ۱۸. Validator Center و چرخه اعتبارسنج بلاک‌چین

صفحه **Validator Center** برای مدیریت نودهای اعتبارسنج بلاک‌چین است.

زیرصفحه‌ها:

- Validator Overview
- Become a Validator
- My Validator Nodes
- Validator Staking
- Unstaking
- Validator Rewards
- Validator Penalties
- Performance History

## ۱۸.۱. عضویت به‌عنوان Blockchain Validator

اطلاعات و شرایط:

- Validator ID
- Wallet Address
- Validator Identity
- Consensus Key
- Required Stake
- Hardware Requirements
- Network Requirements
- Software Version
- Expected Availability

## ۱۸.۲. مراحل عضویت

1. Become a Validator
2. Hardware Compatibility Test
3. Generate Validator Identity
4. Register Validator Key
5. Lock Required Stake
6. Submit Registration Transaction
7. Activation Queue
8. Validator Active

میزان حداقل وثیقه و شرایط سخت‌افزاری باید در **Coin Rules** مشخص شود.

## ۱۸.۳. وضعیت نود اعتبارسنج

- Not Registered
- Registration Pending
- Active
- Standby
- Inactive
- Exiting
- Unbonding
- Suspended
- Slashed

## ۱۸.۴. اطلاعات عملکرد

- Validator ID
- Stake Amount
- Uptime
- Successful Duties
- Missed Duties
- Consensus Participation
- Rewards Earned
- Penalties
- Last Activity

## ۱۸.۵. خروج از اعتبارسنجی

کاربر بتواند درخواست **Unstake** ثبت کند. پس از آن:

1. نود از انتخاب برای وظایف جدید خارج شود.
2. تعهدات فعال خود را تکمیل کند.
3. دوره Unbonding شروع شود.
4. پس از بررسی شرایط تخلف و پایان دوره، وثیقه آزاد شود.

---

# ۱۹. Task Verification Center و انتخاب کمیته‌ها

این صفحه برای افرادی است که می‌خواهند در بررسی اسناد و تأیید پروژه‌های هوش مصنوعی مشارکت کنند.

## ۱۹.۱. عضویت

موارد لازم:

- Wallet Address
- Task Verification Node ID- Verification Identity
- Required Verification Stake
- Software Version
- Availability Status
- Conflict of Interest Declaration

## ۱۹.۲. داشبورد اعتبارسنج وظایف

- Verification Node ID
- Eligibility Status
- Verification Stake
- Completed Reviews
- Pending Reviews
- Correctly Reviewed Tasks
- Verification Rewards
- Penalties
- Reputation History

## ۱۹.۳. انتخاب نودها برای بررسی یک سفارش

برای هر پروژه، یک کمیته ۱۰۰ عضوی از نودهای واجد شرایط انتخاب شود.

قواعد انتخاب:

- انتخاب تصادفی قابل‌راستی‌آزمایی.
- ثبت فهرست انتخاب‌شده در سیستم.
- جلوگیری از انتخاب نودهای دارای تعارض منافع.
- محدودیت بر اساس هویت مالکیت نودها برای مقابله با Sybil Attack.
- جلوگیری از کنترل بیش‌ازحد کمیته توسط یک مالک.

برای مرحله دوم، یک کمیته مستقل متشکل از ۱۰۰ نود دیگر انتخاب می‌شود که با اعضای کمیته اول هم‌پوشانی نداشته باشد.

در نتیجه، برای اجرای کامل این سازوکار در هر سفارش به حداقل ۲۰۰ نود واجد شرایط و مستقل نیاز است. اگر این تعداد فراهم نباشد، سفارش در حالت **Pending Verification** باقی می‌ماند و نباید تعداد کمتر از ۱۰۰ یا ۲۰۰ به‌عنوان تعداد کامل کمیته نمایش داده شود.

---

# ۲۰. Popularity Percentage و محاسبه Reputation

## ۲۰.۱. تعریف Popularity Percentage

**Popularity Percentage** درصدی از کل رمزارز پرداخت‌شده توسط مشتری برای هر سفارش است که به حساب Reputation ارائه‌دهنده خدمت اختصاص می‌یابد.

مقدار آن را مدیر خدمت تعیین می‌کند.

محدوده مجاز:

- Minimum: 10%
- Maximum: 70%

این درصد هنگام تعریف یا تنظیم خدمت مشخص می‌شود و در زمان پذیرش هر سفارش در قرارداد همان سفارش ثبت و ثابت می‌شود. اگر مدیر بعداً درصد خدمت را تغییر دهد، سفارش‌های قبلی تحت تأثیر قرار نمی‌گیرند.

## ۲۰.۲. متغیرهای محاسباتی

- **C:** کل مبلغ رمزارزی پرداخت‌شده بابت سفارش.
- **P:** Popularity Percentage انتخاب‌شده توسط مدیر.
- **G:** مقدار Good Reputation.
- **B:** مقدار Bad Reputation.
- **D:** مبلغ باقی‌مانده برای تقسیم عادی پاداش‌ها.

کارمزد انتقال شبکه از مبلغ پرداختی سفارش جداگانه ثبت می‌شود و در C محاسبه نمی‌شود.

## ۲۰.۳. حالت اول: مشتری راضی باشد

اگر مشتری گزینه **Satisfied** را انتخاب کند، تمام مقدار مربوط به Popularity Percentage به Good Reputation اختصاص پیدا می‌کند.

فرمول:

`G = C × P / 100`

`B = 0`

`D = C - G`

مثال: مبلغ پرداختی مشتری ۱۰۰۰ Coin و Popularity Percentage برابر ۳۰ درصد است.

نتیجه:

- Good Reputation: 300 Coin
- Bad Reputation: 0 Coin
- Remaining Distribution Amount: 700 Coin

## ۲۰.۴. حالت دوم: مشتری ناراضی باشد

اگر مشتری گزینه **Not Satisfied** را انتخاب کند، ۱۰ واحد درصد از کل مبلغ پرداختی به Bad Reputation اختصاص می‌یابد. مابقی درصد Popularity Percentage به Good Reputation تعلق می‌گیرد.

فرمول:

`B = C × 10 / 100`

`G = C × (P - 10) / 100`

`D = C - G - B`

مثال اول: مبلغ پرداختی ۱۰۰۰ Coin و Popularity Percentage برابر ۳۰ درصد است.

نتیجه:

- Bad Reputation: 100 Coin
- Good Reputation: 200 Coin
- Remaining Distribution Amount: 700 Coin

مثال دوم: مبلغ پرداختی ۱۰۰۰ Coin و Popularity Percentage برابر ۱۰ درصد است.

نتیجه:

- Bad Reputation: 100 Coin
- Good Reputation: 0 Coin
- Remaining Distribution Amount: 900 Coin

## ۲۰.۵. قاعده محاسباتی مهم

۱۰ درصد در این فرمول، ۱۰ واحد درصد از کل مبلغ سفارش است؛ نه ۱۰ درصد از مقدار Popularity Percentage.

بنابراین اگر Popularity Percentage برابر ۳۰ درصد باشد و مشتری ناراضی شود، مقدار Reputation به شکل ۲۰ درصد Good و ۱۰ درصد Bad تقسیم می‌شود.

## ۲۰.۶. ماهیت رمزارزهای Reputation

مقادیر Good Reputation و Bad Reputation باید در دو حساب مستقل Reputation ثبت شوند.

این مقادیر:

- به سفارش مشخص وابسته‌اند.
- در سند تسویه ثبت می‌شوند.
- در مجموع Reputation مالک خدمت محاسبه می‌شوند.
- در بخش Wallet نمایش داده می‌شوند.
- تا زمان تأمین شرایط آزادسازی، قابل‌انتقال و خرج‌کردن نیستند.

این مبالغ بدون حکم و فرایند مشخص نباید خودکار سوزانده یا به خزانه منتقل شوند. قواعد آزادسازی و جریمه باید در Coin Rules مشخص باشند.

## ۲۰.۷. فرمول Reputation و نحوه نمایش

فرمول فعلی حفظ می‌شود:

`Reputation = Bad Reputation / Good Reputation`

اگر Good Reputation صفر باشد، مقدار N/A نمایش داده شود.

مقادیر Good Reputation و Bad Reputation باید هم به‌صورت مقدار رمزارزی و هم به‌صورت سابقه تجمعی قابل مشاهده باشند.

Popularity Percentage یک پارامتر تخصیص رمزارز به Reputation است و نباید با درصد رضایت مشتری یا نرخ قبولی اعتبارسنج‌ها اشتباه شود.

---

# ۲۱. تحویل فایل و ذخیره‌سازی خصوصی

پس از تکمیل وظیفه، مدیر هوش مصنوعی باید فایل نهایی پروژه را روی فضای ذخیره‌سازی خصوصی متعلق به اپلیکیشن بارگذاری کند.

## ۲۱.۱. Upload Final Deliverable

در صفحه سفارش، گزینه **Upload Final Deliverable** وجود داشته باشد.

اطلاعات ثبت‌شده:

- Order ID
- Delivery ID
- File Name
- File Type
- File Size
- File Version
- Upload Timestamp
- SHA-256 File Hash

امکان بارگذاری چند فایل و بسته نهایی پروژه وجود داشته باشد.

## ۲۱.۲. نگهداری فایل

فایل نهایی باید در **Private Object Storage** متعلق به زیرساخت اپلیکیشن ذخیره شود.

قواعد:

- فایل در مخزن عمومی قرار نگیرد.
- نام و آدرس واقعی محل ذخیره‌سازی برای سایر کاربران قابل مشاهده نباشد.
- فایل هنگام نگهداری رمزگذاری شود.
- نوع واقعی فایل و حجم آن بررسی شود.
- فایل پیش از دانلود بررسی امنیتی شود.
- هش فایل ثبت شود.
- دسترسی هر فایل به Order ID و Customer ID مربوط به آن محدود باشد.

## ۲۱.۳. لینک دانلود خصوصی

پس از تأیید بارگذاری:

- سیستم یک مسیر دانلود خصوصی ایجاد کند.
- فقط مشتری ثبت‌شده در سفارش امکان دسترسی داشته باشد.
- مشتری پس از ورود به حساب خود بتواند فایل را دریافت کند.
- لینک دانلود کوتاه‌مدت و قابل لغو باشد.
- امکان تغییر Order ID برای دسترسی به فایل مشتری دیگر وجود نداشته باشد.
- تاریخچه دانلود ثبت شود.

صرف مخفی‌بودن URL کافی نیست؛ مجوز دسترسی باید در سمت سرور بررسی شود.

## ۲۱.۴. اعلان تحویل

پس از آماده‌شدن فایل:

- Delivery Available نمایش داده شود.
- مشتری اعلان دریافت کند.
- Download Project فعال شود.
- File Details و File Integrity قابل مشاهده باشند.
- زمان شروع مهلت بررسی مشتری ثبت شود.

---

# ۲۲. بازخورد مشتری و اثر آن بر Reputation

پس از تحویل و دریافت فایل، مشتری دو گزینه خواهد داشت:

- Satisfied
- Not Satisfied

## ۲۲.۱. Satisfied

در صورت انتخاب Satisfied:

- بازخورد مشتری در سند سفارش ثبت می‌شود.
- تمام سهم Popularity Percentage به Good Reputation اختصاص می‌یابد.
- سند وارد مرحله اول اعتبارسنجی می‌شود.

## ۲۲.۲. Not Satisfied

در صورت انتخاب Not Satisfied:

- بازخورد مشتری ثبت می‌شود.
- ۱۰ واحد درصد از کل مبلغ پرداختی به Bad Reputation اختصاص می‌یابد.
- اگر Popularity Percentage بیشتر از ۱۰ درصد باشد، بخش اضافه به Good Reputation می‌رود.
- سند وارد مرحله اول اعتبارسنجی می‌شود.

انتخاب Not Satisfied به‌تنهایی اثبات تخلف مدیر نیست؛ این انتخاب، فرمول Reputation را تعیین می‌کند. اگر مشتری ادعای نقض شرایط قرارداد داشته باشد، می‌تواند به‌صورت جداگانه **Dispute** ثبت کند.

## ۲۲.۳. عدم ثبت نظر

اگر مشتری در مهلت تعیین‌شده پاسخی ثبت نکند:

- وضعیت No Feedback ثبت شود.
- هیچ‌یک از دو گزینه Satisfied یا Not Satisfied به‌صورت خودکار به او نسبت داده نشود.
- بخش Reputation در حالت Pending باقی بماند تا طبق سیاست مصوب تعیین تکلیف شود.

---

# ۲۳. Project Settlement Record

برای هر سفارش تکمیل‌شده باید یک سند مستقل ایجاد شود.

نام سند: **Project Settlement Record**

این سند مرجع نهایی ثبت قرارداد، پرداخت، تحویل، نظر مشتری، Reputation، امضاهای اعتبارسنج‌ها و تقسیم پاداش‌هاست.

## ۲۳.۱. اطلاعات سفارش

- Settlement Record ID
- Order ID
- Task ID
- Provider ID
- Customer ID
- Network ID (if applicable)
- Model ID
- Model Version
- Created Timestamp

## ۲۳.۲. اطلاعات مالی قرارداد

- Agreed Service Price
- Payment Currency
- Actual Payment Amount
- Price Snapshot
- Exchange Rate Snapshot (if applicable)
- Popularity Percentage
- Good Reputation Allocation
- Bad Reputation Allocation
- Remaining Distribution Amount

## ۲۳.۳. اطلاعات پرداخت

- Payment Transaction ID
- Payment Amount
- Payment Asset
- Payment Timestamp
- Escrow ID
- Payment Status

## ۲۳.۴. اطلاعات Reputation

- Reputation Record ID
- Popularity Percentage
- Good Reputation Amount
- Bad Reputation Amount
- Reputation Lock Transaction
- Lock Status
- Release Status

## ۲۳.۵. اطلاعات تحویل

- Delivery ID
- File Manifest
- File Names
- File Hashes
- File Sizes
- Upload Timestamp
- Security Scan Status
- Private Storage Reference
- Customer Download Status

لینک خصوصی دانلود و اطلاعات خصوصی مشتری نباید به‌صورت عمومی در بلاک‌چین ذخیره شوند.

## ۲۳.۶. بازخورد مشتری

- Customer Feedback: Satisfied / Not Satisfied / No Feedback
- Feedback Timestamp
- Customer Signature
- Dispute Status

## ۲۳.۷. اطلاعات اعتبارسنجی مرحله اول

- First Committee ID
- Selected Validator Set
- Valid Vote Count
- Approval Count
- Rejection Count
- Approval Ratio
- Verification Result
- Validator Signatures
- Verification Timestamp

## ۲۳.۸. اطلاعات اعتبارسنجی مرحله دوم

- Audit Committee ID
- Selected Independent Validator Set
- Valid Audit Vote Count
- Audit Approval Count
- Audit Rejection Count
- Audit Ratio
- Audit Result
- Auditor Signatures
- Audit Timestamp

## ۲۳.۹. اطلاعات تقسیم پاداش

- Gross Payment
- Reputation Allocation
- Platform Fee
- Provider Reward
- Network Owner Reward
- Compute Rewards
- Task Verification Rewards
- Blockchain Validator Rewards
- Treasury Contribution
- Refund Amount
- Released Amount
- Pending Amount

## ۲۳.۱۰. اطلاعات بلاک‌چین

- Settlement Record Hash
- Blockchain Transaction ID
- Block Height
- Finality Status
- Settlement Timestamp

## ۲۳.۱۱. وضعیت سند

- Created
- Payment Locked
- Processing
- Delivery Uploaded
- Awaiting Customer Feedback
- Awaiting First Verification
- First Verification Closed
- Awaiting Second Verification
- Audit Completed
- Approved
- Disputed
- Rejected
- Settled
- Refunded
- Closed

در صورت نیاز به تعلیق پرداخت و جلوگیری از تسویه تا بررسی اختلاف، وضعیت Frozen نیز مطابق چرخه وضعیت‌های نهایی سند استفاده می‌شود.

## ۲۳.۱۲. محل نگهداری و ثبت

نسخه کامل سند در پایگاه داده خصوصی اپلیکیشن نگهداری شود. هش سند، شناسه سفارش، اطلاعات مالی لازم و ریشه رمزنگاری‌شده امضاها در بلاک‌چین ثبت شوند.

فایل پروژه، پرامپت خصوصی، اطلاعات شخصی مشتری و لینک دانلود در بلاک‌چین عمومی منتشر نشوند.

---

# ۲۴. اعتبارسنجی مرحله اول: نسبت ۸۰ به ۲۰

پس از ثبت بازخورد مشتری و تکمیل Project Settlement Record، مرحله اول اعتبارسنجی آغاز می‌شود.

## ۲۴.۱. کمیته اول

۱۰۰ نود Task Verification مستقل انتخاب می‌شوند.

هر نود باید اطلاعات زیر را بررسی کند:

- Order ID
- Agreed Service Price
- Actual Payment Amount
- Popularity Percentage
- Customer Feedback
- Good Reputation Calculation
- Bad Reputation Calculation
- Delivery Manifest
- File Hash
- Reward Distribution
- Record Integrity

## ۲۴.۲. امضای دیجیتال نودها

هر نود پس از بررسی، یک امضای دیجیتال منحصر‌به‌فرد در سند اعتبارسنجی پروژه ثبت می‌کند.

اطلاعات امضا:

- Validator Node ID
- Validator Public Key
- Settlement Record ID
- Settlement Record Version Hash
- Committee ID
- Vote
- Evidence Hash
- Block Height
- Signature

امضا باید به نسخه دقیق سند و محتوای دقیق رأی متصل باشد. تغییر هر مقدار در سند پس از امضا باید باعث نامعتبر شدن امضای مربوط به نسخه قبلی شود.

استفاده از استاندارد رمزنگاری معتبر و کتابخانه ممیزی‌شده الزامی است؛ الگوریتم امضای نهایی در مشخصات پروتکل تثبیت می‌شود.

## ۲۴.۳. قانون رأی‌گیری ۸۰/۲۰

تعداد رأی‌های معتبر باید ۱۰۰ باشد:

- حداقل ۸۰ رأی موافق
- حداکثر ۲۰ رأی مخالف

نمونه‌ها:

- ۸۰ موافق و ۲۰ مخالف: Approved
- ۸۵ موافق و ۱۵ مخالف: Approved
- ۹۰ موافق و ۱۰ مخالف: Approved
- ۷۹ موافق و ۲۱ مخالف: Not Approved

این نسبت حداقل آستانه قبولی است، نه الزام به دقیقاً ۸۰ رأی موافق و ۲۰ رأی مخالف. عدم پاسخ یک نود به‌عنوان رأی موافق محسوب نمی‌شود.

## ۲۴.۴. بسته‌شدن مرحله اول

پس از دریافت ۱۰۰ رأی معتبر:

- نتیجه رأی‌گیری توسط پروتکل محاسبه می‌شود.
- امضاها و نسبت رأی بررسی می‌شوند.
- رویداد First Verification Closed ثبت می‌شود.
- نتیجه مرحله اول در سند سفارش ذخیره می‌شود.

آخرین نودی که رأی معتبر خود را ارسال می‌کند، می‌تواند تراکنش تکمیل‌کننده این مرحله را ارسال کند؛ اما اختیار نهایی بستن مرحله با آن نود نیست. وضعیت باید به‌صورت خودکار توسط قوانین بلاک‌چین تعیین شود.

---

# ۲۵. اعتبارسنجی مرحله دوم: نسبت ۹۰ به ۱۰

پس از بسته‌شدن مرحله اول، یک کمیته مستقل دیگر انتخاب می‌شود. این کمیته باید شامل ۱۰۰ نود دیگر باشد که با ۱۰۰ نود مرحله اول هم‌پوشانی نداشته باشند.

وظیفه این کمیته، بررسی صحت مرحله اول است؛ نه تکرار بی‌هدف همان رأی‌گیری.

موارد بررسی:

- صحت امضاهای کمیته اول.
- مستقل‌بودن اعضای دو کمیته.
- صحت تعداد رأی‌های معتبر.
- درست‌بودن محاسبه نسبت ۸۰/۲۰.
- صحت محاسبه Popularity Percentage.
- صحت محاسبه Good Reputation و Bad Reputation.
- تطابق مقادیر مالی با قرارداد ثبت‌شده.
- عدم تغییر سند پس از امضا.
- عدم پرداخت تکراری پاداش.
- رعایت شرایط انتخاب اعتبارسنج‌ها.

## ۲۵.۱. قانون رأی‌گیری ۹۰/۱۰

تعداد رأی‌های معتبر باید ۱۰۰ باشد:

- حداقل ۹۰ رأی موافق
- حداکثر ۱۰ رأی مخالف

نمونه‌ها:

- ۹۰ موافق و ۱۰ مخالف: Approved
- ۹۵ موافق و ۵ مخالف: Approved
- ۸۹ موافق و ۱۱ مخالف: Not Approved

## ۲۵.۲. نتیجه ممیزی

در صورت قبولی:

- Audit Completed ثبت شود.
- نتیجه مرحله اول تأیید نهایی شود.
- سند برای Final Settlement آماده گردد.

در صورت عدم قبولی:

- Settlement در وضعیت Frozen قرار گیرد.
- پرداخت‌های مربوط به سند نهایی نشوند.
- علت اختلاف ثبت شود.
- سند وارد فرایند Dispute / Re-Review شود.

---

# ۲۶. Final Settlement و پرداخت نهایی

پس از قبولی مرحله اول ۸۰/۲۰ و مرحله دوم ۹۰/۱۰، سند وارد مرحله **Final Settlement** می‌شود.

مراحل:

1. نهایی‌کردن Project Settlement Record.
2. تأیید صحت پرداخت مشتری.
3. تأیید تخصیص Good Reputation.
4. تأیید تخصیص Bad Reputation.
5. تأیید Reputation Locks.
6. محاسبه کارمزد پلتفرم.
7. محاسبه Provider Reward.
8. محاسبه Network Owner Reward (if applicable).
9. محاسبه Compute Rewards.
10. محاسبه Task Verification Rewards.
11. محاسبه Blockchain-related Rewards.
12. آزادسازی مبالغ مجاز از Escrow.
13. ثبت تراکنش‌های پاداش.
14. ثبت Final Settlement Hash.
15. اعلام Settlement Completed.

هیچ پرداختی نباید دوبار انجام شود. هر خروجی مالی باید به Settlement Record ID مربوط باشد و وضعیت آن در دفترکل ثبت شود.

---

# ۲۷. پاداش پروتکلی و برنامه انتشار ۲۰ ساله

## ۲۷.۱. هدف

برای تشویق نودهایی که در امنیت بلاک‌چین و اعتبارسنجی پروژه‌های هوش مصنوعی مشارکت می‌کنند، بخشی از رمزارز بومی طبق قوانین پروتکل به‌عنوان **Protocol Node Incentive** منتشر شود. این انتشار باید طی ۲۰ سال به‌تدریج کاهش پیدا کند و پس از پایان سال بیستم به صفر برسد.

## ۲۷.۲. مدل پیشنهادی انتشار

پیشنهاد اصلی، کاهش خطی سالانه ۵ واحد درصد از نرخ پایه پاداش است.

فرمول:

`Reward Multiplier = max(0, 100 - 5 × Completed Protocol Years)`

این درصد، سهم نرخ پاداش از مقدار پایه اولیه است؛ نه درصدی از کل موجودی کیف پول یا مبلغ سفارش.

## ۲۷.۳. برنامه زمانی

| زمان از شروع شبکه | درصد نرخ پایه پاداش نودها |
|---|---:|
| آغاز شبکه | 100% |
| پایان سال ۱ | 95% |
| پایان سال ۲ | 90% |
| پایان سال ۳ | 85% |
| پایان سال ۴ | 80% |
| پایان سال ۵ | 75% |
| پایان سال ۶ | 70% |
| پایان سال ۷ | 65% |
| پایان سال ۸ | 60% |
| پایان سال ۹ | 55% |
| پایان سال ۱۰ | 50% |
| پایان سال ۱۱ | 45% |
| پایان سال ۱۲ | 40% |
| پایان سال ۱۳ | 35% |
| پایان سال ۱۴ | 30% |
| پایان سال ۱۵ | 25% |
| پایان سال ۱۶ | 20% |
| پایان سال ۱۷ | 15% |
| پایان سال ۱۸ | 10% |
| پایان سال ۱۹ | 5% |
| پایان سال ۲۰ | 0% |

در نتیجه:

- در آغاز شبکه، ۱۰۰ درصد نرخ پایه پرداخت می‌شود.
- پس از ۱۰ سال، نرخ پاداش به ۵۰ درصد مقدار پایه می‌رسد.
- پس از ۲۰ سال، انتشار جدید رمزارز برای این برنامه پاداش به صفر می‌رسد.

کاهش‌ها بر اساس سال پروتکلی و ارتفاع بلاک تعریف می‌شوند، نه ساعت کامپیوتر کاربران؛ زیرا زمان محلی دستگاه‌ها قابل اعتماد نیست.

## ۲۷.۴. تفاوت با مدل بیت‌کوین

این برنامه عین مدل بیت‌کوین نیست. در بیت‌کوین، پاداش جدید بلاک هر ۲۱۰٬۰۰۰ بلاک، تقریباً هر چهار سال، نصف می‌شود. کارمزد تراکنش‌ها نیز بخشی از پاداش ماینرها هستند.

مرجع درج‌شده در طرح اولیه برای این مقایسه:

https://developer.bitcoin.org/reference/block_chain.html

در مدل پیشنهادی این پروژه، کاهش پاداش خطی و سالانه است تا در پایان ۲۰ سال به صفر برسد. این انتخاب به دلیل الزام زمانی پروژه است و باید پس از شبیه‌سازی اقتصادی و ارزیابی امنیت شبکه نهایی شود.

## ۲۷.۵. منبع پاداش در هر دوره

سه جریان پاداش باید مستقل باقی بمانند:

**الف) Protocol Node Incentives**  
رمزارز جدیدی که طبق برنامه ۲۰ ساله برای تشویق نودهای واجد شرایط منتشر می‌شود.

**ب) Transaction Fee Rewards**  
کارمزد تراکنش‌های بلاک‌چین که مطابق قوانین اجماع بین نقش‌های مجاز توزیع می‌شود.

**ج) Project Verification Fees**  
بخشی از هزینه سفارش‌ها که برای بررسی و تأیید پروژه‌های هوش مصنوعی اختصاص داده می‌شود.

بعد از پایان ۲۰ سال:

- انتشار جدید در برنامه Protocol Node Incentives صفر می‌شود.
- کارمزد تراکنش‌ها همچنان می‌تواند منبع درآمد اعتبارسنج‌های بلاک‌چین باشد.
- هزینه اعتبارسنجی پروژه‌ها می‌تواند از کارمزد یا بودجه همان سفارش تأمین شود.
- پاداش محاسباتی نودها همچنان از مبلغ سفارش و قواعد Compute Rewards تأمین می‌شود.

بنابراین پایان انتشار تشویقی ۲۰ ساله نباید به‌معنای پایان کامل درآمد نودها باشد.

## ۲۷.۶. تقسیم پاداش میان نقش‌ها

پاداش پروتکلی باید میان نقش‌های مجاز تقسیم شود:

- Blockchain Validators
- AI Task Verification Nodes

نسبت دقیق تقسیم این دو سهم در Tokenomics نهایی تعیین می‌شود.

نودهای پردازشی هوش مصنوعی از مسیر Compute Rewards پاداش می‌گیرند و نباید درآمد حاصل از اجرای سفارش با پاداش انتشار جدید رمزارز دوباره‌شماری شود.

## ۲۷.۷. معیار دریافت پاداش

دریافت پاداش اعتبارسنجی پروژه وابسته به صرفاً موافق یا مخالف بودن رأی نیست.

معیارها:

- ثبت رأی معتبر در مهلت مقرر.
- امضای دیجیتال معتبر.
- بررسی اطلاعات لازم.
- نداشتن تعارض منافع.
- رعایت دستورالعمل پروتکل.
- عبور از بررسی‌های ممیزی.

رأی مخالف به‌تنهایی دلیل رفتار مخرب نیست.

---

# ۲۸. امنیت و حریم خصوصی

امنیت باید در سطح نودهای محاسباتی، داده‌های مشتری، کیف پول، بلاک‌چین، مدیریت شبکه، فایل‌های تحویلی و فرایند اعتبارسنجی در نظر گرفته شود.

## ۲۸.۱. امنیت نودها

- رمزنگاری ارتباطات.
- هویت قابل‌تأیید نودها.
- جلوگیری از پیام‌های تکراری و دستکاری‌شده.
- ممنوعیت اجرای کد ناشناس ارسالی از نودهای دیگر.
- اجرای مدل در محیط محدود و ایزوله.
- بررسی صحت فایل‌های مدل.
- امضای معتبر نسخه‌های نرم‌افزار.
- محدودیت دسترسی به منابع سیستم.

## ۲۸.۲. اطلاعات مشتری و داده‌های میانی

رمزنگاری ارتباطات به‌تنهایی تضمین نمی‌کند که داده‌های میانی مدل برای نودهای پردازش‌کننده قابل مشاهده نباشند.

بنابراین لازم است:

- اطلاعات ورودی حداقلی باشند.
- ماهیت پردازش توزیع‌شده به مشتری توضیح داده شود.
- اطلاعات حساس غیرضروری ارسال نشوند.
- داده‌های موقت بی‌دلیل ذخیره نشوند.
- راهکارهای پیشرفته‌تر محاسبات محرمانه برای آینده بررسی شوند.

## ۲۸.۳. امنیت کیف پول

- حفاظت از کلید خصوصی.
- پشتیبان‌گیری و بازیابی.
- تأیید مبلغ و آدرس پیش از امضا.
- جلوگیری از Double Spending.
- جداسازی کلیدهای نقش‌های مختلف.
- حفاظت از خزانه و کلیدهای مدیریتی.

## ۲۸.۴. امنیت اسناد و فایل‌های تحویلی

- ذخیره فایل‌های نهایی در مخزن خصوصی.
- رمزگذاری فایل در حالت ذخیره.
- کنترل نوع واقعی فایل و اندازه آن.
- بررسی امنیتی پیش از دانلود.
- احراز مجوز سمت سرور برای هر درخواست دانلود.
- ثبت هش فایل و تاریخچه دانلود.
- عدم انتشار فایل پروژه، پرامپت خصوصی، اطلاعات مشتری یا لینک دانلود در بلاک‌چین عمومی.

## ۲۸.۵. حملات و خطاهای مورد بررسی

- Sybil Attack
- Double Spending
- Node Impersonation
- Replay Attack
- Malicious Node
- Collusion
- Denial of Service
- Network Partition
- Conflicting Transactions
- Invalid Computation Results
- Owner Node Failure

---

# ۲۹. محدودیت‌ها و ریسک‌های فنی اصلی

۱. تأخیر اینترنت می‌تواند سرعت Pipeline Parallelism را به‌شدت محدود کند.

۲. تفاوت سخت‌افزار نودها، تقسیم متوازن مدل را دشوار می‌کند.

۳. خاموشی یا قطع ارتباط کامپیوترها به سیستم بازیابی نیاز دارد.

۴. بررسی صحت خروجی مدل‌های هوش مصنوعی پیچیده‌تر از تأیید تراکنش‌های معمولی است.

۵. تمرکز تمام اطلاعات مدیریتی روی کامپیوتر مالک می‌تواند شبکه را به یک نقطه شکست مرکزی وابسته کند؛ به همین دلیل اطلاعات حیاتی به رمزگذاری و پشتیبان‌گیری نیاز دارند و نباید فقط در دستگاه مدیر نگهداری شوند.

۶. استفاده از منابع میلیون‌ها کامپیوتر به‌معنای دستیابی خودکار به عملکرد یک دیتاسنتر یا ابررایانه نیست؛ کارایی باید با آزمایش واقعی اثبات شود.

۷. دسترس‌پذیری و استقلال دو کمیته ۱۰۰ نودی برای هر سفارش، نیازمند حداقل ۲۰۰ نود واجد شرایط و مستقل است. در نبود این ظرفیت، سفارش باید در وضعیت Pending Verification باقی بماند.

۸. ذخیره فایل تحویلی در Private Object Storage متعلق به زیرساخت اپلیکیشن، نیازمند طراحی دقیق کنترل دسترسی و مدیریت زیرساخت ذخیره‌سازی است و به‌خودی‌خود ماهیت غیرمتمرکز شبکه محاسباتی را تضمین نمی‌کند.

۹. اجرای مدل‌های بزرگ روی نودهای ناهمگون، نیازمند Benchmark، مدیریت حافظه، زمان‌بندی، سازگاری Runtime و بازیابی از خطاست؛ تخمین منابع به‌تنهایی تضمین‌کننده عملکرد قابل قبول نیست.

---

# ۳۰. مراحل پیشنهادی توسعه

ترتیب پیشنهادی توسعه برای رسیدن از محصول محلی به اکوسیستم کامل:

1. اجرای محلی مدل و ساخت رابط اصلی.
2. اجرای یک مدل تقسیم‌شده روی دو کامپیوتر در شبکه محلی.
3. آزمایش ارتباط میان کامپیوترها از طریق اینترنت.
4. ساخت سیستم عضویت، تخصیص لایه و نود پشتیبان.
5. ساخت Defined Tasks و Explore.
6. ساخت سیستم سفارش، پرداخت آزمایشی و تاریخچه.
7. ساخت سیستم اعتبارسنجی وظایف.
8. ساخت بلاک‌چین آزمایشی و کیف پول آزمایشی.
9. اتصال پاداش‌ها و پرداخت‌ها به بلاک‌چین.
10. ارزیابی امنیتی، اقتصادی و حقوقی پیش از شبکه اصلی.

این ترتیب از اجرای مدل و اثبات امکان تقسیم محاسبات آغاز می‌شود و سپس به بازار خدمات، تسویه و زیرساخت بلاک‌چین گسترش می‌یابد.

---

# ۳۱. تصمیم‌های باز و موارد نیازمند نهایی‌سازی

موارد زیر بخشی از پروژه‌اند، اما مقدار یا سازوکار نهایی آن‌ها هنوز تعیین نشده است. ثبت این موارد به‌عنوان تصمیم باز مانع از آن می‌شود که یک پیشنهاد اولیه به‌اشتباه الزام قطعی پیاده‌سازی تلقی شود.

## ۳۱.۱. معماری هوش مصنوعی

- مدل‌های اولیه کدام‌اند؟
- نسخه اول فقط مدل متنی دارد یا تصویر و صوت نیز پشتیبانی می‌شود؟
- کوچک‌ترین واحد اجرایی هر مدل چگونه تعریف می‌شود؟
- آیا Tensor Parallelism در آینده اضافه می‌شود؟
- حداکثر تعداد نودهای یک شبکه چقدر است؟
- آیا یک کامپیوتر می‌تواند هم‌زمان عضو چند شبکه شود؟

## ۳۱.۲. بازار خدمات و سفارش‌ها

- معیار دقیق زمان پاسخ چیست؟
- شرایط رد سفارش و بازپرداخت چگونه است؟
- اختلاف مشتری و ارائه‌دهنده چگونه حل می‌شود؟
- پرداخت خارج از برنامه چگونه تأیید می‌شود؟
- قیمت دلاری چگونه و با چه منبعی به رمزارز تبدیل می‌شود؟
- سیاست سفارش‌های دارای External Payment چگونه با محاسبات Reputation هماهنگ می‌شود؟
- در صورت عدم پاسخ مشتری، بخش Popularity Percentage چگونه تعیین تکلیف می‌شود؟
- در صورت نارضایتی مشتری، چه شرایطی باعث آغاز Dispute می‌شود؟

## ۳۱.۳. اعتبارسنجی و پاداش

- اعتبارسنج‌ها چگونه انتخاب می‌شوند؟
- تعداد اعتبارسنج‌های هر وظیفه ثابت است یا متغیر؟
- مقابله با هویت جعلی و تبانی چگونه انجام می‌شود؟
- فرمول Compute Rewards و Verification Rewards چیست؟
- سهم مدیر و اعضای شبکه چگونه محاسبه می‌شود؟
- فرمول Popularity Percentage چیست؟
- در صورت تأیید نشدن مرحله اول یا دوم اعتبارسنجی، کمیته جدید چگونه انتخاب شود؟

## ۳۱.۴. بلاک‌چین و رمزارز

- عرضه ثابت است یا انتشار مستمر؟
- سازوکار اجماع چیست؟
- پاداش بلاک چگونه تقسیم می‌شود؟
- رمزارز فقط در اکوسیستم کاربرد دارد یا کاربرد عمومی‌تری خواهد داشت؟
- قیمت خدمات با دلار تعیین و سپس تبدیل می‌شود یا مستقیماً با رمزارز؟
- کیف پول Self-Custody خواهد بود یا Managed؟
- آیا در آینده اتصال به صرافی‌ها یا سایر بلاک‌چین‌ها انجام می‌شود؟
- مقدار پایه اولیه پاداش نودها در هر بلاک یا دوره چقدر باشد؟
- سهم Protocol Node Incentives بین Blockchain Validators و AI Task Verification Nodes چقدر باشد؟
- حداقل Validator Stake چقدر باشد؟
- حداقل Task Verification Stake چقدر باشد؟
- دوره آزادسازی هر نوع وثیقه چقدر باشد؟
- مقدار جریمه قابل اعمال بر وثیقه در هر نوع تخلف چگونه تعیین شود؟
- درصد دقیق Platform Fee چقدر باشد؟
- سهم Compute Rewards، Provider Rewards و Verification Fees از مبلغ سفارش چگونه تقسیم شود؟

## ۳۱.۵. Reputation و تسویه

- فرمول و محدوده دقیق Popularity Percentage در سیاست کامل سیستم چگونه مستند می‌شود؟
- برای No Feedback چه مهلت و چه سیاست نهایی اعمال می‌شود؟
- قواعد آزادسازی Good Reputation و Bad Reputation چیست؟
- چه شرایطی برای سوزاندن، انتقال یا جریمه مبالغ Reputation لازم است؟
- اختلاف مشتری و ارائه‌دهنده چه اثری بر آزادسازی Escrow و Reputation دارد؟
- در صورت Frozen شدن Settlement، مرجع و فرایند رفع انسداد چیست؟
- چگونه از تسویه یا پرداخت تکراری در تمام مسیرها جلوگیری می‌شود؟

## ۳۱.۶. کمیته‌های بررسی

- منبع تصادفی قابل‌راستی‌آزمایی برای انتخاب اعضای کمیته چیست؟
- مالکیت مشترک نودها چگونه تشخیص داده می‌شود؟
- تعارض منافع چگونه اعلام، تشخیص و اعمال می‌شود؟
- اگر یک یا چند نود پس از انتخاب غیرفعال شوند، جایگزینی آن‌ها چگونه انجام می‌شود؟
- پس از عدم قبولی یک مرحله، کمیته جدید چگونه انتخاب می‌شود؟
- دوره اعتراض و Re-Review چقدر است؟

---

# ۳۲. چشم‌انداز و اصل نهایی سیستم

هدف نهایی، ایجاد اکوسیستمی مستقل شامل دو زیرساخت اصلی است:

## ۳۲.۱. شبکه هوش مصنوعی توزیع‌شده

کامپیوترهای شخصی با همکاری یکدیگر مدل‌های بزرگ را اجرا می‌کنند و خدمات هوش مصنوعی ارائه می‌دهند.

## ۳۲.۲. بلاک‌چین و رمزارز اختصاصی

شبکه‌ای مستقل برای ثبت تراکنش‌ها، پرداخت هزینه خدمات، مدیریت پاداش‌ها و ایجاد انگیزه اقتصادی برای مشارکت‌کنندگان ایجاد می‌شود.

## ۳۲.۳. نقش کاربران در اکوسیستم

در این اکوسیستم:

- کاربران مدل‌ها را محلی یا توزیع‌شده اجرا می‌کنند.
- صاحبان کامپیوترها منابع خود را به شبکه اختصاص می‌دهند.
- ارائه‌دهندگان خدمات هوش مصنوعی تعریف و عرضه می‌کنند.
- مشتریان خدمات را از Explore پیدا و سفارش می‌دهند.
- پرداخت درون‌برنامه‌ای با رمزارز بومی انجام می‌شود.
- مشارکت‌کنندگان و اعتبارسنج‌ها طبق قوانین مشخص پاداش می‌گیرند.
- بلاک‌چین مستقل، دفترکل و سوابق مالی را نگهداری می‌کند.

## ۳۲.۴. اصل نهایی تسویه و اعتبار

هر سفارش باید یک سند تراکنش مستقل، امضاشده، قابل ممیزی و مرتبط با شناسه یکتای خودش داشته باشد.

این سند باید از لحظه ثبت سفارش تا تحویل، بازخورد مشتری، محاسبه Reputation، بررسی ۱۰۰ نود اول، ممیزی ۱۰۰ نود دوم و تسویه نهایی، تمام رویدادهای مالی و اعتبارسنجی را ثبت کند.

در نهایت، پرداخت‌ها، وثیقه‌ها، پاداش‌ها، اعتبار و سوابق مشارکت باید از طریق همین سند و قوانین بلاک‌چین به یکدیگر متصل شوند.

**اصل معماری:** هیچ پاداش، Reputation، وثیقه یا تسویه مالی نباید بدون ارتباط با یک سفارش مشخص و یک سند تسویه قابل‌راستی‌آزمایی ثبت شود.

## ۳۲.۵. چشم‌انداز نهایی

تبدیل کامپیوترهای شخصی به زیرساخت محاسباتی جهانی و مشارکتی، همراه با یک اقتصاد دیجیتال مستقل برای مدیریت خدمات و پاداش‌های شبکه.