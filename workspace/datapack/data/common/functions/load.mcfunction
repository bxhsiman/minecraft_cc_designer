scoreboard objectives add ifload dummy
scoreboard players add #ifload ifload 1
tellraw @a {"text":"awa"}
execute if score #ifload ifload matches 1 run function common:firstload
