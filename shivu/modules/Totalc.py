from pymongo import ReturnDocument
import os
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext

from shivu import application, sudo_users, collection, db, CHARA_CHANNEL_ID, SUPPORT_CHAT



async def check_total_characters(update: Update, context: CallbackContext) -> None:
    try:
        total_characters = await collection.count_documents({})
        
        await update.message.reply_text(f"Total number of characters ln bot: {total_characters}")
    except Exception as e:
        await update.message.reply_text(f"Error occurred: {e}")



application.add_handler(CommandHandler("totalc", check_total_characters))
