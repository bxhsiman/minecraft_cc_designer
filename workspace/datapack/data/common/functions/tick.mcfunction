function common:clock
function common:info_show
function common:playercheck
execute as @a if score @s info matches 1.. run function common:setting
scoreboard players enable @a info
#亡灵类生物属性
#HP
execute as @e[type=#zombie] at @s run attribute @s generic.max_health modifier add 100af772-b04b-49cb-958d-abb3cb0bc415 CC_died_health 0.0 multiply
execute as @e[type=#skeleton] at @s run attribute @s generic.max_health modifier add 100af772-b04b-49cb-958d-abb3cb0bc415 CC_died_health 0.0 multiply
execute as @e[tag=!CC_died_health,type=#died] run data modify entity @s Health set value 20000
tag @e[type=#died] add CC_died_health
#ATK
execute as @e[type=#zombie] run attribute @s minecraft:generic.attack_damage modifier add 100af772-b04b-49cb-958d-abb3cb0bcd45 CC_died_attack 0.0 multiply
execute as @e[type=#skeleton] run attribute @s minecraft:generic.attack_damage modifier add 100af772-b04b-49cb-958d-abb3cb0bcd45 CC_died_attack 0.0 multiply

#小白属性
#ATK
replaceitem entity @e[type=minecraft:skeleton,tag=!CC_Skeleton_attack] weapon bow{Enchantments:[{id:"power",lvl:0}]}
tag @e[type=minecraft:skeleton] add CC_Skeleton_attack

#玩家攻击间隔加长 
execute as @a run attribute @s minecraft:generic.attack_speed base set 4

#敌对生命加强
execute as @e[type=#mob] at @s run attribute @s generic.max_health modifier add 100af772-b04b-49cb-958d-abb3cb0bc455 CC_mob_health 0.0 multiply
execute as @e[type=#mob] at @s run data modify entity @s Health set value 20000
tag @e[type=#mob] add CC_mob_health

#敌对攻击加强
execute as @e[type=#mob] run attribute @s minecraft:generic.attack_damage modifier add 100af762-b04b-49cb-958d-abb3cb0bcd45 CC_mob_attack 0.0 multiply

#敌对速度加强
execute as @e[type=#mob] run attribute @s minecraft:generic.movement_speed modifier add 100af772-b04b-49cb-958d-abb3cb0bdd54 CC_mob_speed 0.0 multiply
execute as @e[type=#zombie] run attribute @s minecraft:generic.movement_speed modifier add 100af772-b04b-49cb-958d-abb3cb0bdd54 CC_mob_speed 0.0 multiply
execute as @e[type=#skeleton] run attribute @s minecraft:generic.movement_speed modifier add 100af772-b04b-49cb-958d-abb3cb0bdd54 CC_mob_speed 0.0 multiply
execute as @e[type=creeper] run attribute @s minecraft:generic.movement_speed modifier add 100af772-b04b-49cb-958d-abb3cb0bdd54 CC_mob_speed 0.0 multiply

#玩家生命上限降低
execute as @a run attribute @s minecraft:generic.max_health base set 20

#苦力怕隐形，无声


#增加怪物侦查
execute as @e[type=#died] run attribute @s minecraft:generic.follow_range base set 64
execute as @e[type=#mob] run attribute @s minecraft:generic.follow_range base set 64
execute as @e[type=creeper] run attribute @s minecraft:generic.follow_range base set 64

#末影龙增强
execute as @a at @s if entity @e[type=ender_dragon] run function common:dragon

#凋零加强
execute as @a at @s if entity @e[type=wither] run function common:wither

#伤害降低to 0.7/挖掘疲劳


#检测玩家死亡
execute as @a if score @s death > @s deathF run tag @s add died
scoreboard players add @a[tag=died] deathF 1
clear @a[tag=died]
tag @a remove died

#无法入睡


#掉血失明
execute as @a if score @s HP matches ..0 run effect give @s minecraft:blindness 2 0 true

#生命限制


#蜘蛛强化


#毒水

#玩家减速
execute as @a run attribute @s minecraft:generic.movement_speed modifier add 100af762-b04b-49cb-958d-abb3cb0bcd45 player_speed -0.4 multiply

execute if entity @s[advancements={minecraft:end/kill_dragon=true}] run tag @a add win
execute if entity @s[advancements={minecraft:end/kill_dragon=true}] run function common:finish