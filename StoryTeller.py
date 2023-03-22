import discord
import os
import dotenv
import StoryGen

bot = discord.Bot(intents = discord.Intents.all())

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.slash_command(name='tell_me', description='Tell me a story')
async def tell_me(ctx, character_1, character_2):

    await ctx.respond("Working on it...")
    ephemeral = True

    try:
        await ctx.send(ctx.author.mention + StoryGen.get_response("The story of " + character_1 + " fighting " + character_2))
    except Exception as e:
        await ctx.send('That Query was too long. Please try again.')
        print(e)
        print("Character 1: " + character_1, "Character 2: " + character_2)


dotenv.load_dotenv('StoryTeller/token.env')
bot.run(os.getenv('TOKEN_STORY'))
