from callsmusic.callsmusic import client as USER
from pyrogram import filters
from pyrogram.types import Chat, Message, User


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
  await USER.send_message(message.chat.id,"Merhabalar, Bu bir müzik asistanı hizmetidir @SesliMuzikBot .\n\n ❗️ Kurallar:\n   - Sohbete izin yok\n   -Spam yapılmasına izin verilmez \n\n 👉 **USERBOT GRUBUNUZA KATILAMAZSA GRUP DAVETİ BAĞLANTISINI VEYA KULLANICI ADINI GÖNDERİN.**\n\n - Bu kullanıcıyı gizli gruplara eklemeyin.\n ")
  return                        
