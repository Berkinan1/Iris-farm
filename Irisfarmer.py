# meta developer: @Berki_modul
# бот сделан по угару
from .. import loader, utils
import asyncio

@loader.tds
class Iris_spamMod(loader.Module):
    """Модуль для фарма денежек монет в ирисе, спам в чате  
    чтобы он работал пожалуйста войдите в чат по ссылке: https://t.me/+WcHo3M2GDwYxYmMy"""
    strings = {"name": "iris_spam"}
    
    def __init__(self):
        self.running = False 

    async def irisgocmd(self, message):
        """Включить автоматическую отправку фарма """
        if self.running:
            await message.edit("<b>❎Процесс уже запущен!</b>")
            return

        self.running = True
        await message.edit("<b>✅Автоматическая отправка фарма запущена!</b>")

#вот тут выбираем в какой чат кидать, какое слово да
        while self.running:
            await message.client.send_message("https://t.me/+WcHo3M2GDwYxYmMy", "фарма ")
            await asyncio.sleep(14760)
    async def irisoffcmd(self, message):
        """Отключить автоматическую отправку фарма """
        if not self.running:
            await message.edit("<b>❎Процесс не запущен!</b>")
            return

        self.running = False
        await message.edit("<b>❎Автоматическая отправка фарма остановлена!</b>")
