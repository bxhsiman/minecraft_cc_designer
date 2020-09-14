title @a[tag=gameover] title {"text":"挑战失败","color":"red","bold":"true"}
title @a[tag=gameover] subtitle {"text":"复活次数用尽"}

title @a[tag=win] title {"text":"挑战成功","color":"green","bold":"true"}
title @a[tag=win] subtitle ["",{"text":"危机合约","color":"red"},{"score":{"name":"#dif","objective":"dif"},"bold":true,"color":"red"},{"text":"已完成","color":"red"}]
tellraw @a[tag=win] [{"text":"挑战成功！","bold":true,"color":"green"},{"text":"\n"},{"text":"危机合约 ","color":"red"},{"score":{"name":"#dif","objective":"dif"},"bold":true,"color":"red"},{"text":"\n"},{"text":"参与挑战的玩家数量:","color":"red"},{"score":{"name":"#playercheck","objective":"players"},"bold":true,"color":"aqua"}]
execute as @a run function common:cc
tellraw @a[tag=win] {"text":"感谢您的游玩！敬请期待我们的下一个作品！","color":"aqua"}
tellraw @a[tag=win] [{"text":"制作:","bold":true,"color":"white"},{"text":" 秋梨社","bold":true,"color":"gold","clickEvent":{"action":"open_url","value":"https://space.bilibili.com/308020237"},"hoverEvent":{"action":"show_text","contents":{"text":"点击打开官方B站账号"}}}]
