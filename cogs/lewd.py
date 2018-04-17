import os
import random
import discord
from discord.ext import commands
from cogs.utils.dataIO import dataIO
from .utils.dataIO import fileIO
from random import choice as randchoice
from .utils.chat_formatting import italics


class Lewd:
    def __init__(self, bot):
        self.bot = bot
        self.cuddles = fileIO("data/lewd/cuddles.json","load")
        self.hold_self = fileIO("data/lewd/hand/self.json","load")
        self.hold_person = fileIO("data/lewd/hand/person.json","load")
        self.hold_nothing = fileIO("data/lewd/hand/nothing.json","load")

    @commands.command(pass_context=True, no_pm=False)
    async def handhold(self, ctx, user : discord.Member=None):
        """Hold another users hand."""
        msg = ' '
        if user != None:
            if user.id == self.bot.user.id:
                user = ctx.message.author
                msg = " You try to hold the bots hand, only then you realise computers don't have hands."
                await self.bot.say(user.display_name + msg)
            elif user.id == ctx.message.author.id:
                await self.bot.say(randchoice(self.hold_self).format(victim=user.display_name, holder=ctx.message.author.display_name))
            else:
                await self.bot.say(randchoice(self.hold_person).format(victim=user.display_name, holder=ctx.message.author.display_name))
        elif user is None:
            await self.bot.say("You try to cuddle with air.")
        else:
            await self.bot.say(randchoice(self.hold_person).format(victim=user.display_name, holder=ctx.message.author.display_name))

    @commands.command(pass_context=True, no_pm=False)
    async def cuddle(self, ctx, user : discord.Member=None):
        """Cuddles the user. Messages brought to you by @Mandelora#1108"""
        msg = ' '
        if user != None:
            if user.id == self.bot.user.id:
                user = ctx.message.author
                msg = " You try to cuddle the bot but end up hugging a metal box."
                await self.bot.say(user.mention + msg)
            else:
                await self.bot.say(randchoice(self.cuddles).format(victim=user.display_name, cuddler=ctx.message.author.display_name))
        elif user is None:
            await self.bot.say("You try to cuddle with air.")
        else:
            await self.bot.say(randchoice(self.cuddles).format(victim=user.display_name, cuddler=ctx.message.author.display_name))
        

    @commands.command(no_pm=True, hidden=True)
    async def hug(self, user : discord.Member, intensity : int=1):
        """Because everyone likes hugs

        Up to 10 intensity levels."""
        name = italics(user.display_name)
        if intensity <= 0:
            msg = "(っ˘̩╭╮˘̩)っ" + name
        elif intensity <= 3:
            msg = "(っ´▽｀)っ" + name
        elif intensity <= 6:
            msg = "╰(*´︶`*)╯" + name
        elif intensity <= 9:
            msg = "(つ≧▽≦)つ" + name
        elif intensity >= 10:
            msg = "(づ￣ ³￣)づ{} ⊂(´・ω・｀⊂)".format(name)
        await self.bot.say(msg)

def checks():
    if not os.path.exists('data/lewd'):
        print('Creating data/lewd folder...')
        os.makedirs('data/lewd')
    if not dataIO.is_valid_json('data/lewd/cuddles.json'):
        print('Creating data/lewd/cuddles.json...')
        dataIO.save_json('data/lewd/cuddles.json', {})
    if not os.path.exists('data/lewd/hand'):
        print('Creating data/lewd/hand folder...')
    if not dataIO.is_valid_json('data/lewd/hand/person.json'):
        print('Creating default person.json...')
        dataIO.save_json('data/lewd/hand/person.json', {})
    if not dataIO.is_valid_json('data/lewd/hand/self.json'):
        print('Creating default self.json...')
        dataIO.save_json('data/lewd/hand/self.json', {})
    if not dataIO.is_valid_json('data/lewd/hand/nothing.json'):
        print('Creating default nothing.json...')
        dataIO.save_json('data/lewd/hand/nothing.json', {})

def setup(bot):
    checks()
    bot.add_cog(Lewd(bot))