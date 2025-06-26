# 🎓 Academic Management System

একটি সম্পূর্ণ Academic Management System যা Flask এবং Python দিয়ে তৈরি করা হয়েছে। এই সিস্টেমটি শিক্ষাপ্রতিষ্ঠানের জন্য ক্লাস ম্যানেজমেন্ট, রেজাল্ট ম্যানেজমেন্ট এবং রুটিন ম্যানেজমেন্ট এর সুবিধা প্রদান করে।

## ✨ ফিচারগুলি

### 🔐 ইউজার ম্যানেজমেন্ট
- **অ্যাডমিন প্যানেল** - সম্পূর্ণ সিস্টেম কন্ট্রোল
- **ইউজার অথেনটিকেশন** - সুরক্ষিত লগইন সিস্টেম
- **রোল-বেসড অ্যাক্সেস** - অ্যাডমিন এবং সাধারণ ইউজার

### 📚 ক্লাস ম্যানেজমেন্ট
- **স্টুডেন্ট রেজিস্ট্রেশন** - নতুন স্টুডেন্ট যোগ করা
- **অ্যাটেনডেন্স ট্র্যাকিং** - দৈনিক উপস্থিতি রেকর্ড
- **অ্যাসেসমেন্ট ম্যানেজমেন্ট** - পরীক্ষার ফলাফল ট্র্যাক
- **আর্কাইভ সিস্টেম** - পুরানো ডেটা সংরক্ষণ

### 📊 রেজাল্ট ম্যানেজমেন্ট
- **সেশন ম্যানেজমেন্ট** - একাডেমিক সেশন তৈরি
- **সাবজেক্ট ম্যানেজমেন্ট** - কোর্স এবং বিষয় যোগ করা
- **মার্কস এন্ট্রি** - পরীক্ষার ফলাফল ইনপুট
- **রেজাল্ট ভিউ** - স্টুডেন্ট এবং কোর্স-ওয়াইজ ফলাফল
- **রেজাল্ট আর্কাইভ** - পুরানো ফলাফল সংরক্ষণ

### 📅 রুটিন ম্যানেজমেন্ট
- **টিচার ম্যানেজমেন্ট** - শিক্ষকদের তথ্য
- **রুম ম্যানেজমেন্ট** - ক্লাসরুম অ্যাসাইনমেন্ট
- **কোর্স অ্যাসাইনমেন্ট** - শিক্ষক-কোর্স ম্যাপিং
- **রুটিন জেনারেশন** - অটোমেটিক রুটিন তৈরি

## 🚀 ইনস্টলেশন

### স্থানীয় ডেভেলপমেন্ট

1. **Repository ক্লোন করুন**
```bash
git clone https://github.com/yourusername/academic-management-system.git
cd academic-management-system
```

