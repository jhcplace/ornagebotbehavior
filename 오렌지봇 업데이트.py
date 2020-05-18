# 유저 아이디: message.author.name
# 채널 이름: message.channel
# 서버 아이디: message.author.display_name

import time
import discord
from discord.ext import commands
import datetime
import asyncio
import random
import sys
import urllib
from urllib.request import Request
import bs4

token=("NjgwMzMzMzY0ODU4OTc4MzE0.XrtS9Q.ukSZ8d-zEptbDg9VwTzvM0Jmcrw")

check = ["오렌지봇"]

client = discord.Client()
print (client.guilds)
print (client.users)
print ("----------------------------")
print ("")
print ("잠시만 기다려 주세요...")
print ("")
print ("----------------------------")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.offline)
    print(client.user.id)
    print("ready")
    game = discord.Game("업데이트로 인해 일부 기능만 지원")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)

@client.event
async def on_message(message):

    # 봇 설명
    if message.content.startswith(".봇"):
        now = datetime.datetime.now()
        orangesendtime = str(now.year) + "년 " + str(now.month) + "월 " + str(now.day) + "일 | " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
        embed = discord.Embed(title=str(client.user.name) + " 정보", description= """봇 이름: 오렌지 봇 🍊
        봇 ID: 680333364858978314
        봇 생일: 2020년 2월 20일
        오렌지 봇 홈페이지: https://jhcplace.wixsite.com/orangebot
        오렌지봇 오픈소스: https://github.com/jhcplace/orangebot
        
        개발자: jhcpalce
        개발자 엔트리 마이페이지: https://playentry.org/jhcplece
        
        작성언어: python""", color=0x00ff00)
        embed.set_thumbnail(url="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2FVliqw%2FbtqCd1h9SOI%2FCzMfFsghAIdPfRkPzCKpak%2Fimg.png")
        embed.set_footer(text ="오렌지 봇" + " | " + (orangesendtime))
        await message.channel.send(embed=embed)
    
    if message.content.startswith("ㅊㅊ"):
        check.append(message.author.display_name)
        print(check)
        embed = discord.Embed(title="출석체크 시스템", description="출석체크가 완료되었습니다.", color=0x00ff00)
        embed.set_thumbnail(url="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2F9M6qG%2FbtqEdyejxb6%2Fp6cEiCqE8QERwOg5EhDTn1%2Fimg.png")
        await message.channel.send(embed=embed)

    if message.content.startswith("출석 리스트"):
        finalcheck = ""
        a = 0
        print (check)
        for a in check:
            print (a)
            finalcheck = finalcheck + """
            ```""" + (a) + "```"
        embed = discord.Embed(title="출석체크 시스템", description="""다음은 오늘 출석 체크한 유저의 이름입니다.
        {}""".format(finalcheck), color=0x00ff00)
        embed.set_thumbnail(url="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fk.kakaocdn.net%2Fdn%2F9M6qG%2FbtqEdyejxb6%2Fp6cEiCqE8QERwOg5EhDTn1%2Fimg.png")
        await message.channel.send(embed=embed)

client.run(token)