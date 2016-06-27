import sys
import os
import codecs

r = ["A", "a","I","i","U","u","E","e","O","o","ka","ga","ki","gi","ku","gu","ke","ge","ko","go","sa","za","si","zi","su","zu","se","ze","so","zo","ta","da","ti","di","TU","tu","du","te","de","to","do","na","ni","nu","ne","no","ha","ba","pa","hi","bi","pi","hu","bu","pu","he","be","pe","ho","bo","po","ma","mi","mu","me","mo","YA","ya","YU","yu","YO","yo","ra","ri","ru","re","ro","WA","wa","wi","we","wo","n̄","vu","KA","KE","kya","kyu","kyo","gya","gyu","gyo","sya","syu","syo","zya","zyu","zyo","tya","tyu","tyo","dya","dyu","dyo","nya","nyu","nyo","hya","hyu","hyo","bya","byu","byo","pya","pyu","pyo","mya","myu","myo","rya","ryu","ryo","fa","fi","fe","fo","va","vi","ve","vo"]
k = ["ァ","ア","ィ","イ","ゥ","ウ","ェ","エ","ォ","オ","カ","ガ","キ","ギ","ク","グ","ケ","ゲ","コ","ゴ","サ","ザ","シ","ジ","ス","ズ","セ","ゼ","ソ","ゾ","タ","ダ","チ","ヂ","ッ","ツ","ヅ","テ","デ","ト","ド","ナ","ニ","ヌ","ネ","ノ","ハ","バ","パ","ヒ","ビ","ピ","フ","ブ","プ","ヘ","ベ","ペ","ホ","ボ","ポ","マ","ミ","ム","メ","モ","ャ","ヤ","ュ","ユ","ョ","ヨ","ラ","リ","ル","レ","ロ","ヮ","ワ","ヰ","ヱ","ヲ","ン","ヴ","ヵ","ヶ","きゃ","きゅ","きょ","ぎゃ","ぎゅ","ぎょ","しゃ","しゅ","しょ","じゃ","じゅ","じょ","ちゃ","ちゅ","ちょ","ぢゃ","ぢゅ","ぢょ","にゃ","にゅ","にょ","ひゃ","ひゅ","ひょ","びゃ","びゅ","びょ","ぴゃ","ぴゅ","ぴょ","みゃ","みゅ","みょ","りゃ","りゅ","りょ","ファ","フィ","フェ","フォ","ヴァ","ヴィ","ヴェ","ヴォ"]
h = ["ぁ","あ","ぃ","い","ぅ","う","ぇ","え","ぉ","お","か","が","き","ぎ","く","ぐ","け","げ","こ","ご","さ","ざ","し","じ","す","ず","せ","ぜ","そ","ぞ","た","だ","ち","ぢ","っ","つ","づ","て","で","と","ど","な","に","ぬ","ね","の","は","ば","ぱ","ひ","び","ぴ","ふ","ぶ","ぷ","へ","べ","ぺ","ほ","ぼ","ぽ","ま","み","む","め","も","ゃ","や","ゅ","ゆ","ょ","よ","ら","り","る","れ","ろ","ゎ","わ","ゐ","ゑ","を","ん","ゔ","ゕ","ゖ","キャ","キュ","キョ","ギャ","ギュ","ギョ","シャ","シュ","ショ","ジャ","ジュ","ジョ","チャ","チュ","チョ","ヂャ","ヂュ","ヂョ","ニャ","ニュ","ニョ","ヒャ","ヒュ","ヒョ","ビャ","ビュ","ビョ","ピャ","ピュ","ピョ","ミャ","ミュ","ミョ","リャ","リュ","リョ","ふぁ","ふぃ","ふぇ","ふぉ","ゔぁ","ゔぃ","ゔぇ","ゔぉ"]

rkh = {}
khr = {}
hrk = {}

for i in range(0,len(r)-1):
    rkh[r[i]] = (k[i], h[i])
    khr[k[i]] = (h[i], r[i])
    hrk[h[i]] = (r[i], k[i])

def scnd(x):
    (first,second) = x
    return second

def frst(x):
    (first,second) = x
    return first

def RtoH(exr):
    if exr not in r:
        print("Sorry, ",exr," isn't in the romaji list. Are you using JSL transliteration? (RtoH)")
    return scnd(rkh[exr])
def RtoK(exr):
    if exr not in r:
        print("Sorry, ",exr," isn't in the romaji list. Are you using JSL transliteration? (RtoK)")
    return frst(rkh[exr])
def KtoH(exk):
    if exk not in k:
        print("Sorry, ",exk," isn't in the katakana list. Maybe you put hiragana in instead? (KtoH)")
    return frst(khr[exk])
def KtoR(exk):
    if exk not in k:
        print("Sorry, ",exk," isn't in the katakana list. Maybe you put hiragana in instead? (KtoR)")
    return scnd(khr[exk])
def HtoR(exh):
    if exh not in h:
        print("Sorry, ",exh," isn't in the hiragana list. Maybe you put katakana in instead? (HtoR)")
    return frst(hrk[exh])
def HtoK(exh):
    if exh not in h:
        print("Sorry, ",exh," isn't in the hiragana list. Maybe you put katakana in instead? (HtoK)")
    return scnd(hrk[exh])
failCountRHKR = 0
failCountRKHR = 0
RtoHtoKtoR = False
RtoKtoHtoR = False
for i in range(0,len(r)-1):
    print("checking on",i,"... the romaji is",r[i]+", the katakana is",k[i]+", and the hiragana is",h[i])
    if RtoH(r[i]) != h[i]:
        print("FAIL! RtoH(r[", i , "] should equal h[", i , "] =", h[i], "but instead it equals", RtoH(r[i]), "!!")
    if RtoK(r[i]) != k[i]:
        print("FAIL! RtoK(r[", i , "] should equal k[", i , "] =", k[i], "but instead it equals", RtoK(r[i]), "!!")
    if KtoH(k[i]) != h[i]:
        print("FAIL! KtoH(k[", i , "] should equal h[", i , "] =", h[i], "but instead it equals", KtoH(k[i]), "!!")
    if KtoR(k[i]) != r[i]:
        print("FAIL! KtoR(k[", i , "] should equal r[", i , "] =", r[i], "but instead it equals", KtoR(k[i]), "!!")
    if HtoR(h[i]) != r[i]:
        print("FAIL! HtoR(h[", i , "] should equal r[", i , "] =", r[i], "but instead it equals", HtoR(h[i]), "!!")
    if HtoK(h[i]) != k[i]:
        print("FAIL! HtoK(h[", i , "] should equal k[", i , "] =", k[i], "but instead it equals", HtoK(h[i]), "!!")

    if KtoR(HtoK(RtoH(r[i])))!=r[i]:
        RtoHtoKtoR = True
        failCountRHKR += 1
    if HtoR(KtoH(RtoK(r[i])))!=r[i]:
        RtoKtoHtoR = True
        failCountRKHR +=1
    if RtoHtoKtoR and RtoKtoHtoR:
        print("failure in both directions!")
    elif RtoHtoKtoR:
        print("failure in the RHKR direction only...")
    elif RtoKtoHtoR:
        print("failure in the RKHR direction only...")
#    else:
#        print("success...\#teamwork")
    RtoHtoKtoR = False
    RtoKtoHtoR = False
print(len(r))
print(failCountRKHR)
print(failCountRHKR)