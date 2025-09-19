import discord
import random
import asyncio

# -------- LISTAS DE CONTENIDO -------- #
tips = [
    "💡 Apaga las luces que no uses 🌍 → Esto ayuda a reducir el consumo de electricidad, lo que a su vez disminuye la quema de combustibles fósiles en plantas de energía. ¡Menos emisiones de CO₂ significan un planeta más sano!",
    "♻️ Recicla botellas de plástico → Al reciclar, evitamos que millones de toneladas de plástico terminen en vertederos u océanos. Además, el plástico reciclado puede transformarse en ropa, envases o incluso muebles.",
    "🚍 Usa transporte público → Compartir un autobús equivale a sacar muchos autos de circulación. Esto reduce el tráfico, las emisiones y la contaminación sonora, mientras ahorras dinero y tiempo.",
    "🚿 No desperdicies agua → El agua dulce es un recurso limitado. Cada gota que ahorras ayuda a preservar ríos, lagos y acuíferos que son esenciales para la vida en el planeta.",
    "🌳 Planta un árbol hoy → Los árboles absorben CO₂, producen oxígeno, ofrecen sombra y refugio para los animales. Un solo árbol puede dar oxígeno suficiente para 4 personas al día.",
    "🛍️ Lleva tu propia bolsa de tela → Las bolsas de plástico de un solo uso tardan cientos de años en degradarse. Usar tela reduce desechos y promueve un consumo más consciente.",
    "🐄➡🌱 Reduce el consumo de carne → La ganadería intensiva genera metano, un gas de efecto invernadero muy potente. Reducir la carne, aunque sea un día a la semana, tiene un gran impacto positivo.",
    "🥤♻️ Reutiliza envases → Cada vez que reutilizas un envase, evitas producir otro nuevo que requiere energía y recursos. Es una de las maneras más fáciles de cuidar al planeta desde casa.",
    "🔌 Desconecta cargadores que no uses → Aunque no lo notes, los cargadores consumen energía en ‘modo fantasma’. Desconectarlos reduce tu factura eléctrica y cuida los recursos naturales.",
    "🍅🥦 Prefiere productos locales → Comprar local significa menos transporte, menos emisiones de CO₂ y un impulso directo a la economía de tu comunidad."
]

frases_motivacionales = [
    "🌟 ¡Tú puedes hacer la diferencia todos los días! Cada acción, por pequeña que parezca, suma en el cuidado del planeta.",
    "💚 Cada acción cuenta, no importa lo pequeña que sea. Incluso apagar una luz puede ayudar más de lo que crees.",
    "🌍 El futuro depende de lo que hagamos hoy. Si sembramos conciencia ahora, cosecharemos un mañana mejor.",
    "✨ Ser eco-friendly también es cool, ¡inténtalo y verás que contagias a otros con tu ejemplo positivo!"
]

# -------- FRASES DEL ENGINEER (TF2) -------- #
frases_engineer = [
    "Erectin' a dispenser!",
    "Sentry going up!",
    "Spy sapping my sentry!",
    "Need a dispenser here!",
    "I'm moving this.",
    "Nope.",
    "Y'all gotta stop them!",
    "Much obliged, pardner.",
    "Teleporter coming right up!",
    "Dispenser goin' up!",
    "Sentry down!",
    "Dagnabbit!",
    "That there wasn’t gettin’ any lighter."
]

# -------- CONFIGURACIÓN DEL BOT -------- #
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# -------- EVENTOS -------- #
@client.event
async def on_ready():
    print(f'Bot conectado como {client.user}')
    await client.change_presence(activity=discord.Game("🌱 Cuidando el planeta"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    contenido = message.content.lower()

    # -------- COMANDOS PRINCIPALES -------- #
    if contenido.startswith("!eco"):
        await message.channel.send(random.choice(tips))

    elif contenido.startswith("!motivame"):
        await message.channel.send(random.choice(frases_motivacionales))

    elif contenido.startswith("!ayuda"):
        ayuda = (
            "**🌍 Lista de comandos:**\n"
            "`!eco` → Recibir un tip ecológico con explicación\n"
            "`!motivame` → Mensaje motivacional 🌟\n"
            "`!ayuda` → Mostrar este menú 📜\n"
            "`!dado` → Tirar un dado 🎲\n"
            "`!secreto` → Comando oculto 👀\n"
        )
        await message.channel.send(ayuda)

    elif contenido.startswith("!dado"):
        numero = random.randint(1, 6)
        await message.channel.send(f"🎲 El dado cayó en **{numero}**")

    # -------- COMANDOS SECRETOS -------- #
    elif "putispencerhere" in contenido:
        await message.channel.send(random.choice(frases_engineer))

    elif contenido.startswith("!secreto"):
        await message.channel.send("shhhhh...")

    # -------- MINI-EVENTO ALEATORIO -------- #
    if random.random() < 0.01:  # 1% de probabilidad en cada mensaje
        await message.channel.send("🌟 Recuerda: cada acción ecológica cuenta 💚")


# -------- INICIO DEL BOT -------- #
client.run("MTQxNjIxNTI3MTA0NzMwMzI0Mg.GwYcir.Dl6PRpf7RYUS_MRVm8kD0rWlkFxcf2kuUCgH1Y")
