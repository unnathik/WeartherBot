import discord
import os
import requests

client = discord.Client()
my_secret = os.environ['TOKEN']
API_KEY = os.environ['API_KEY']

@client.event
async def on_ready():
  print("Bot is ready")

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  msg = message.content

  if msg.startswith('!start'):
    await message.channel.send('Hi there! I am WeartherBot. I can help you decide what to wear based on the weather outside. Just enter a city name to get started!')

  if msg.startswith('!wear'):
    city = msg.split("!wear ", 1)[1]
    url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + API_KEY
    data = requests.request('GET', url)

    if not data:
      await message.channel.send('Sorry! I am unable to find any data for ' + city + '. Would you like to try another location?')
    else:
      weather_data = data.json()
      celsius_temp = int(weather_data['main']['temp'] - 273.15)

      if celsius_temp <= 2:
        await message.channel.send("Make sure to grab a thick coat or a winter jacket and stay warm!")
      elif celsius_temp <= 9:
        await message.channel.send("It's freezing! Grab a coat on the way out.")
      elif celsius_temp <= 15:
        await message.channel.send("It's cold, but not that much. Do put on a pullover or sweater though!")
      elif celsius_temp <= 20:
        await message.channel.send("The weather is quite pleasant today! Grab a shrug or thin jacket just to be on the safe side.")
      elif celsius_temp <= 27:
        await message.channel.send("It's quite warm; a light t-shirt and jeans should do.")
      else: 
        await message.channel.send("Be prepared to sweat buckets if you step out; today is the day to pull out those shorts.")

client.run(my_secret)