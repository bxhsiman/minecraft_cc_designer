execute as @e[type=minecraft:wither] at @s run attribute @s generic.max_health modifier add 100af772-b14b-49cb-948d-abb3cb0bc455 CC_wither_health 1 multiply
execute as @e[type=minecraft:wither,tag=!CC_wither_health] at @s run data modify entity @s Health set value 40000
tag @e[type=minecraft:wither] add CC_wither_health
execute as @e[type=minecraft:ender_wither] run attribute @s minecraft:generic.attack_damage modifier add 100af762-b04b-49cb-958d-abb3cb0bca95 CC_wither_attack 1.5 multiply