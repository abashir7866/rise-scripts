@Ghost.command()
async def neko(ctx):
    neko = requests.get("https://nekos.life/api/v2/img/neko").json()["url"]
    await ctx.send(neko)