# This Python file uses the following encoding: utf-8
from telegram.ext import *
from telegram import ParseMode


token = "TOKEN"

print('Starting up bot...')


# Lets us use the /start command
def start_command(update, context):
    update.message.reply_text('''
    Hello there! I\'m a Mostafa Karimi. How can I help you?\n
    Please use command 😄

    Source-Code: [Github](https://github.com/MKarimi21/MKarimi21/blob/master/TelegramBot/mkarimi21bot.py)
    \n\n
    سلام من مصطفی کریمی هستم. چه کمکی میتونم بهتون بکنم؟
    \n
    لطفا از دستورات زیر استفاده کنید 😄
    
    سورس کد ربات: [Github](https://github.com/MKarimi21/MKarimi21/blob/master/TelegramBot/mkarimi21bot.py)
    ''', parse_mode=ParseMode.MARKDOWN)


# Lets us use the /help command
def help_command(update, context):
    update.message.reply_text('''
    If you need help, please contact me on my telegram:\n
    @mkarimi21\n
    \n
    اگر به کمکی نیاز دارید، لطفا با من در تلگرام تماس بگیرید:\n
    @mkarimi21
    ''')


# Lets us use the /about_me command
def about_command(update, context):
    about_fa=f'''
    👨🏻‍💻    من کارشناس ارشد مهندسی صنایع در گرایش بهینه‌سازی سیستم‌ها هستم. در زمینه یادگیری ماشین و مدیریت و کنترل پروژه مهارت دارم. به تازگی وارد حوزه مدیریت محصول مبتنی بر یادگیری ماشین شده‌ام و علاقه‌مندم در این حوزه به‌صورت حرفه‌ای فعالیت داشته باشم.
    هدف من استفاده از دانش و مهارت مدیریت محصول، هوش تجاری، یادگیری ماشین و... هست که با تیم‌های شرکت‌ها و سازمان‌ها به‌صورت چابک برای توسعه و بهبود آن همکاری بکنم و نقش اثربخشی داشته باشم.
    ✌🏼💪🏼
    '''
    about_en=f'''
    👨🏻‍💻    I have an MSc in industrial engineering with concentrations in machine learning, project planning and control, and systems optimization. I recently entered the field of machine learning product management and am eager to advance professionally in this field.
    I aim to use my knowledge and skills in product management, business intelligence, machine learning, etc. and collaborate with teams of companies and organizations in an agile manner. This will enable me to develop and improve the product and to play an influential role.
    ✌🏼💪🏼
    '''
    update.message.reply_text(about_en, parse_mode=ParseMode.MARKDOWN)
    update.message.reply_text(about_fa, parse_mode=ParseMode.MARKDOWN)

# Lets us use the /contact_me command
def contact_me_command(update, context):
    cantact_me = f'''
    You can contact me by: [🥷🏼](https://t.me/mkarimi21bot)

    - 👨‍💻 All of my projects are available at [Github-Repo](https://github.com/MKarimi21?tab=repositories)  
    
    - 🌐 My website is available at [My WebSite](https://www.mkarimi21.ir)
    
    - 📝🔜 I regularly write articles on [My Blog](https://www.mkarimi21.ir)
    
    - 📫 How to reach me [MailBox](me@mkarimi21.ir?subject=Hello%20Mostafa,%20I%20contact%20you%20from%20Telegram%20Bot)
    
    - 📞 You can call me at: 09159830611
    
    - 🔗 My LinkedIn: [LinkedIn](https://www.linkedin.com/in/mkarimi21)
    
    - 🐱 My GitHub: [GitHub](https://www.github.com/mkarimi21)
    
    - 🐦 My Twitter: [Twitter](https://www.twitter.com/mkarimi21)
    
    - 📷 My Instagram: [Instagram](https://www.instagram.com/mkarimi21)
    
    - 📺 My YouTube: [YouTube](https://www.youtube.com/channel/UCpVgQSEvrK-HWU6osjqhFCA)
    
    - 🆔 My Telegram: [Telegram](https://t.me/mkarimi21)


    💞❤️💕💮
    - ☕️ Support Me: [Buy The Coffie](https://coffeebede.ir/mkarimi21)
    \n
    \n
    '''
    update.message.reply_text(cantact_me, parse_mode=ParseMode.MARKDOWN)

# Lets us use the /work command
def work_command(update, context):
    update.message.reply_text('I tell you very soon 🤨🧐', parse_mode=ParseMode.MARKDOWN)

