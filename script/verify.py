#!/usr/bin/python

import sys
import discord

import logging
import json 

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


# load config
f = open('config.json')
config = json.load(f)

logger.info("Started verifier")

userid = sys.argv[1]
serverid = sys.argv[2]

logger.info(f"Verifying {userid} in {serverid}")
roleid = config["guild_settings"][str(serverid)]["role"]

intents = discord.Intents.default()
bot = discord.Client(intents=intents)

logger.info(f'Want to verify user {userid}')

@bot.event
async def on_ready():
	logger.info(f'We have logged in as {bot.user}')
	
	guild = await bot.fetch_guild(serverid);
	member = await guild.fetch_member(userid);
	role = guild.get_role(roleid);
	
	try:
		mail_chan = await bot.fetch_channel( config["guild_settings"][str(serverid)]["mail_channel"] )
	except:
		pass
	
	try:
		await member.add_roles(role);
	except BaseException as e:
		logger.critical(e);
		await mail_chan.send(content=f"Error: {client.user.mention} is unable to assign the role {role.mention} - check the role hierarchy?")
		raise (e);
	
	await member.send(f"You have been verified in server {guild}.")
	
	print(f"Hi {member}, welcome to {guild}! The bot has just given you the {role} role, allowing you to access the server 😊");
	
	try:
		await mail_chan.send(f"{member.mention} verified themselves.")
	except BaseException as e:
		logger.debug(e);
	
	await bot.close()

# don't want the script to persist when an error occurs...
@bot.event
async def on_error(e):
	logger.critical(f'Error - shutting down');
	print("AN ERROR OCCURED");
	await bot.close()
	
botkey = config["botkey"]
bot.run(botkey)