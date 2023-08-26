from telegraph import upload_file
from pyrogram import filters
from VipX import app


@app.on_message(filters.command('تلكراف'))
def ul(_, message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("🌹جاري استخراج رابط تلكراف انتظر قليلاً....🌹")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://telegra.ph" + x

        i.edit(f'رابط الصوره يا حيدي 🇾🇪🫡 👉 {url}')