# Lets us use the /experience command
def experience_command(update, context):
    exp_fa=f'''
    
⚓️  _شرکت مهندسین مشاور خاک سازه بارمان - ۱۳۹۹ - ۱۴۰۱_
    
    ⌛️ *کارشناس ارشد برنامه‌ریزی و کنترل پروژه*
    انجام اولیه و تقویم پروژه، تعریف فاکتورهای وزنی، فرمول نویسی و استخراج و تنظیم گزارش‌های پیشرفت ماهانه پروژه و کنترل اسناد مدارک و پیشرفت مهندسی و مناقصات را برعهده داشتم.
    🔖 - پروژه احداث پایانه صادراتی در مجتمع بندری نگین - بوشهر - ایران
    🔖 - طرح، تهیه، حمل، ساخت و نصب و راه‌اندازی اسکله شناور در بندر مردمی سوزا قشم - هرمزگان - ایران
    🔖 - خدمات نظارت کارگاهی و نظارت عالیه طرح احداث تاسیسات خشکی و پسکرانه مارینا - چابهار - ایران
    
    📈 *کارشناس مهندسی ارزش*
    به‌عنوان یکی از کارشناسان و عضو تیم مهندسی ارزش  درجهت تصمیم‌گیری و بالابردن شاخص‌های با ارزش در پروژه‌های تدوین شده با بررسی موانع، نیازها و تصمیمات در چرایی انتخاب روش انجام کار و بهبود و بهینه آن نقش داشتم.
    🔖 - مطالعه مهندسی ارزش پروژه اسکله نفتی و کریدور خطوط لوله نفتی شهید بهشتی چابهار - ایران 
    🔖 - مطالعه مهندسی ارزش پروژه به‌روزرسانی سامانه رسوبگیر بندر نوشهر - ایران
    
    🌐 [WebPage](http://khaksazeh.com/) | 🔗 [LinkedIn](https://www.linkedin.com/company/khaksazeh)

🔃  _پروژه همکاری با دانشگاه بجنورد - ۱۴۰۰_

    📒 *پروژه شناسایی و مدل‌سازی فرایندهای سازمانی ادارات نظارت بر اجرای استاندارد، امور آزمایشگاه‌ها، تایید صلاحیت و سیستم‌های مدیریت کیفیت، امور حقوقی، آموزش و ترویج و اندازه‌شناسی اوزان و مقیاس‌های اداره کل استاندارد خراسان شمالی*
    بهبود و پیاده‌سازی با استفاده از روش مدیریت فرایندهای کسب و کار BPMN ادارات ذی‌ربط اداره استاندارد خراسان شمالی

    🔗 [LinkedIn](https://www.linkedin.com/in/hossein-karimi-8a452153/)

🚢  _شرکت مجستیک مارین قشم - ۱۳۹۷_

    ⛓ *کارشناس لجستیک و مدل‌سازی*
    برنامه‌ریزی، مدل‌سازی و بهینه‌سازی ارسال مارین و اسکله‌های شناور از کارخانه مجستیک مارین امارات و قشم به پروژه احداث اسکله‌های تفریحی و تجاری بندر انزلی

    🌐 [WebPage](http://www.majesticjetties.ir/)
    
    '''
    exp_en=f'''
⚓️  _Khak Sazeh Barman Consulting - Jun 2020 - Sep 2022_ 

    ⌛️ *Senior project planning and control*
    I was in charge of making the initial settings and project calendar, defining weighting factors, writing and extracting and setting up monthly project progress reports, and controlling the documents and engineering progress and tenders.
    🔖 - Export terminal construction project in Negin port complex
    🔖 - Design, procurement, transportation, construction, and installation of a floating dock in Souza Qeshm People's Port
    🔖 - Workshop supervision services and high supervision of the construction of the onshore and offshore facilities of the Marina 

    📈 *Value engineering practitioner*
    As an expert member of the value engineering team, I played a critical role in decision-making and raising important indicators in the proposed projects by examining obstacles, needs, and reasons behind why the suggested method and optimization were chosen.
    🔖 - Engineering study of the value engineering of Shahid Beheshti oil wharf and oil pipeline corridor, Chabahar.
    🔖 - Engineering study of the value of the project of updating the sedimentation system of Bandar Nowshahr.

    🌐 [WebPage](http://khaksazeh.com/) | 🔗 [LinkedIn](https://www.linkedin.com/company/khaksazeh)

🔃 _Project collaboration with the University of Bojnord - 2021_  

    📒 *Bojnord municipality has assigned Mahya Pardaz the task of auditioning and registering the properties of Bojnord in the municipality system. Due to the high volume of documents, management and planning of the process were required and it was done with project management software for planning and allocation.*
    Improvement and implementation using the BPMN business process management method of relevant departments of the Standards Department.

    🔗 [LinkedIn](https://www.linkedin.com/in/hossein-karimi-8a452153/)

🚢  _Majestic Jetties & Marinas - Jun 2018 - Feb 2019_

    ⛓ *Logistics and project planning and control*
    Modeling and planning of the delivery of marine and floating docks from the Majestic Marine factory of Emirates and Qeshm to the construction project of recreational and commercial docks of Bandar Anzali.
    
    🌐 [WebPage](http://www.majesticjetties.ir/)
    '''
    update.message.reply_text(exp_en, parse_mode=ParseMode.MARKDOWN)
    update.message.reply_text(exp_fa, parse_mode=ParseMode.MARKDOWN)

