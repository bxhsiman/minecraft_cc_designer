execute as @a[tag=info] run title @s actionbar [{"text":"当前挑战时间:"},{"score":{"name":"#clock","objective":"hour_1"},"color":"green"},{"score":{"name":"#clock","objective":"hour"},"color":"green"},{"text":":","color":"green"},{"score":{"name":"#clock","objective":"min_1"},"color":"green"},{"score":{"name":"#clock","objective":"min"},"color":"green"},{"text":":","color":"green"},{"score":{"name":"#clock","objective":"sec_1"},"color":"green"},{"score":{"name":"#clock","objective":"sec"},"color":"green"}]
execute as @a[tag=info_,tag=!info] run function common:addinfo
execute as @a[tag=info_,tag=info] run function common:removeinfo
execute as @a[tag=info_] run tag @s remove info_
