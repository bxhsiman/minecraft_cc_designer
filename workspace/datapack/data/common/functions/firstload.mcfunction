scoreboard objectives add players dummy "历史登录玩家"
scoreboard objectives add dif dummy "难度"
scoreboard players set #dif dif 2
scoreboard objectives add sec dummy
scoreboard objectives add sec_1 dummy
scoreboard objectives add min dummy
scoreboard objectives add min_1 dummy
scoreboard objectives add hour dummy
scoreboard objectives add hour_1 dummy
scoreboard objectives add death deathCount
scoreboard objectives add info trigger
scoreboard objectives add deathF dummy
scoreboard objectives add HP health
scoreboard players set #clock sec_1 0
scoreboard players set #clock min 0
scoreboard players set #clock min_1 0
scoreboard players set #clock hour 0
scoreboard players set #clock hour_1 0
gamerule sendCommandFeedback false
scoreboard objectives add clock dummy
#若选择永夜则删除此句
time set day

#永夜
time set day
gamerule doDaylightCycle true

#若不选择雷阵雨则删除这句和clock.mcfunction


#难度选择（极限模式请调为hard）
difficulty easy

#不回血
gamerule naturalRegeneration true
#死亡不掉落
gamerule keepInventory true