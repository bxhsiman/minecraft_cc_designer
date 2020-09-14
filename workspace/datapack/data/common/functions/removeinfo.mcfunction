execute as @a[tag=info_,tag=info] run tag @s remove info
execute as @a[tag=info_,tag=!info] run tellraw @s {"text":"挑战时长隐藏"}
execute as @a[tag=info_] run tag @s remove info_