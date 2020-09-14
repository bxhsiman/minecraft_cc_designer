execute as @a if score @s info matches 1 run tellraw @s ["",{"text":"危 机 合 约 ","bold":true,"color":"red","clickEvent":{"action":"run_command","value":"/function common:cc"},"hoverEvent":{"action":"show_text","contents":{"text":"点击查看详细合约信息","color":"aqua"}}},{"score":{"name":"#dif","objective":"dif"},"bold":true,"color":"red","clickEvent":{"action":"run_command","value":"/function common:cc"},"hoverEvent":{"action":"show_text","contents":{"text":"点击查看详细合约信息","color":"aqua"}}}]

#固定内容
execute as @a if score @s info matches 1 run tellraw @s [{"text":"当前挑战时间:"},{"score":{"name":"#clock","objective":"hour_1"},"color":"green"},{"score":{"name":"#clock","objective":"hour"},"color":"green"},{"text":":","color":"green"},{"score":{"name":"#clock","objective":"min_1"},"color":"green"},{"score":{"name":"#clock","objective":"min"},"color":"green"},{"text":":","color":"green"},{"score":{"name":"#clock","objective":"sec_1"},"color":"green"},{"score":{"name":"#clock","objective":"sec"},"color":"green"}]

execute as @a if score @s info matches 1 run tellraw @s [{"text":"制作:","bold":true,"color":"white"},{"text":" 秋梨社","bold":true,"color":"gold","clickEvent":{"action":"open_url","value":"https://space.bilibili.com/308020237"},"hoverEvent":{"action":"show_text","contents":{"text":"点击打开官方B站账号"}}}]

execute as @a if score @s info matches 2 run tag @s add info_
scoreboard players set @a info 0
