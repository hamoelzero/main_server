from discord_webhook import DiscordWebhook, DiscordEmbed
import json
import time

def sender(deal):
    issued_number=deal["issued_number"]
    item_name=deal["item_name"]
    differ=deal["differ"]
    differ_percent=deal["differ_percent"]
    old_price=deal["old_price"]
    new_price=deal["new_price"]
    rarity_id=deal["rarity_id"]
    img=deal["img"]
    buy_link=deal["buy_link"]
    check_button_url=deal["check_button_url"]
    total_items=deal["total_items"]
    color=deal["color"]


    webhook  = DiscordWebhook(url="https://discord.com/api/webhooks/1190604795996811395/FARFsOassdixyYbvwFjcVLljNAUaWLw83F3jC_WstyGdRsAd25INU46nORUxcSuDTpyD")
    embed = DiscordEmbed(title=f"**__#{issued_number}__**   **{item_name}**      **<t:{int(time.time())}:R>** ",description=f"☆                     [BUYNOW]({buy_link})                                    ☆                     [CHECK]({check_button_url})                     ☆")
    embed.add_embed_field( name="Old Price",value=f">      **~~${round(old_price,2)}~~**",inline=True,)
    embed.add_embed_field( name="☆               New Price                  ☆        Decreased By",value=f"☆              **${round(new_price,2)}**                                    ☆                      **${round(differ,1)}** / %{round(differ_percent,1)}",inline=True)
    embed.add_embed_field( name="☆               Rarity",value=f"☆               **<@&{rarity_id}>**",inline=True)
    embed.set_thumbnail(url=img)
    embed.set_footer(text="Embed Footer Text", icon_url="URL of icon")
    embed.set_footer( icon_url=
                        "https://media.discordapp.net/attachments/1008571147853504612/1086812999379066970/HOSSAM_explosive_man_with_TNT_c351f524-8b63-466b-8346-816037c0ff80.png?width=513&height=513",
                        text=
                        f"Hossam Omar | TNT                                   Total Supply: [{total_items}]")


    webhook.add_embed(embed)

    response = webhook.execute()