# Lets us use the /edu command
def edu_command(update, context):

    edu_fa=f'''
    🎓 سال ۱۳۹۸ - ۱۴۰۰ - در رشته مهندسی صنایع مفطع کارشناسی ارشد گرایش بهینه‌سازی سیستم‌ها \n
    🏫 _دانشگاه دولتی بجنورد_\n
    📗 عنوان پایان‌نامه:
    *توسعه مدل یادگیرنده پیش‌بینی الگوی مصرف گاز به‌منظور تصمیم‌گیری راهبردهای شرکت گاز خراسان شمالی* \n
    در این پایان‌نامه با استفاده از مدل‌های یادگیری عمیق (سری‌های زمانی) و کتابخانه پای‌تورچ برای پیش‌بینی حجم مصرف گاز استان صورت گرفت که با خروجی پیش‌بینی اقدام به تخصیص گاز در ماه‌های سال بامدل‌های تصمیم‌گیری انجام شده است و جهت دقت بالا و درستی به‌صورت چابک برای هر فیچر با کارفرما در ارتباط بودم.\n\n
    🎓 سال ۱۳۹۳ - ۱۳۹۷ - در رشته مهندسی صنایع مقطع کارشناسی \n
    🏫 _دانشگاه فنی مهندسی اسفراین_\n
    📘 عنوان پایان‌نامه:
    *برنامه‌ریزی و زمان‌بندی ثبت اسناد ممیزی شهرستان بجنورد توسط شرکت محیا پرداز با نرم‌افزار MS Project*\n
    شرکت محیا پرداز با مجوز از شهرداری بجنورد وظیفه ممیزی و ثبت اسناد املاک بجنورد در سامانه شهرداری را دارد. به‌دلیل حجم بالای اسناد نیازمند مدیریت و برنامه‌ریزی فرایند آن بود که با استفاده از نرم‌افزار مدیریت پروژه برای برنامه‌ریزی و تخصیص آن انجام دادم که زمان کل فرایند در حالت عادی به نصف کاهش پیدا کرد.\n
    📄 مقاله کنفرانسی#۱: [سیویلیکا](https://civilica.com/doc/851848/)
    📄 مقاله کنفرانسی#۲: [سیویلیکا](https://civilica.com/doc/851847/)
        
    @mkarimi21
    @mkarimi21bot
    '''
    edu_en=f'''
    🎓 2019 - 2021 - MSc of Systems Optimization in Industrial Engineering \n
    🏫 _University of Bojnord_\n
    📗 Thesis Title:
    *Extended learning predictive model for gas consumption pattern in order to decide the strategies of North Khorasan Gas Company*\n
    For this thesis, deep learning models (time series) and the PyTorch library were used to forecast the gas consumption volume of the province. For each month of the year, the gas allocation action has been done with decision-making models, and for high accuracy, every feature for forecasting is unique. While on the project, I was in contact with the employer using the agile method.\n\n
    🎓 2014 - 2018 - Bachelor of Science in Industrial Engineering \n
    🏫 _Esfarayen University of Technology_\n
    📘 Thesis Title: 
    *Real Estate Audit Planning and Scheduling with MS Project Software (Case Study: Bojnourd Municipality)*\n
    Mahia Pardaz Company, with a license from Bojnord municipality, is responsible for auditing and registering Bojnord real estate documents in the municipal system. Due to the high volume of documents, it was necessary to manage and plan the process, which I did by using the project management software to plan and allocate it, which reduced the time of the whole process to half.\n
    📄 Publication#1: [Civilica-Conf](https://en.civilica.com/doc/851848/)
    📄 Publication#2: [Civilica-Conf](https://en.civilica.com/doc/851847/)
    
    @mkarimi21
    @mkarimi21bot
    '''
    update.message.reply_text(f'{edu_en}' ,parse_mode=ParseMode.MARKDOWN)
    update.message.reply_text(f'{edu_fa}' ,parse_mode=ParseMode.MARKDOWN)