2. **Virtual Environment তৈরি করুন**
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# অথবা
venv\Scripts\activate  # Windows
```

3. **Dependencies ইনস্টল করুন**
```bash
pip install -r requirements.txt
```

4. **Environment Variables সেট করুন**
```bash
# .env ফাইল তৈরি করুন
SECRET_KEY=your_secret_key_here
FLASK_ENV=development
```

5. **ডাটাবেস ইনিশিয়ালাইজ করুন**
```bash
python init_db.py
```

6. **অ্যাডমিন ইউজার তৈরি করুন**
```bash
python create_admin.py
```

7. **অ্যাপ্লিকেশন চালু করুন**
```bash
python app.py
```

### Cpanel ডিপ্লয়মেন্ট

#### GitHub Actions এর মাধ্যমে (অটোমেটিক)
1. **GitHub Secrets সেট করুন**
   - `CPANEL_HOST`
   - `CPANEL_USERNAME`
   - `CPANEL_PASSWORD`
   - `CPANEL_PORT`

2. **Code Push করুন**
```bash
git add .
git commit -m "Setup deployment"
git push origin main
```

3. **GitHub Actions অটোমেটিক ডিপ্লয় করবে**

#### ম্যানুয়াল ডিপ্লয়
1. **Deployment Package ডাউনলোড করুন**
```bash
./deploy_cpanel.sh
```

2. **ZIP ফাইল Cpanel এ আপলোড করুন**
3. **Python App সেটআপ করুন**
4. **ডাটাবেস কনফিগার করুন**

## 📁 প্রজেক্ট স্ট্রাকচার

```
academic-management-system/
├── app.py                          # মূল Flask অ্যাপ্লিকেশন
├── models.py                       # ডাটাবেস মডেল
├── user_models.py                  # ইউজার মডেল
├── extensions.py                   # Flask এক্সটেনশন
├── requirements.txt                # Python dependencies
├── requirements_cpanel.txt         # Cpanel dependencies
├── passenger_wsgi.py              # Cpanel entry point
├── create_admin.py                # অ্যাডমিন ইউজার স্ক্রিপ্ট
├── .htaccess                      # Apache configuration
├── .github/
│   └── workflows/
│       └── deploy-cpanel.yml      # GitHub Actions workflow
├── blueprints/                    # Flask blueprints
│   ├── auth/                      # অথেনটিকেশন
│   ├── class_management/          # ক্লাস ম্যানেজমেন্ট
│   ├── result_management/         # রেজাল্ট ম্যানেজমেন্ট
│   └── routine_management/        # রুটিন ম্যানেজমেন্ট
├── templates/                     # HTML templates
├── static/                        # CSS, JS, Images
├── migrations/                    # Database migrations
├── instance/                      # Instance-specific files
└── uploads/                       # Uploaded files
```

## 🔧 কনফিগারেশন

### Environment Variables
```env
SECRET_KEY=your_secret_key_here
DATABASE_URL=mysql://username:password@localhost/database_name
FLASK_ENV=production
CPANEL=1
```

### ডাটাবেস সেটআপ
- **Local**: SQLite (default)
- **Production**: MySQL/PostgreSQL

## 📊 ডাটাবেস স্কিমা

### মূল টেবিলগুলি
- **users** - ইউজার অ্যাকাউন্ট
- **students** - স্টুডেন্ট তথ্য
- **teachers** - শিক্ষক তথ্য
- **classes** - ক্লাস তথ্য
- **subjects** - বিষয় তথ্য
- **sessions** - একাডেমিক সেশন
- **marks** - পরীক্ষার ফলাফল
- **attendance** - উপস্থিতি রেকর্ড
- **routines** - ক্লাস রুটিন

## 🛠️ ডেভেলপমেন্ট

### নতুন ফিচার যোগ করা
1. **Blueprint তৈরি করুন**
2. **মডেল ডিফাইন করুন**
3. **রাউটস যোগ করুন**
4. **টেমপ্লেট তৈরি করুন**
5. **মাইগ্রেশন রান করুন**

### টেস্টিং
```bash
# Unit tests
python -m pytest tests/

# Integration tests
python -m pytest tests/integration/
```

## 🔒 সিকিউরিটি

- **Password Hashing** - bcrypt ব্যবহার
- **Session Management** - Flask-Login
- **CSRF Protection** - Flask-WTF
- **Input Validation** - Form validation
- **SQL Injection Protection** - SQLAlchemy ORM

## 📈 পারফরম্যান্স

- **Database Optimization** - Indexed queries
- **Static File Caching** - Browser caching
- **Template Caching** - Jinja2 optimization
- **Database Connection Pooling** - Production ready

## 🤝 কন্ট্রিবিউশন

1. **Fork করুন** এই repository
2. **Feature branch** তৈরি করুন (`git checkout -b feature/AmazingFeature`)
3. **Commit করুন** আপনার changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push করুন** branch এ (`git push origin feature/AmazingFeature`)
5. **Pull Request** তৈরি করুন

## 📝 লাইসেন্স

এই প্রজেক্টটি MIT লাইসেন্সের অধীনে লাইসেন্সকৃত। দেখুন `LICENSE` ফাইলটি বিস্তারিত তথ্যের জন্য।

## 📞 সাপোর্ট

- **Issues**: GitHub Issues ব্যবহার করুন
- **Documentation**: `docs/` ফোল্ডার দেখুন
- **Email**: your-email@example.com

## 🙏 ধন্যবাদ

- **Flask** - Web framework
- **SQLAlchemy** - Database ORM
- **Bootstrap** - CSS framework
- **Font Awesome** - Icons

---

⭐ যদি এই প্রজেক্টটি আপনার কাছে ভালো লাগে, তাহলে একটি star দিন!