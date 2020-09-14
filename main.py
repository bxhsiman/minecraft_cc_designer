# encoding: utf-8
from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_CCofMinecraft
import os
import json
import ast
import time
import shutil
import zipfile
import sys
'''
此处为初始化区域
'''
#注意工作目录！
cvcc = []
mpcc = []
path = os.getcwd()

with open(path+'\cvccdic.json','r') as a:
    cvccdic = json.loads(a.read())
with open(path+'\mpccdic.json','r') as a:
    mpccdic = json.loads(a.read())

with open(path+'\muti_mpccdic.json','r') as a:
    muti_mpccdic = json.loads(a.read())


class mywindow(QtWidgets.QMainWindow, Ui_CCofMinecraft):
    

    def  __init__ (self):
        super(mywindow, self).__init__()
        self.setupUi(self)
        
    
        '''
        此处进行按钮功能链接
        '''
        #说明：1* 2* 3* 为不同合约条目 *1 *2 *3为三档不同等级 *9为删除本条约全部内容
        self.radio_allhp_1.clicked.connect(lambda:self.insertcc(11))
        self.radio_allhp_2.clicked.connect(lambda:self.insertcc(12))
        self.radio_allhp_3.clicked.connect(lambda:self.insertcc(13))
        self.button_allatk.clicked.connect(lambda:self.insertcc(19))
        
        self.radio_allatk_1.clicked.connect(lambda:self.insertcc(21))
        self.radio_allatk_2.clicked.connect(lambda:self.insertcc(22))
        self.radio_allatk_3.clicked.connect(lambda:self.insertcc(23))
        self.button_allatk_2.clicked.connect(lambda:self.insertcc(29))
        
        self.radio_allspeed_1.clicked.connect(lambda:self.insertcc(31))
        self.radio_allspeed_2.clicked.connect(lambda:self.insertcc(32))
        self.radio_allspeed_3.clicked.connect(lambda:self.insertcc(33))
        self.button_allspeed.clicked.connect(lambda:self.insertcc(39))
        
        self.radio_allspeed_4.clicked.connect(lambda:self.insertcc(41))
        self.radio_allspeed_5.clicked.connect(lambda:self.insertcc(43))
        self.radio_allspeed_6.clicked.connect(lambda:self.insertcc(46))
        self.button_allspeed_2.clicked.connect(lambda:self.insertcc(49))

        self.radio_allspeed_7.clicked.connect(lambda:self.insertcc(51))
        self.radio_allspeed_8.clicked.connect(lambda:self.insertcc(52))
        self.radio_allweakness_4.clicked.connect(lambda:self.insertcc(54))
        self.button_allspeed_3.clicked.connect(lambda:self.insertcc(59))

        self.radioButton.clicked.connect(lambda:self.insertcc(65))
        #self.radio_allspeed_11.clicked.connect(lambda:self.insertcc(62))
        #self.radio_allspeed_12.clicked.connect(lambda:self.insertcc(63))
        self.battle_cancle.clicked.connect(lambda:self.insertcc(69))

        self.radio_allspeed_9.clicked.connect(lambda:self.insertcc(71))
        
        self.radio_allspeed_10.clicked.connect(lambda:self.insertcc(73))
        self.radio_allspeed_11.clicked.connect(lambda:self.insertcc(75))
        self.button_allspeed_4.clicked.connect(lambda:self.insertcc(79))
        
        self.radio_allspeed_12.clicked.connect(lambda:self.insertcc(82))
        #self.radio_allspeed_13.clicked.connect(lambda:self.insertcc(82))
        #self.button_allspeed.clicked.connect(lambda:self.insertcc(83))
        self.button_allspeed_5.clicked.connect(lambda:self.insertcc(89))
        
        self.radio_allspeed_16.clicked.connect(lambda:self.insertcc(91))
        #self.radio_allspeed_17.clicked.connect(lambda:self.insertcc(92))
        #self.radio_allspeed_18.clicked.connect(lambda:self.insertcc(93))
        self.button_allspeed_7.clicked.connect(lambda:self.insertcc(99))

        self.radio_allspeed_19.clicked.connect(lambda:self.insertcc(101))
        self.radio_allspeed_20.clicked.connect(lambda:self.insertcc(102))
        self.radio_allspeed_21.clicked.connect(lambda:self.insertcc(103))
        self.button_allspeed_8.clicked.connect(lambda:self.insertcc(109))

        
        #self.radio_allspeed_22.clicked.connect(lambda:self.insertcc(111))
        #self.radio_allspeed_23.clicked.connect(lambda:self.insertcc(112))
        #self.radio_allspeed_24.clicked.connect(lambda:self.insertcc(113))
        #self.button_allspeed_9.clicked.connect(lambda:self.insertcc(119))

        self.radioButton_cantsleep.clicked.connect(lambda:self.insertcc(121))
        #self..clicked.connect(lambda:self.insertcc(122))
        #self..clicked.connect(lambda:self.insertcc(123))
        self.button_cantsleepcancle.clicked.connect(lambda:self.insertcc(129))
        
        
        self.radio_itemmakeuneasy.clicked.connect(lambda:self.insertcc(132))
        #self..clicked.connect(lambda:self.insertcc(132))
        #self..clicked.connect(lambda:self.insertcc(133))
        self.button_itemmakeuneasycancle.clicked.connect(lambda:self.insertcc(139))

       
        

        
        self.radio_allspeed_25.clicked.connect(lambda:self.insertcc(140))
        self.radio_allspeed_26.clicked.connect(lambda:self.insertcc(141))
        self.radio_allspeed_27.clicked.connect(lambda:self.insertcc(142))
        self.button_allspeed_10.clicked.connect(lambda:self.insertcc(149))

        self.radio_allspeed_28.clicked.connect(lambda:self.insertcc(151))
        self.radio_allspeed_29.clicked.connect(lambda:self.insertcc(152))
        #self.radio_allspeed_30.clicked.connect(lambda:self.insertcc(153))
        self.button_allspeed_11.clicked.connect(lambda:self.insertcc(159))


        self.radio_allspeed_31.clicked.connect(lambda:self.insertcc(161))
        self.radio_allspeed_32.clicked.connect(lambda:self.insertcc(162))
        self.radio_allspeed_33.clicked.connect(lambda:self.insertcc(163))
        self.radio_blind_5.clicked.connect(lambda:self.insertcc(165))
        self.button_allspeed_12.clicked.connect(lambda:self.insertcc(169))


        self.radioButton_allrain.clicked.connect(lambda:self.insertcc(172))
        #self..clicked.connect(lambda:self.insertcc(172))
        #self..clicked.connect(lambda:self.insertcc(173))
        self.button_allraincancle.clicked.connect(lambda:self.insertcc(179))


        self.radio_allspeed_34.clicked.connect(lambda:self.insertcc(181))
        self.radio_allspeed_35.clicked.connect(lambda:self.insertcc(182))
        self.radio_allspeed_36.clicked.connect(lambda:self.insertcc(183))
        self.button_allspeed_13.clicked.connect(lambda:self.insertcc(189))

        self.radio_allspeed_37.clicked.connect(lambda:self.insertcc(191))
        self.radio_allspeed_38.clicked.connect(lambda:self.insertcc(192))
        #self..clicked.connect(lambda:self.insertcc(193))
        self.button_allspeed_14.clicked.connect(lambda:self.insertcc(199))

        self.radio_allspeed_39.clicked.connect(lambda:self.insertcc(201))
        self.radio_allspeed_40.clicked.connect(lambda:self.insertcc(202))
        self.radio_allspeed_41.clicked.connect(lambda:self.insertcc(203))
        self.button_allspeed_15.clicked.connect(lambda:self.insertcc(209))

        self.radio_cantinwater.clicked.connect(lambda:self.insertcc(211))
        #self..clicked.connect(lambda:self.insertcc(212))
        #self..clicked.connect(lambda:self.insertcc(213))
        self.button_cantinwatercancle.clicked.connect(lambda:self.insertcc(219))

        #self.radio_allspeed_42.clicked.connect(lambda:self.insertcc(221))
        #self.radio_allspeed_43.clicked.connect(lambda:self.insertcc(222))
        #self..clicked.connect(lambda:self.insertcc(223))
        #self.button_allspeed_16.clicked.connect(lambda:self.insertcc(229))

        #self..clicked.connect(lambda:self.insertcc(231))
        self.radio_diedimprove_2.clicked.connect(lambda:self.insertcc(232))
        self.radio_diedimprove_3.clicked.connect(lambda:self.insertcc(233))
        self.button_diedimprovecancle.clicked.connect(lambda:self.insertcc(239))
        
        #self.radio_boomquick_1.clicked.connect(lambda:self.insertcc(241))
        #self.radio_boomquick_2.clicked.connect(lambda:self.insertcc(242))
        #self.radio_boomkuick.clicked.connect(lambda:self.insertcc(243))
        #self.button_boomquickcancle.clicked.connect(lambda:self.insertcc(249))

        #倍率合约
        self.checkBox.clicked.connect(lambda:self.insertcc(1000))
        self.checkBox_2.clicked.connect(lambda:self.insertcc(1010))
        self.checkBox_3.clicked.connect(lambda:self.insertcc(1020))
        
        #生成
        self.pushButton.clicked.connect(lambda:self.write())
        
       
        

        
        
    
    '''
    面板逻辑区
    '''
   
    #按钮与内容链接

    #def reset(self):#合约重置模块
    #    cvcc = []#常规合约表
    #    mpcc = []#倍率合约表
    

    #合约的加入与删除模块
    def insertcc(self,a):
       
        if a <1000:
            if a in cvcc:
                pass
            elif a % 10 == 9:
                if a//10*10+1 in cvcc:
                    cvcc.remove(a//10*10+1)
                elif a//10*10+2 in cvcc:
                    cvcc.remove(a//10*10+2)
                elif a//10*10+3 in cvcc:
                    cvcc.remove(a//10*10+3)
                elif a//10*10+4 in cvcc:
                    cvcc.remove(a//10*10+4)
                elif a//10*10+5 in cvcc:
                    cvcc.remove(a//10*10+5)
                elif a//10*10+6 in cvcc:
                    cvcc.remove(a//10*10+6)
                elif a//10*10+7 in cvcc:
                    cvcc.remove(a//10*10+7)
                elif a//10*10+8 in cvcc:
                    cvcc.remove(a//10*10+8)
                elif a//10*10+9 in cvcc:
                    cvcc.remove(a//10*10+9)
                elif a//10*10 in cvcc:
                    cvcc.remove(a//10*10)
                print("remove")
                
                
            else:
                if a//10*10+1 in cvcc:
                    cvcc.remove(a//10*10+1)
                elif a//10*10+2 in cvcc:
                    cvcc.remove(a//10*10+2)
                elif a//10*10+3 in cvcc:
                    cvcc.remove(a//10*10+3)
                elif a//10*10+4 in cvcc:
                    cvcc.remove(a//10*10+4)
                elif a//10*10+5 in cvcc:
                    cvcc.remove(a//10*10+5)
                elif a//10*10+6 in cvcc:
                    cvcc.remove(a//10*10+6)
                elif a//10*10+7 in cvcc:
                    cvcc.remove(a//10*10+7)
                elif a//10*10+8 in cvcc:
                    cvcc.remove(a//10*10+8)
                elif a//10*10+9 in cvcc:
                    cvcc.remove(a//10*10+9)
                elif a//10*10 in cvcc:
                    cvcc.remove(a//10*10)
                cvcc.append(a)
                print("append")
                
                
                    
        elif a >= 1000:
            if a in mpcc:
                mpcc.remove(a)
            else:
                mpcc.append(a)
                
        self.restart()    
        print(cvcc,mpcc)
            
        
    
    #面板刷新
    def restart(self):
        self.items()
        self.level() 
        self.conflict('non')
    
    #合约项目反显
    def items(self):
        self.textBrowser.clear()
        a = []
        b = []
        c = ''
        
        for i in cvcc:
            a.append(cvccdic[str(i//10*10)]+'+'+str(i%10))
        
        for i in mpcc:
            b.append(mpccdic[str(i//10*10)]+'*'+str(muti_mpccdic[str(i)]))
        
        c+='常规合约\n您选择了：\n'
        for i in a:
            c+=i+'\n'
        
        c+='\n倍率合约\n您选择了：\n'
        for i in b:
            c+=i+'\n'
        
        self.textBrowser.insertPlainText(c)
        
    
    #合约等级计算
    def level(self):
        
        a = 0
        for i in cvcc:
            a+=int(i%10)

        for i in mpcc:
            a = a*muti_mpccdic[str(i)]
        print(a)
        self.lcdNumber.display(int(a))
        return(a)
    
    '''
    datapack区
    '''
    

    #冲突检测 if 后面冲突项目and冲突项目
    def conflict(self,a):
        if 1000 in mpcc and 121 in cvcc:
            if a == 'yes':
                self.textBrowser_2.insertPlainText('生成出错!：<%s>与<%s>不能同时选择！'%(mpccdic[str(1000)],cvccdic[str(120)]))
            else:
                self.textBrowser.append('<%s>与<%s>不能同时选择！'%(mpccdic[str(1000)],cvccdic[str(120)]))
            return False
        
        elif 1010 in mpcc and (181 in cvcc or 182 in cvcc or 183 in cvcc):
            if a == 'yes':
                self.textBrowser_2.insertPlainText('生成出错!：<%s>与<%s>不能同时选择！'%(mpccdic[str(1010)],cvccdic[str(180)]))
            else:
                self.textBrowser.append('<%s>与<%s>不能同时选择！'%(mpccdic[str(1010)],cvccdic[str(180)]))
            return False
        
        elif (71 in cvcc or 73 in cvcc or 75 in cvcc) and (232 in cvcc or 233 in cvcc):
            if a == 'yes':
                self.textBrowser_2.insertPlainText('生成出错!：<%s>与<%s>不能同时选择！'%(cvccdic[str(70)],cvccdic[str(230)]))
            else:
                self.textBrowser.append('<%s>与<%s>不能同时选择！'%(cvccdic[str(70)],cvccdic[str(230)]))
            return False
        else:
            return True
    
    #写入tellraw文件 注意！没有修改工作目录    
    def write_tellraw(self):
        c = ''
        
        with open(path+r'\workspace\datapack\data\common\functions\cc.mcfunction','w',encoding='utf-8') as a:#注意路径！！还没改到工作目录！！
            #下个版本这里争取换为外部存储！
            tellraw = {'11':r'{"text":"环境：耐力I ","color":"green","hoverEvent":{"action":"show_text","contents":{"text":"所有敌对生物生命值提高60%"}}}','12':r'{"text":"环境：耐力II ","color":"green","hoverEvent":{"action":"show_text","contents":{"text":"所有敌对生物生命值提高110%"}}}','13':r'{"text":"环境：耐力III ","color":"yellow","hoverEvent":{"action":"show_text","contents":{"text":"所有敌对生物生命值提高160%"}}}','21':r'{"text":"环境：刺激I ","color":"green","hoverEvent":{"action":"show_text","contents":{"text":"所有敌对生物攻击力提升30%"}}}','22':r'{"text":"环境：刺激II ","color":"green","hoverEvent":{"action":"show_text","contents":{"text":"所有敌对生物攻击力提升60%"}}}','23':r'{"text":"环境：刺激III ","color":"yellow","hoverEvent":{"action":"show_text","contents":{"text":"所有敌对生物攻击力提升90%"}}}','31':r'{"text":"环境：爆发I ","color":"green","hoverEvent":{"action":"show_text","contents":{"text":"所有敌对生物移速增加25%"}}}','32':r'{"text":"环境：爆发II ","color":"green","hoverEvent":{"action":"show_text","contents":{"text":"所有敌对生物移速增加50%"}}}','33':r'{"text":"环境：爆发III ","color":"yellow","hoverEvent":{"action":"show_text","contents":{"text":"所有敌对生物移速增加75%"}}}','41':r'{"text":"目标:侵蚀I ","color":"green","hoverEvent":{"action":"show_text","contents":{"text":"生命值上限降低4"}}}','43':r'{"text":"目标:侵蚀III ","color":"yellow","hoverEvent":{"action":"show_text","contents":{"text":"生命值上限降低8"}}}','46':r'{"text":"目标:侵蚀VI ","color":"red","hoverEvent":{"action":"show_text","contents":{"text":"生命值上限降低16"}}}','51':r'{"text":"环境：虚弱因子I ","color":"green","hoverEvent":{"action":"show_text","contents":{"text":"造成伤害降低15%"}}}','52':r'{"text":"环境：虚弱因子II ","color":"green","hoverEvent":{"action":"show_text","contents":{"text":"造成伤害降低30%"}}}','54':r'{"text":"环境：虚弱因子IV ","color":"yellow","hoverEvent":{"action":"show_text","contents":{"text":"造成伤害降低30%，挖掘疲劳I级"}}}','65':r'{"text":"目标：殊死搏斗V ","color":"red","hoverEvent":{"action":"show_text","contents":{"text":"你无法自然恢复生命"}}}','71':r'{"text":"环境：亡灵觉醒I ","color":"green","hoverEvent":{"action":"show_text","contents":{"text":"亡灵类生物生命值提高50%,攻击力提高40%"}}}','73':r'{"text":"环境：亡灵觉醒III ","color":"yellow","hoverEvent":{"action":"show_text","contents":{"text":"亡灵类生物生命值提高100%,攻击力提高80%"}}}','75':r'{"text":"环境：亡灵觉醒V ","color":"red","hoverEvent":{"action":"show_text","contents":{"text":"亡灵类生物生命值提高150%,攻击力提高120%"}}}','82':r'{"text":"环境:隐形爆破II ","color":"green","hoverEvent":{"action":"show_text","contents":{"text":"苦力怕隐形，无声"}}}','91':r'{"text":"环境:灵敏嗅觉I ","color":"green","hoverEvent":{"action":"show_text","contents":{"text":"敌对生物发现玩家距离提升175%"}}}','101':r'{"text":"目标：龙吟I ","color":"green","hoverEvent":{"action":"show_text","contents":{"text":"[末影龙]伤害提升50%,生命值提升75%"}}}','102':r'{"text":"目标：龙吟II ","color":"green","hoverEvent":{"action":"show_text","contents":{"text":"[末影龙]伤害提升100%,生命值提升150%"}}}','103':r'{"text":"目标：龙吟III ","color":"yellow","hoverEvent":{"action":"show_text","contents":{"text":"[末影龙]伤害提升150%,生命值提升250%"}}}','121':r'{"text":"削弱:失眠I ","color":"green","hoverEvent":{"action":"show_text","contents":{"text":"你无法入睡，与永夜冲突"}}}','132':r'{"text":"环境:易碎物品II ","color":"green","hoverEvent":{"action":"show_text","contents":{"text":"死亡后掉落物品消失"}}}','140':r'{"text":"难度:简单 ","color":"green","hoverEvent":{"action":"show_text","contents":{"text":"难度设为简单"}}}','141':r'{"text":"难度:普通 ","color":"green","hoverEvent":{"action":"show_text","contents":{"text":"难度设为普通"}}}','142':r'{"text":"难度:困难 ","color":"green","hoverEvent":{"action":"show_text","contents":{"text":"难度设为困难"}}}','151':r'{"text":"目标:沉重武器I ","color":"green","hoverEvent":{"action":"show_text","contents":{"text":"攻击速度减少0.3"}}}','152':r'{"text":"目标:沉重武器II ","color":"green","hoverEvent":{"action":"show_text","contents":{"text":"攻击速度减少0.6"}}}','161':r'{"text":"目标:失明I ","color":"green","hoverEvent":{"action":"show_text","contents":{"text":"血量低于6时失明"}}}','162':r'{"text":"目标:失明II ","color":"green","hoverEvent":{"action":"show_text","contents":{"text":"血量低于12时失明"}}}','163':r'{"text":"目标:失明III ","color":"yellow","hoverEvent":{"action":"show_text","contents":{"text":"血量低于16时失明"}}}','165':r'{"text":"目标:失明V ","color":"red","hoverEvent":{"action":"show_text","contents":{"text":"血量低于24时失明"}}}','172':r'{"text":"环境:暴雨 ","color":"green","hoverEvent":{"action":"show_text","contents":{"text":"天气恒为雷雨"}}}','181':r'{"text":"目标:生命限制I ","color":"green","hoverEvent":{"action":"show_text","contents":{"text":"复活次数限定为25次"}}}','182':r'{"text":"目标:生命限制II ","color":"green","hoverEvent":{"action":"show_text","contents":{"text":"复活次数限定为20次"}}}','183':r'{"text":"目标:生命限制III ","color":"yellow","hoverEvent":{"action":"show_text","contents":{"text":"复活次数限定为15次"}}}','191':r'{"text":"环境:节肢动物强化I ","color":"green","hoverEvent":{"action":"show_text","contents":{"text":"蜘蛛、洞穴蜘蛛获得速度2效果"}}}','192':r'{"text":"环境:节肢动物强化II ","color":"green","hoverEvent":{"action":"show_text","contents":{"text":"蜘蛛、洞穴蜘蛛获得速度2、隐身效果"}}}','201':r'{"text":"削弱:沉重I ","color":"green","hoverEvent":{"action":"show_text","contents":{"text":"玩家移动速度减慢15%"}}}','202':r'{"text":"削弱:沉重II ","color":"green","hoverEvent":{"action":"show_text","contents":{"text":"玩家移动速度减慢25%"}}}','203':r'{"text":"削弱:沉重III ","color":"yellow","hoverEvent":{"action":"show_text","contents":{"text":"玩家移动速度减慢40%"}}}','211':r'{"text":"环境:思想钢印I ","color":"green","hoverEvent":{"action":"show_text","contents":{"text":"在水中受到中毒效果"}}}','232':r'{"text":"特化:亡灵II ","color":"green","hoverEvent":{"action":"show_text","contents":{"text":"僵尸类血量提升至1000%,移动速度降低50%,伤害降低20%;骷髅类伤害提升600%,移动速度降低30%,血量降低40%"}}}','233':r'{"text":"特化:亡灵III ","color":"yellow","hoverEvent":{"action":"show_text","contents":{"text":"僵尸类血量提升至1000%,移动速度降低30%,伤害降低10%;骷髅类伤害提升600%,移动速度降低20%,血量降低20%"}}}','1000':r'{"text":"永夜x1.5 ","color":"light_purple"}','1010':r'{"text":"极限x1.8 ","color":"light_purple"}','1020':r'{"text":"死亡不掉落x0.7 ","color":"light_purple"}'}

            for i in cvcc:
                c = c+tellraw[str(i)]+','
                print(c+'\n')
            c = c[:-1]
            a.write('tellraw @s {"text":"当前选择的合约有:","color":"aqua"}\n'+'tellraw @s ['+c+']')
    
    #编辑dragon包
    def write_dragon(self):
        if 101 or 102 or 103 in cvcc:
            with open(path+r'\workspace\datapack\data\common\functions\dragon.mcfunction','w',encoding='utf-8') as a:
                c = '0'
                
                dragon = {'101':'0.5','102':'1','103':'1.5'}
                if 101 in cvcc:
                    c = dragon[str(101)]
                elif 102 in cvcc:
                    c = dragon[str(102)]
                elif 103 in cvcc:
                    c = dragon[str(103)]
                
                d = 'execute as @e[type=minecraft:ender_dragon] at @s run attribute @s generic.max_health modifier add 100af772-b04b-49cb-948d-abb3cb0bc455 CC_dragon_health '+c+' multiply\n'+'execute as @e[type=minecraft:ender_dragon,tag=!CC_dragon_health] at @s run data modify entity @s Health set value 40000\n'+'tag @e[type=minecraft:ender_dragon] add CC_dragon_health\n'+'execute as @e[type=minecraft:ender_dragon] run attribute @s minecraft:generic.attack_damage modifier add 100af762-b04b-49cb-958d-abb3cb0bca45 CC_dragon_attack '+c+' multiply'

                print(d)
                a.write(d)
        else:
            pass
    


    #编辑firstload包
    def write_firstload(self):
        d,f,t,di = 'day','true','','easy'
        level = ''
        r = 'true'
        k = 'false'
        
        with open(path+r'\workspace\datapack\data\common\functions\firstload.mcfunction','w',encoding='utf-8') as a:
            level = str(self.level())
            if 1000 in mpcc:
                d = '18000'
                f = 'false'
            
                
            if 172 in cvcc:
                t = '''weather thunder
gamerule doWeatherCycle false'''
            
            if 141 in cvcc:
                di = 'normal'
            if 142 in cvcc:
                di = 'hard'
            if 1010 in mpcc:
                di = 'hard'
                self.radio_allspeed_27.click()
                time.sleep(0.5)
            if 65 in cvcc:
                r = 'false'
            if 1020 in mpcc or 132 in cvcc:
                k = 'true'

            w = '''scoreboard objectives add players dummy "历史登录玩家"
scoreboard objectives add dif dummy "难度"
scoreboard players set #dif dif %s
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
time set %s
gamerule doDaylightCycle %s

#若不选择雷阵雨则删除这句和clock.mcfunction
%s

#难度选择（极限模式请调为hard）
difficulty %s

#不回血
gamerule naturalRegeneration %s
#死亡不掉落
gamerule keepInventory %s'''%(str(int(float(level))),d,f,t,di,r,k)
            print(w)
            a.write(w)



    #编辑 tick.mcfun
    def write_tick(self):
        with open(path+r'\workspace\datapack\data\common\functions\tick.mcfunction','w',encoding='utf-8') as a:
            
            zb_hp = 1 #zb血线
            zb_at = 1 #亡灵攻击
            zb_sp = 1
            kl_hp = 1
            kl_at = 1
            kl_hp = 1
            kl_sp = 1

            
            pl_atk_cd = '4' #玩家攻击间隔
            al_atk = '1'#怪物攻击提升
            al_hp = '1'#怪物血量提升
            al_speed = '1'#怪物速度
            pl_hpupend = '20'#玩家血量上限
            cp_boom = ''#苦力怕隐形爆炸
            mob_find_d = '64'#怪物发现距离
            weak = ''#挖掘疲劳与虚弱
            cant_sleep = ''#不能入睡
            blind = '0'#掉血失明
            life = ''#生命限制
            spider_up = ''#蜘蛛升级
            w_m_y_died = ''#rt
            
            pl_sp = '0'
            

            


                


            if 71 in cvcc:  
                zb_at = zb_at*1.5
                zb_hp = zb_hp*1.6
                kl_at = kl_at*1.5
                kl_hp =kl_hp*1.6 
                
            if 73 in cvcc:
                zb_at = zb_at*1.8
                zb_hp = zb_hp*2
                kl_at = kl_at*1.8
                kl_hp =kl_hp*2
            if 75 in cvcc:
                zb_at = zb_at*2.2
                zb_hp = zb_hp*2.5
                kl_at = kl_at*2.2
                kl_hp =kl_hp*2.5
            
            if 11 in cvcc:
                #zb_hp = zb_hp*1.6
                #kl_hp = kl_hp*1.6
                al_hp = '1.6'
            if 12 in cvcc:
                #zb_hp = zb_hp*2.1
                #kl_hp = kl_hp*2.1
                al_hp = '2.1'
            if 13 in cvcc:
                #zb_hp = zb_hp*2.6
                #kl_hp = kl_hp*2.6
                al_hp = '2.6'
                
            
            if 21 in cvcc:
                al_atk = '1.3'
            if 22 in cvcc:
                al_atk = '1.6'
            if 23 in cvcc:
                al_atk = '1.9'
            
            if 151 in cvcc:
                pl_atk_cd = '3.7'
            if 152 in cvcc:
                pl_atk_cd = '3.4'

            if 31 in cvcc:
                al_speed = '1.25'
            if 32 in cvcc:
                al_speed = "1.5"
            if 33 in cvcc:
                al_speed = '1.75'
            
            if 41 in cvcc:
                pl_hpupend = '16'
            if 43 in cvcc:
                pl_hpupend = '12'
            if 46 in cvcc:
                pl_hpupend = '4'
            
            if 82 in cvcc:
                cp_boom = '''execute as @e[type=creeper] run data merge entity @s {Silent:1b}
effect give @e[type=minecraft:creeper] minecraft:invisibility 999 0 true
execute as @e[type=minecraft:creeper] at @s if entity @a[distance=..3] run effect clear'''

            if 91 in cvcc:
                mob_find_d = '112'
            
            if 51 in cvcc:
                weak = 'execute as @a run attribute @s minecraft:generic.attack_damage base set 0.85'
            if 52 in cvcc:
                weak = 'execute as @a run attribute @s minecraft:generic.attack_damage base set 0.7'
            if 54 in cvcc:
                weak = 'execute as @a run attribute @s minecraft:generic.attack_damage base set 0.7\neffect give @a minecraft:mining_fatigue 999999 0 true'
            
            if 121 in cvcc:
                cant_sleep = 'execute as @a at @s if block ~ ~-0.5625 ~ #minecraft:beds run tp @s ~ ~0.00001 ~'

            if 161 in cvcc:
                blind = '5'
            if 162 in cvcc:
                blind = '11'
            if 163 in cvcc:
                blind = '15'
            if 165 in cvcc:
                blind = '23'
            
            if 1010 in mpcc:
                life = '''execute as @a if score @s death matches 1.. run tag @s add gameover
gamemode spectator @a[tag=gameover]
execute as @a if score @s death matches 1.. run function common:finish'''
            if 181 in cvcc:
                life = '''execute as @a if score @s death matches 25.. run tag @s add gameover
gamemode spectator @a[tag=gameover]
execute as @a if score @s death matches 25.. run function common:finish'''
            if 182 in cvcc:
                life = '''execute as @a if score @s death matches 20.. run tag @s add gameover
gamemode spectator @a[tag=gameover]
execute as @a if score @s death matches 20.. run function common:finish'''
            if 183 in cvcc:
                life = '''execute as @a if score @s death matches 15.. run tag @s add gameover
gamemode spectator @a[tag=gameover]
execute as @a if score @s death matches 15.. run function common:finish'''

            if 191 in cvcc:
                spider_up = 'effect give @e[type=#spider] minecraft:speed 20 1 true'
            if 192 in cvcc:
                spider_up = 'effect give @e[type=#spider] minecraft:speed 20 1 true\neffect give @e[type=#spider] minecraft:invisibility 20 0 true'

            if 211 in cvcc:
                w_m_y_died = 'execute as @a at @s if block ~ ~ ~ water run effect give @s minecraft:wither 6 0 false'

            if 232 in cvcc:
                zb_at = zb_at*0.8
                zb_hp = zb_hp*10
                zb_sp = float(al_speed)*0.5
                kl_at = kl_at*7
                kl_hp =kl_hp*0.6
                kl_sp = float(al_speed)*0.5
            if 233 in cvcc:
                zb_at = zb_at*0.9
                zb_hp = zb_hp*10
                zb_sp = float(al_speed)*0.7
                kl_at = kl_at*7
                kl_hp =kl_hp*0.8
                kl_sp = float(al_speed)*0.8+0.3
            
            if 201 in cvcc:
                pl_sp = '-0.15'
            if 202 in cvcc:
                pl_sp = '-0.25'
            if 203 in cvcc:
                pl_sp = '-0.4'
            
            zb_at = zb_at*float(al_atk)-1
            zb_hp = zb_hp*float(al_hp)-1
            kl_at = kl_at*float(al_atk)-1
            kl_hp = kl_hp*float(al_hp)-1
            zb_sp = zb_sp*float(al_speed)-1
            kl_sp = kl_sp*float(al_speed)-1

            zb_at = str(round(zb_at,2))
            zb_hp = str(round(zb_hp,2))
            zb_sp = str(round(zb_sp,2)) 
            kl_at = str(round(kl_at,2))
            kl_hp = str(round(kl_hp,2))
            kl_sp = str(round(kl_sp,2))
            print(zb_at)
            
            al_atk = str(round((float(al_atk)-1),2))
            al_speed = str(round((float(al_speed)-1),2))
            al_hp = str(round((float(al_hp)-1),2))
            print(al_speed)





            
             


            w = '''function common:clock
function common:info_show
function common:playercheck
execute as @a if score @s info matches 1.. run function common:setting
scoreboard players enable @a info
#亡灵类生物属性
#HP
execute as @e[type=#zombie] at @s run attribute @s generic.max_health modifier add 100af772-b04b-49cb-958d-abb3cb0bc415 CC_died_health %s multiply
execute as @e[type=#skeleton] at @s run attribute @s generic.max_health modifier add 100af772-b04b-49cb-958d-abb3cb0bc415 CC_died_health %s multiply
execute as @e[tag=!CC_died_health,type=#died] run data modify entity @s Health set value 20000
tag @e[type=#died] add CC_died_health
#ATK
execute as @e[type=#zombie] run attribute @s minecraft:generic.attack_damage modifier add 100af772-b04b-49cb-958d-abb3cb0bcd45 CC_died_attack %s multiply
execute as @e[type=#skeleton] run attribute @s minecraft:generic.attack_damage modifier add 100af772-b04b-49cb-958d-abb3cb0bcd45 CC_died_attack %s multiply

#小白属性
#ATK
replaceitem entity @e[type=minecraft:skeleton,tag=!CC_Skeleton_attack] weapon bow{Enchantments:[{id:"power",lvl:%s}]}
tag @e[type=minecraft:skeleton] add CC_Skeleton_attack

#玩家攻击间隔加长 
execute as @a run attribute @s minecraft:generic.attack_speed base set %s

#敌对生命加强
execute as @e[type=#mob] at @s run attribute @s generic.max_health modifier add 100af772-b04b-49cb-958d-abb3cb0bc455 CC_mob_health %s multiply
execute as @e[type=#mob] at @s run data modify entity @s Health set value 20000
tag @e[type=#mob] add CC_mob_health

#敌对攻击加强
execute as @e[type=#mob] run attribute @s minecraft:generic.attack_damage modifier add 100af762-b04b-49cb-958d-abb3cb0bcd45 CC_mob_attack %s multiply

#敌对速度加强
execute as @e[type=#mob] run attribute @s minecraft:generic.movement_speed modifier add 100af772-b04b-49cb-958d-abb3cb0bdd54 CC_mob_speed %s multiply
execute as @e[type=#zombie] run attribute @s minecraft:generic.movement_speed modifier add 100af772-b04b-49cb-958d-abb3cb0bdd54 CC_mob_speed %s multiply
execute as @e[type=#skeleton] run attribute @s minecraft:generic.movement_speed modifier add 100af772-b04b-49cb-958d-abb3cb0bdd54 CC_mob_speed %s multiply
execute as @e[type=creeper] run attribute @s minecraft:generic.movement_speed modifier add 100af772-b04b-49cb-958d-abb3cb0bdd54 CC_mob_speed %s multiply

#玩家生命上限降低
execute as @a run attribute @s minecraft:generic.max_health base set %s

#苦力怕隐形，无声
%s

#增加怪物侦查
execute as @e[type=#died] run attribute @s minecraft:generic.follow_range base set %s
execute as @e[type=#mob] run attribute @s minecraft:generic.follow_range base set %s
execute as @e[type=creeper] run attribute @s minecraft:generic.follow_range base set %s

#末影龙增强
execute as @a at @s if entity @e[type=ender_dragon] run function common:dragon

#凋零加强
execute as @a at @s if entity @e[type=wither] run function common:wither

#伤害降低to 0.7/挖掘疲劳
%s

#检测玩家死亡
execute as @a if score @s death > @s deathF run tag @s add died
scoreboard players add @a[tag=died] deathF 1
clear @a[tag=died]
tag @a remove died

#无法入睡
%s

#掉血失明
execute as @a if score @s HP matches ..%s run effect give @s minecraft:blindness 2 0 true

#生命限制
%s

#蜘蛛强化
%s

#毒水
%s
#玩家减速
execute as @a run attribute @s minecraft:generic.movement_speed modifier add 100af762-b04b-49cb-958d-abb3cb0bcd45 player_speed %s multiply

execute if entity @s[advancements={minecraft:end/kill_dragon=true}] run tag @a add win
execute if entity @s[advancements={minecraft:end/kill_dragon=true}] run function common:finish'''%(zb_hp,kl_hp,zb_at,kl_at,str(int(float(kl_at)*4)),pl_atk_cd,al_hp,al_atk,al_speed,zb_sp,kl_sp,al_speed,pl_hpupend,cp_boom,mob_find_d,mob_find_d,mob_find_d,weak,cant_sleep,blind,life,spider_up,w_m_y_died,pl_sp)
            print(w)#上面格式化丢失两个
            a.write(w)
    
    
    
    def zipDir(self,dirpath,outFullName):
    
        zip = zipfile.ZipFile(outFullName,"w",zipfile.ZIP_DEFLATED)
        for path,dirnames,filenames in os.walk(dirpath):
            # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
            fpath = path.replace(dirpath,'')

            for filename in filenames:
                zip.write(os.path.join(path,filename),os.path.join(fpath,filename))
        zip.close()

    
    
    #打包datapack 主程序
    def write(self):
        self.textBrowser_2.clear()
        if self.conflict('yes'):
            self.write_tellraw()
            self.write_dragon()
            self.write_firstload()
            self.write_tick()
            self.zipDir(path+r'\workspace\datapack',path+r'\危机合约'+str(int(self.level()))+'by_秋梨社.zip')
            self.textBrowser_2.insertPlainText('生成成功!\n您的合约等级为%s'%self.level())
        else:
            pass
        



if __name__=="__main__":
    import sys

    app=QtWidgets.QApplication(sys.argv)
    
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    ui = mywindow()    
    ui.show()
    sys.exit(app.exec_())