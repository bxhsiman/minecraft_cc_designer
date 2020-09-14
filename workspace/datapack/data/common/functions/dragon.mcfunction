execute as @e[type=minecraft:ender_dragon] at @s run attribute @s generic.max_health modifier add 100af772-b04b-49cb-948d-abb3cb0bc455 CC_dragon_health 0 multiply
execute as @e[type=minecraft:ender_dragon,tag=!CC_dragon_health] at @s run data modify entity @s Health set value 40000
tag @e[type=minecraft:ender_dragon] add CC_dragon_health
execute as @e[type=minecraft:ender_dragon] run attribute @s minecraft:generic.attack_damage modifier add 100af762-b04b-49cb-958d-abb3cb0bca45 CC_dragon_attack 0 multiply