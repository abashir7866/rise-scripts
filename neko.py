@Ghost.command()
async def neko(ctx):
    image = requests.get("https://nekos.life/api/v2/img/neko").json()["url"]
    await ctx.send(image)