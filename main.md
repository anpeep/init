## Main.py

Laadime meie tehtud .env failist tokeni.
```
from dotenv import dotenv_values
```
__Intents__ on need "load", mille ise andsime botile Discordi API (kliendi ja serveri vahelise suhtluse haldaja) kaudu.
__Message__ annab botile "loa" ka ise sõnumeid saata ning __commands__ abil saab bot reageerida käskudele.

```
from discord import Intents, Message  
from discord.ext import commands  
```

Otsime .env lõpuga faili.

```config = dotenv_values(".env")```

Botil on "luba" teada, kui keegi serveriga liitus, saata emojisid, võtta vastu kutseid, panna reaktsioone sõnumitele jne.

```intents = Intents.default()  ```

Et bot tohiks lugeda, mida kasutajad kirjutasid.

```intents.message_content = True  ```

Sellega loome boti, ütleme et käsud algavad hüüumärgiga (tohib muuta) ning anname ka kõik meie Developer Portali load.

```client = commands.Bot(command_prefix="!", intents=intents)  ```

client.event muidu tähendab, et järgnev meetod käivitatakse iga kord, kui keegi kanalisse kirjutab, kuid kuna __on_ready__ 
meetod on seest tühi, siis käivitatakse see vaid 1 kord, boti käivitusel.
```
@client.event  
async def on_ready():  
    print(f"{client.user} is now running!")  
```
Järgnev meetod käivitatakse iga kord, kui keegi midagi Discordi kirjutab.
```
@client.event  
async def on_message(message: Message):  
    # Ilma selleta !help kirjutades tuleks ka sõnum on_message, millel on tühi väärtus
    if message.author == client.user:  
        return  
```    
Kas sõnum algas hüüumärgiga? sellisel juhul reageeri.
```
    if message.content.startswith("!"):  
        await client.process_commands(message)  
        return  
```
Boti käivitamiseks.

```def main():  ```

Võtame ainult "TOKEN" väärtuse.
```
    token = config.get("TOKEN")  
    if token is None:  
        raise ValueError("loo fail nimega .env ja pane sinna BOT_TOKEN=isiklik Discord Developer Portal token")  
    client.run(token)  
if __name__ == "__main__":  
    main()
```