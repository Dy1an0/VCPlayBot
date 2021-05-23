from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only

@Client.on_message(filters.group & filters.command(["userbotjoin"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Önce beni grubunuzun yöneticisi olarak ekleyin</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "SesliMuzikBot"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id,"İstediğiniz gibi buraya katıldım")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>@SesliMusicRoBOt zaten sohbette</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 Flood Wait Error 🛑 \n Kullanıcı {user.first_name} userbot için yoğun katılım istekleri nedeniyle grubunuza katılamadı! Kullanıcının grupta yasaklanmadığından emin olun."
            "\n\nVeya @SesliMuzikRoBot'u Grubunuza manuel olarak ekleyin ve tekrar deneyin</b>",
        )
        return
    await message.reply_text(
            "<b>@SesliMusicRoBot grubunuza bağlandı</b>",
        )
    
@USER.on_message(filters.group & filters.command(["userbotleave"]))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:  
        await message.reply_text(
            f"<b>Kullanıcı grubunuzdan ayrılamadı!."
            "\n\n beni Grubunuzdan elle atabilirsiniz</b>",
        )
        return
