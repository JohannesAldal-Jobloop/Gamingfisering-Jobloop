import discord
import json
from discord.ext import commands
from discord import app_commands

class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}.')

        try: 
            guild = discord.Object(id=1460909088522371266)
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} commands to guild {guild.id}')
        except Exception as e:
            print(f'Error syncing commands: {e}')


    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.startswith('hello'):
            await message.channel.send(f'Hi there {message.author}')



intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents=intents)

GUILD_ID = discord.Object(id=1460909088522371266)

with open("secrets.json") as f:
    secrets = json.load(f)
    print()

@client.tree.command(name="hallo", description="Say hello", guild=GUILD_ID)
async def sayHello(interaction: discord.Interaction):
    await interaction.response.send_message("Hi there.")

@client.tree.command(name="din_profil", description="Din oppmøte og framgang på Digitale Talenter", guild=GUILD_ID)
async def visEmbed(interaction: discord.Interaction, privat: bool):
    embed = discord.Embed(
        title=f"{interaction.user.display_name} sin profil på Digitale Talenter", 
        #url="https://www.youtube.com/watch?v=KHQ2MaDbx5I&list=PL-7Dfw57ZZVQ-GCNQS4Kyz637Fffhb0Hs&index=7", 
        description="Din framgang på DT",
        color=discord.Color.purple()
        )
    embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar)
    embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.webfx.com%2Fwp-content%2Fuploads%2F2021%2F10%2Fgeneric-image-placeholder.png&f=1&nofb=1&ipt=7a9a556c9a9fb1a83d6d420408365ee88b4c359380329e1db9363386b4287c57")
    embed.add_field(name="Oppmøte", value="⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜", inline=False)
    embed.add_field(name="Sosial", value="⬛⬛⬛⬜⬜⬜⬜⬜⬜⬜")
    embed.add_field(name="Inlevering", value="⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜")
    embed.set_image(url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.webfx.com%2Fwp-content%2Fuploads%2F2021%2F10%2Fgeneric-image-placeholder.png&f=1&nofb=1&ipt=7a9a556c9a9fb1a83d6d420408365ee88b4c359380329e1db9363386b4287c57")
    embed.set_footer(text=f"footer")

    await interaction.response.send_message(embed=embed, ephemeral=privat)

client.run(secrets["dicordbottoken"])