# Lets us use the /skills command
def skills_command(update, context):
    skill_tree = '''
    ```

Skills/
    ├── Python/
    │   ├── Machine Learning/
    │   │   └── Deep Learning/
    │   ├── Time Series/
    │   ├── Analyzing/
    │   ├── OOP/
    │   └── Selenium/
    ├── Git&GitHub/
    ├── SQL/
    ├── MSP & Excel & Visio/
    ├── MS BI & Tableau/
    ├── Agile Methodology/
    │   ├── Scrum/
    │   ├── Kanban/
    │   ├── Trello & Miro/
    │   └── V Paradigm/
    └── COMFAR/
    ```

    @mkarimi21
    @mkarimi21bot
    '''
    update.message.reply_text(skill_tree, parse_mode=ParseMode.MARKDOWN)
    


# Lets us use the /resume command
def resume_command(update, context):
    caption_en='My General Resume - Rev Oct 2022\n\nand you can See-Online: \n\n\t\t\t\t [_*Link*_](https://drive.google.com/file/d/1PyqYQZedPN0R9YF7yQmz2nWPIXQIoTwg/view?usp=sharing)\n\n@mkarimi21\n@mkarimi21bot\n'
    context.bot.sendDocument(update.effective_chat.id, document=open('Mostafa-Karimi-Resume-En-Rev09-.pdf', 'rb'), caption=caption_en, parse_mode=ParseMode.MARKDOWN)

    caption_fa='رزومه عمومی من - ویرایش مهرماه ۱۴۰۱\n\nو به صورت آنلاین: \n\n\t\t\t\t [_*لینک*_](https://drive.google.com/file/d/13wcIyOd4RcvJlF-RMi8n8u7HQjoQs8V5/view?usp=sharing) \n\n@mkarimi21\n@mkarimi21bot'
    context.bot.sendDocument(update.effective_chat.id, document=open('Mostafa-Karimi-Resume-Fa-Rev09-.pdf', 'rb'), caption=caption_fa, parse_mode=ParseMode.MARKDOWN)

def handle_response(text) -> str:
    # Create your own response logic

    if 'hello' in text:
        return 'Hey there!'

    if 'سلام' in text:
        return 'سلام به شما'

    if 'how are you' in text:
        return 'I\'m good!'
    
    if "حالت چطوره" in text:
        return 'عالی'

    return 'I don\'t understand'


def handle_message(update, context):
    # Get basic info of the incoming message
    message_type = update.message.chat.type
    text = str(update.message.text).lower()
    response = ''

    # Print a log for debugging
    print(f'User ({update.message.chat.id}) says: "{text}" in: {message_type}')

    # React to group messages only if users mention the bot directly
    if message_type == 'group':
        # Replace with your bot username
        if '@mkarimi21bot' in text:
            new_text = text.replace('@mkarimi21bot', '').strip()
            response = handle_response(new_text)
    else:
        response = handle_response(text)

    # Reply normal if the message is in private
    update.message.reply_text(response)


# Log errors
def error(update, context):
    print(f'Update {update} caused error {context.error}')


# Run the program
if __name__ == '__main__':
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('about_me', about_command))
    dp.add_handler(CommandHandler('contact_me', contact_me_command))
    dp.add_handler(CommandHandler('work', work_command))
    dp.add_handler(CommandHandler('experience', experience_command))
    dp.add_handler(CommandHandler('edu', edu_command))
    dp.add_handler(CommandHandler('skills', skills_command))
    dp.add_handler(CommandHandler('resume', resume_command))

    # Messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Log all errors
    dp.add_error_handler(error)

    # Run the bot
    updater.start_polling(1.0)
    updater.idle()
