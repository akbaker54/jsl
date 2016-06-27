# This Python file uses the following encoding: utf-8
import os
import sys

digits = {"0": "", "1":"itî","2":"nî","3":"san̄","4":"sî","4'":"yôn̄","5":"gô","6":"rokû","7":"sitî","7'":"nâna","8":"hatî","9":"kû","9'":"kyûu","10":"zyûu","11":"zyuúitì","12":"zyuúnì","13":"zyûusan̄","14":"zyuúsì","15":"zyûugo","16":"zyuúrokù","17":"zyuúsitì","18":"zyuúhatì","19":"zyûuku","20":"nîzyuu ","21":"nîzyuu itî","22":"nîzyuu nî","23":"nîzyuu ` san̄","24":"nîzyuu sî","25":"nîzyuu gô","26":"nîzyuu rokû","27":"nîzyuu sitî","28":"nîzyuu hatî","29":"nîzyuu kû","30":"san̄zyuu ","31":"san̄zyuu itî","32":"san̄zyuu nî","33":"san̄zyuu ` san̄","34":"san̄zyuu sî","35":"san̄zyuu gô","36":"san̄zyuu rokû","37":"san̄zyuu sitî","38":"san̄zyuu hatî","39":"san̄zyuu kû","40":"yôn̄zyuu ","41":"yôn̄zyuu itî","42":"yôn̄zyuu nî","43":"yôn̄zyuu san̄","44":"yôn̄zyuu sî","45":"yôn̄zyuu gô","46":"yôn̄zyuu rokû","47":"yôn̄zyuu sitî","48":"yôn̄zyuu hatî","49":"yôn̄zyuu kû","50":"gozyûu ","51":"gozyúu itì","52":"gozyúu nì","53":"gozyúu san̄","54":"gozyúu sì","55":"gozyúu gò","56":"gozyúu rokù","57":"gozyúu sitì","58":"gozyúu hatì","59":"gozyúu kù","60":"rokúzyùu ","61":"rokúzyuu itì","62":"rokúzyuu nì","63":"rokuzyuu san̄","64":"rokúzyuu sì","65":"rokúzyuu gò","66":"rokúzyuu rokù","67":"rokúzyuu sitì","68":"rokúzyuu hatì","69":"rokúzyuu kù","70":"nanâzyuu ","71":"nanâzyuu itî","72":"nanâzyuu nî","73":"nanâzyuu ` san̄","74":"nanâzyuu sî","75":"nanâzyuu gô","76":"nanâzyuu rokû","77":"nanâzyuu sitî","78":"nanâzyuu hatî","79":"nanâzyuu kû","80":"hatízyùu ","81":"hatízyuu itì","82":"hatízyuu nì","83":"hatizyuu ` san̄","84":"hatízyuu sì","85":"hatízyuu gò","86":"hatízyuu rokù","87":"hatízyuu sitì","88":"hatízyuu hatì","89":"hatízyuu kù","90":"kyûuzyuu ","91":"kyûuzyuu itî","92":"kyûuzyuu nî","93":"kyûuzyuu ` san̄","94":"kyûuzyuu sî","95":"kyûuzyuu gô","96":"kyûuzyuu rokû","97":"kyûuzyuu sitî","98":"kyûuzyuu hatî","99":"kyûuzyuu kû","100":"hyakû","200":"nihyákù","300":"sânbyaku","400":"yônhyaku","500":"gohyákù","600":"roṕpyakù","700":"nanâhyaku","800":"haṕpyakù","900":"kyûuhyaku","1000":"iśsèn̄","2000":"nisên̄","3000":"sańzèn̄","4000":"yońsèn̄","5000":"gosên̄","6000":"rokúsèn̄","7000":"nanásèn̄","8000":"haśsèn̄","9000":"kyuúsèn̄","10000":"itímàn̄","20000":"nimân̄","30000":"sańmàn̄","40000":"yońmàn̄","50000":"gomân̄","60000":"rokúmàn̄","70000":"nanámàn̄","80000":"hatímàn̄","90000":"kyuúmàn̄","100000":"zyuúmàn̄"}


def jpnum(num,digits):
    num = str(num)
    if len(num) >4:
        pi = 4
    else:
        pi = 8
    for i in range(0,pi-len(str(num))):
        num = "0" + num
    if pi = 4:
        numa = "0"
        numb = num
    if pi = 8:
        numa = num[0:3]
        numb = num[4:7]
        digits = numb[2:3]
        hun = numb[1:1] + "00"
        thou = numb[0:0] + "0"
    return digits[numa]





def joooooooooooooopnum(num):
    hun = ""
    thou = ""
    tenthou = ""
    num = str(num)
    leng = len(num)
    hun = num[(leng-3):(leng-2)] + "00"
    thou = num[(leng-4):(leng-3)] + "000"
    tenthou = num[:(leng-4)] + "0000"
    return jpnum(tenthou) + " mân " + digits[thou] + " " + digits[hun] + " " + digits[num[(leng-2):]]




#tens = num[(leng-2):]

print(jpnum(321))