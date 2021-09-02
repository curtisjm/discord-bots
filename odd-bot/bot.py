import discord
import os
from dotenv import load_dotenv

load_dotenv()
client = discord.Client()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):

    msg = message.content

    if message.author == client.user:
        return

    if msg.startswith("$eoo"):
        args = msg.split(" ")
        if len(args) < 3:
            await message.channel.send("You must give me two numbers...")
            return
        try:
            low = int(args[1])
            high = int(args[2])
            if low > 500 or high > 500:
                await message.channel.send("Please keep your numbers below 500.")
                return
        except:
            await message.channel.send("You can only give me valid integers...")
            return

        if low > high:
            low, high = high, low
        if low % 2 == 0:
            low += 1

        nums = gen_eoo(low, high)
        await message.channel.send(
            "EOO numbers between " + str(low) + " & " + str(high) + ":    " + nums
        )


def gen_eoo(low, high):
    nums = ""
    for i in range(low, high + 1, 4):
        nums += str(i) + ", "
    nums = nums.strip()
    nums = nums.rstrip(",")
    return nums


client.run(os.getenv("TOKEN"))
