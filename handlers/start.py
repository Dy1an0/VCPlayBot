from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgEAAxkBAAEKBAdgqk47FtOSrcu0ZJgELdC-lxEZgAACCQEAAkXMSUZLDfnTEFCHeh8E")
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
\nBen grubunuzda sesli müzik çalmak için @lynx_zero tarafından sevgiyle yaratıldım  ❤
\nGrubunuza admin olarak ekleyin ve çalıştıramazsanız benimle iletişime geçin.
\nKomutlar ve bilgi için /help komutunu kullanın.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌍 Grubumuz", url="https://t.me/koruyucularailesi",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Benimle iletişim", url="https://t.me/lynx_zero"
                    )
                    
                ],
                [
                    InlineKeyboardButton(
                        "➕ Grubunuza eklemek için ➕", url="https://t.me/seslimuzikbot?startgroup=true"
                    ) 
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Bir YouTube videosu aramak ister misiniz?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Grup", url="https://t.me/koruyucularailesi"
                    )
                ],    
                [    
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
\n/play <song name> - istediğiniz şarkıyı çalır
/dplay <song name> - deezer ile istediğin şarkıyı çalır
/splay <song name> - jiosaavn ile istediğin şarkıyı çal
/playlist - Şimdi çalınan listeyi gösterir
/current - Şimdi çalınanı gösterir
/song <song name> -hızlıca istediğiniz şarkıları indirir
/search <query> -youtube'da ayrıntılı video arar
/deezer <song name> -deezer ile istediğiniz şarkıları hızlıca indirin
/saavn <song name> - saavn ile istediğiniz şarkıları hızlıca oynatır
/video <song name> - hızlıca istediğiniz videoları indirin
\n*Admin komutları*
/player - müzik çalar ayarları panelini aç
/pause - çalınan müziği durdurur
/resume - durdurulan müziği devam ettirir
/skip - müziği atlar
/end - müzik çalmayı durdur
/userbotjoin - asistanı sohbetinize davet eder(çalışmazsa asistanı manuel olarak ekleyin)
/admincache - Yönetici listesini yenile
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                InlineKeyboardButton(
                    "🔊 Grup", url="https://t.me/koruyucularailesi"
                )
            ], 
         )   
