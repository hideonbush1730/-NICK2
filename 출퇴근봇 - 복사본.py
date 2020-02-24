import discord
import openpyxl
import random
import asyncio
import os
token=os.environ["TOKEN"]

client = discord.Client()

@client.event
async def on_ready():
    print("ready")
    print(client.user.id)
    print(client.user.name)
    print('=====================================')
    print('벤츠봇 베타')
    print('저작권 siri#2409')
    print('벤츠서버에 기증한봇입니다')
    print('=====================================')


@client.event
async def on_message(message):
    if message.content.startswith('$공지'):
        if message.author.id == 581396513108918295 or message.author.id == 388585033029517323:
            for i in message.guild.members:
                if i.bot == True:
                    pass
                else:
                    await i.send(message.content[4:])

    if message.content == '!출근':
        if message.author.id ==388585033029517323 or message.author.id == 581396513108918295:
            await message.channel.send('@everyone')
            embed=discord.Embed(title='정상 출근처리되셧습니다', color=0xff00, timestamp=message.created_at)
            embed.add_field(name="출.퇴근 알림", value=f'{message.author} 님이 출근하셧습니다.즐거운하루되세요!', inline=True)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)
        else:
            await message.channel.send('❌ 이런 존재하지않는 명령어또는 권한이없어요!')
    if message.content == '!퇴근':
        if message.author.id ==388585033029517323 or message.author.id == 581396513108918295:
            await message.channel.send('@everyone')
            embed=discord.Embed(title='정상 퇴근처리 되셧습니다', color=0xff00, timestamp=message.created_at)
            embed.add_field(name="출.퇴근 알림", value=f'{message.author} 님이 퇴근하셧습니다.수고하셧습니다!.', inline=True)
            embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await message.channel.send(embed=embed)
        else:
            await message.channel.send('❌ 이런 존재하지않는 명령어또는 권한이없어요!')

    if message.content == '!NICk 명령어':
        embed=discord.Embed(title='📗NICK 명령어📗', color=0x00ff56)
        embed.set_author(name='NICK')
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/678483814346915841/681376813741506587/123456.jpg')
        embed.add_field(name='!NICK 출근/퇴근.', value='자동출퇴근 이됩니다', inline=True)
        embed.add_field(name='!&공지.', value='유저들에게 개인디엠을 보낼수있습니다 예)&공지 내용', inline=True)
        embed.set_footer(text='이글은 NICK SHOP 봇입니다')
        await message.channel.send(embed=embed)
 
async def my_background_task():
    await client.wait_until_ready()
    while not client.is_closed():
        game = discord.Game("문의siri#2409")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(5)
        game = discord.Game(f'{len(client.guilds)}개의 서버에 참여중')
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(5)
        game = discord.Game(f'{len(client.users)}명의 유저들과 소통하는중')
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(5)

client.loop.create_task(my_background_task())

client.run(token) 
