# 🚀 Cpanel Deployment Summary

## ✅ প্রস্তুত ফাইলগুলি
আপনার প্রজেক্টে নিম্নলিখিত ফাইলগুলি তৈরি হয়েছে:

1. **`passenger_wsgi.py`** - Cpanel এর জন্য মূল entry point
2. **`requirements_cpanel.txt`** - Cpanel এর জন্য compatible dependencies
3. **`deploy_cpanel.sh`** - Deployment script
4. **`cpanel_deploy/`** - Deployment ফোল্ডার (ZIP করা হয়েছে)
5. **`academic_management_cpanel.zip`** - Cpanel এ আপলোড করার জন্য ZIP ফাইল
6. **`.htaccess`** - স্ট্যাটিক ফাইল হ্যান্ডলিং এর জন্য

## 📋 Cpanel এ ডিপ্লয় করার ধাপগুলি

### ধাপ ১: ফাইল আপলোড
1. Cpanel এর File Manager খুলুন
2. `public_html` ফোল্ডারে যান
3. `academic_management_cpanel.zip` ফাইলটি আপলোড করুন
4. ZIP ফাইলটি এক্সট্রাক্ট করুন

### ধাপ ২: Python App সেটআপ
1. Cpanel → Software → Setup Python App
2. নিম্নলিখিত তথ্য দিন:
   - **Python version**: 3.8 বা তার উপরে
   - **Application startup file**: `passenger_wsgi.py`
   - **Application entry point**: `application`
   - **Application URL**: আপনার ডোমেইন

### ধাপ ৩: ডাটাবেস সেটআপ
1. Cpanel → MySQL Databases
2. একটি নতুন ডাটাবেস তৈরি করুন
3. একটি নতুন ইউজার তৈরি করুন
4. ইউজারকে ডাটাবেসে অ্যাসাইন করুন

### ধাপ ৪: Environment Variables সেট করুন
1. Cpanel → Software → Environment Variables
2. নিম্নলিখিত ভ্যারিয়েবলগুলি যোগ করুন:
   ```
   CPANEL=1
   SECRET_KEY=your_secret_key_here
   DATABASE_URL=mysql://username:password@localhost/database_name
   ```

### ধাপ ৫: Dependencies ইনস্টল করুন
1. Cpanel → Terminal
2. নিম্নলিখিত কমান্ডগুলি রান করুন:
   ```bash
   cd public_html
   pip3 install -r requirements_cpanel.txt
   ```

### ধাপ ৬: অ্যাপ্লিকেশন রিস্টার্ট করুন
1. Setup Python App এ যান
2. আপনার অ্যাপ্লিকেশন খুঁজুন
3. "Restart" বাটন ক্লিক করুন

### ধাপ ৭: অ্যাডমিন ইউজার তৈরি করুন
1. Terminal এ যান
2. নিম্নলিখিত কমান্ড রান করুন:
   ```bash
   python3 create_admin.py
   ```

## 🔧 সমস্যা সমাধান

### যদি অ্যাপ্লিকেশন লোড না হয়:
- Cpanel → Error Logs চেক করুন
- ফাইল পারমিশন সঠিক কিনা দেখুন (644 for files, 755 for folders)
- `passenger_wsgi.py` ফাইলটি সঠিক জায়গায় আছে কিনা দেখুন

### যদি ডাটাবেস এরর হয়:
- MySQL credentials সঠিক কিনা চেক করুন
- ডাটাবেস ইউজারকে সঠিক পারমিশন দেওয়া আছে কিনা দেখুন

### যদি স্ট্যাটিক ফাইল লোড না হয়:
- `.htaccess` ফাইলটি সঠিক জায়গায় আছে কিনা দেখুন
- `static/` ফোল্ডারের পারমিশন 755 কিনা দেখুন

## 📞 সহায়তা
- `cpanel_deploy/QUICK_DEPLOY.md` - দ্রুত গাইড
- `cpanel_deploy/CPANEL_CHECKLIST.md` - বিস্তারিত চেকলিস্ট
- `cpanel_deployment_guide.md` - সম্পূর্ণ গাইড

## 🎯 গুরুত্বপূর্ণ নোট
- প্রথমবার অ্যাপ্লিকেশন চালু করার সময় ডাটাবেস টেবিলগুলি অটোমেটিক তৈরি হবে
- নিয়মিত ব্যাকআপ নিন
- সিকিউরিটি আপডেট রাখুন
- Error logs নিয়মিত চেক করুন

## 🚀 সফল ডিপ্লয়ের পর
আপনার Academic Management System এখন Cpanel এ লাইভ! আপনি নিম্নলিখিত ফিচারগুলি ব্যবহার করতে পারবেন:

- ✅ ইউজার অথেনটিকেশন
- ✅ ক্লাস ম্যানেজমেন্ট
- ✅ রেজাল্ট ম্যানেজমেন্ট
- ✅ রুটিন ম্যানেজমেন্ট
- ✅ অ্যাটেনডেন্স ট্র্যাকিং
- ✅ অ্যাডমিন প্যানেল 