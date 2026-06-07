import os
import json
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# ✅ তোমার সেট করা মেসেজগুলো এখানে পরিবর্তন করো
MESSAGE_1 = """✨ DKWin ✨
🎨 Color Trading Platform 🎨

━━━━━━━━━━━━━━━━━━━
💼 আমাদের সাথে কাজ করলে ইনশাল্লাহ ভালো প্রফিট করার সুযোগ পাবেন
━━━━━━━━━━━━━━━━━━━

🔗 Registration Link 👇
https://dkwin9.com/#/register?invitationCode=186731981267

━━━━━━━━━━━━━━━━━━━
📩 এটি একটি অটো রিপ্লাই সেট করা
🙏 অনুগ্রহ করে কেউ বিরক্ত হবেন না
━━━━━━━━━━━━━━━━━━━"""

MESSAGE_2 = """আরেকটু অপেক্ষা করো ভাই, শীঘ্রই রিপ্লাই দিচ্ছি! ⏳
জরুরি হলে এখানে বলো।"""

# কে কতবার মেসেজ দিয়েছে সেটা মনে রাখবে
user_message_count = {}

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    # গণনা বাড়াও
    if user_id not in user_message_count:
        user_message_count[user_id] = 0
    user_message_count[user_id] += 1
    
    count = user_message_count[user_id]
    
    print(f"User {user_id} sent message #{count}")
    
    if count == 1:
        # প্রথম মেসেজ
        await update.message.reply_text(MESSAGE_1)
    elif count == 2:
        # দ্বিতীয় মেসেজ
        await update.message.reply_text(MESSAGE_2)
    # তৃতীয় বার থেকে কোনো রিপ্লাই নেই (চাইলে আরো যোগ করতে পারো)

def main():
    token = os.environ.get("BOT_TOKEN")
    if not token:
        print("❌ BOT_TOKEN পাওয়া যায়নি!")
        return
    
    print("✅ Bot চালু হচ্ছে...")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("✅ Bot চালু! মেসেজের অপেক্ষায়...")
    app.run_polling()

if __name__ == "__main__":
    main()
