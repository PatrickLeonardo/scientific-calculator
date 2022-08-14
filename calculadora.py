from tkinter import *
from math import *
from random import *
from path.funções import *
from path.help import *

janela = Tk() # janela
janela.geometry("780x440") # tamanho da janela
janela.title('CALCULADORA') # titulo
janela.config(background = '#404040')
expressao1 = Label(janela, text = "         ", background = '#404040')
expressao1.grid(column = 0, row = 0, padx = 10, pady = 10)



bot_help = Button(janela, text = "HELP", height = altura, width = largura, command = help1, background = background)
bot_help.grid(column = 1, row = 1, padx = padx, pady = pady)



def ress():
    global expressao
    try:
        resul = str(eval(expressao))
    except ZeroDivisionError:
        resul = 'ZeroDivisionError'
    except SyntaxError:
        resul = 'SyntaxError'
    except (ValueError, TypeError): 
        resul = 'Value or Type Error'
    except Exception as erro:
        resul = 'Error'
    bot_r["text"] = resul

botr = Button(janela, text = "=", height = altura, width = largura, command = ress, background = background)
botr.grid(column = 7, row = 20, padx = padx, pady = pady)
bot_r = Label(janela, text = "", background = "#85A68A", height = altura, width = 30)
bot_r.grid(column = 8, row = 6, padx = 30, pady = pady)



def binn():
    global expressao
    global expressao2
    global numero
    expressao = f'bin({numero})[2:]'
    expressao2 = f'bin({numero})[2:]'
    bot_r["text"] = expressao

bin1 = Button(janela, text = "BIN", height = altura, width = largura, command = binn, background = background)
bin1.grid(column = 3, row = 3, padx = padx, pady = pady)




def octt():
    global expressao
    global expressao2
    global numero
    expressao = f'oct({numero})[2:]'
    expressao2 = f'oct({numero})[2:]'
    bot_r["text"] = expressao

oct1 = Button(janela, text = "OCT", height = altura, width = largura, command = octt, background = background)
oct1.grid(column = 4, row = 3, padx = padx, pady = pady)




def hexx():
    global expressao
    global expressao2
    global numero
    expressao = f'hex({numero})[2:]'
    expressao2 = f'hex({numero})[2:]'
    bot_r["text"] = expressao

hex1 = Button(janela, text = "HEX", height = altura, width = largura, command = hexx, background = background)
hex1.grid(column = 5, row = 3, padx = padx, pady = pady)




def seno():
    global expressao
    global expressao2
    global numero
    expressao = f'sin(radians({numero}))'
    expressao2 = f'sin(radians({numero}))'
    bot_r["text"] = expressao

seno1 = Button(janela, text = "sin", height = altura, width = largura, command = seno, background = background)
seno1.grid(column = 1, row = 7, padx = padx , pady = pady)




def senoh():
    global expressao
    global expressao2
    global numero
    expressao = f'sinh({numero})'
    expressao2 = f'sinh({numero})'
    bot_r["text"] = expressao

senoh1 = Button(janela, text = "sinh", height = altura, width = largura, command = senoh, background = background)
senoh1.grid(column = 1, row = 9, padx = padx , pady = pady)




def cose():
    global expressao
    global expressao2
    global numero
    expressao = f'cos(radians({numero}))'
    expressao2 = f'cos(radians({numero}))'
    bot_r["text"] = expressao

cose1 = Button(janela, text = "cos", height = altura, width = largura, command = cose, background = background)
cose1.grid(column = 2, row = 7, padx = padx , pady = pady)



def coseh():
    global expressao
    global expressao2
    global numero
    expressao = f'cosh({numero})'
    expressao2 = f'cosh({numero})'
    bot_r["text"] = expressao

coseh1 = Button(janela, text = "cosh", height = altura, width = largura, command = coseh, background = background)
coseh1.grid(column = 2, row = 9, padx = padx , pady = pady)




def tang():
    global expressao
    global expressao2
    global numero
    expressao = f'tan(radians({numero}))'
    expressao2 = f'tan(radians({numero}))'
    bot_r["text"] = expressao

tan1 = Button(janela, text = "tan", height = altura, width = largura, command = tang, background = background)
tan1.grid(column = 3, row = 7, padx = padx , pady = pady)




def tangh():
    global expressao
    global expressao2
    global numero
    expressao = f'tanh({numero})'
    expressao2 = f'tanh({numero})'
    bot_r["text"] = expressao

tanh1 = Button(janela, text = "tanh", height = altura, width = largura, command = tangh, background = background)
tanh1.grid(column = 3, row = 9, padx = padx , pady = pady)




def sec():
    global expressao
    global expressao2
    global numero
    expressao = f'1 / (cos(radians({numero})))'
    expressao2 = f'1 / (cos(radians({numero})))'
    bot_r["text"] = expressao

sec1 = Button(janela, text = "sec", height = altura, width = largura, command = sec, background = background)
sec1.grid(column = 1, row = 8, padx = padx , pady = pady)




def sech():
    global expressao
    global expressao2
    global numero
    expressao = f'1 / (cosh({numero}))'
    expressao2 = f'1 / (cos({numero}))'
    bot_r["text"] = expressao

sech1 = Button(janela, text = "sech", height = altura, width = largura, command = sech, background = background)
sech1.grid(column = 1, row = 20, padx = padx , pady = pady)




def csc():
    global expressao
    global expressao2
    global numero
    expressao = f'1 / (sin(radians({numero})))'
    expressao2 = f'1 / (sin(radians({numero})))'
    bot_r["text"] = expressao

csc1 = Button(janela, text = "csc", height = altura, width = largura, command = csc, background = background)
csc1.grid(column = 2, row = 8, padx = padx , pady = pady)




def csch():
    global expressao
    global expressao2
    global numero
    expressao = f'1 / (sinh({numero}))'
    expressao2 = f'1 / (sinh({numero}))'
    bot_r["text"] = expressao

csch1 = Button(janela, text = "csch", height = altura, width = largura, command = csch, background = background)
csch1.grid(column = 2, row = 20, padx = padx , pady = pady)




def cot():
    global expressao
    global expressao2
    global numero
    expressao = f'1 / (tan(radians({numero})))'
    expressao2 = f'1 / (tan(radians({numero})))'
    bot_r["text"] = expressao

cot1 = Button(janela, text = "cot", height = altura, width = largura, command = cot, background = background)
cot1.grid(column = 3, row = 8, padx = padx , pady = pady)




def coth():
    global expressao
    global expressao2
    global numero
    expressao = f'1 / (tanh({numero}))'
    expressao2 = f'1 / (tanh({numero}))'
    bot_r["text"] = expressao

coth1 = Button(janela, text = "coth", height = altura, width = largura, command = coth, background = background)
coth1.grid(column = 3, row = 20, padx = padx , pady = pady)




def deg1():
    global expressao
    global expressao2
    global numero
    expressao = f'degrees({numero})'
    expressao2 = f'degrees({numero})'
    bot_r["text"] = expressao

deeg1 = Button(janela, text = "deg", height = altura, width = largura, command = deg1, background = background)
deeg1.grid(column = 6, row = 3, padx = padx, pady = pady)




def rad1():
    global expressao
    global expressao2
    global numero
    expressao = f'radians({numero})'
    expressao2 = f'radians({numero})'
    bot_r["text"] = expressao

raad1 = Button(janela, text = "rad", height = altura, width = largura, command = rad1, background = background)
raad1.grid(column = 7, row = 3, padx = padx, pady = pady)




def rand1():
    global expressao
    global expressao2
    global numero
    global contador
    x = uniform(0, 1)
    contador += 1
    if contador == 1:
        text = expressao
        expressao = ""
        expressao2 = ""
        expressao = f'{text}{x}'
        expressao2 = f'{text}{x}'
    else:
        expressao = ""
        expressao2 = ""
        expressao = f'{x}'
        expressao2 = f'{x}'

    bot_r["text"] = expressao

exp11 = Button(janela, text = 'rand', height = altura, width = largura, command = rand1, background = background)
exp11.grid(column = 2, row = 2, padx = padx, pady = pady )




def exp1():
    global expressao
    global expressao2
    global numero
    expressao2 = f'{numero}*10**'
    expressao = f'{numero}*10**'
    bot_r["text"] = expressao

exp11 = Button(janela, text = 'exp', height = altura, width = largura, command = exp1, background = background)
exp11.grid(column = 1, row = 5, padx = padx, pady = pady )




def logg10():
    global expressao
    global expressao2
    global numero
    expressao = expressao[:-len(numero)]
    expressao2 = expressao2[:-len(numero)]
    expressao2 += f"log10({numero})"
    expressao += f"log10({numero})"
    bot_r["text"] = expressao

log1 = Button(janela, text = "log", height = altura, width = largura, command = logg10, background = background)
log1.grid(column = 1, row = 6, padx = padx, pady = pady)




def logg():
    global expressao
    global expressao2
    global numero
    expressao = expressao[:-len(numero)]
    expressao2 = expressao2[:-len(numero)]
    expressao2 += f"log({numero}, "
    expressao += f"log({numero}, "
    bot_r["text"] = expressao

log1 = Button(janela, text = "log-y^x", height = altura, width = largura, command = logg, background = background)
log1.grid(column = 2, row = 6, padx = padx, pady = pady)




def ln1():
    global expressao
    global expressao2
    global numero
    expressao = expressao[:-len(numero)]
    expressao2 = expressao2[:-len(numero)]
    expressao2 += f"log({numero}, e)"
    expressao += f"log({numero}, e)"
    bot_r["text"] = expressao

lnn1 = Button(janela, text = "ln", height = altura, width = largura, command = ln1, background = background)
lnn1.grid(column = 3, row = 6, padx = padx, pady = pady)




def ex():
    global expressao
    global expressao2
    global numero
    expressao = expressao[:-len(numero)]
    expressao2 = expressao2[:-len(numero)]
    expressao2 += f"(e**{numero})"
    expressao += f"(e**{numero})"
    bot_r["text"] = expressao

ex1 = Button(janela, text = "e^x", height = altura, width = largura, command = ex, background = background)
ex1.grid(column = 2, row = 5, padx = padx, pady = pady)




def va():
    global expressao
    global expressao2
    global numero
    expressao2 = f"abs({numero})"
    expressao = f"abs({numero})"
    bot_r["text"] = expressao

va1 = Button(janela, text = "|x|", height = altura, width = largura, command = va, background = background)
va1.grid(column = 3, row = 5, padx = padx, pady = pady)




def vn():
    global expressao
    global expressao2
    global numero
    expressao2 = f"floor({numero})"
    expressao = f"floor({numero})"
    bot_r["text"] = expressao

va1 = Button(janela, text = "⌊x⌋", height = altura, width = largura, command = vn, background = background)
va1.grid(column = 4, row = 5, padx = padx, pady = pady)




def vt():
    global expressao
    global expressao2
    global numero
    expressao2 = f"ceil({numero})"
    expressao = f"ceil({numero})"
    bot_r["text"] = expressao

va1 = Button(janela, text = "⌈x⌉", height = altura, width = largura, command = vt, background = background)
va1.grid(column = 5, row = 5, padx = padx, pady = pady)




def pdois():
    global expressao
    global expressao2
    global numero
    expressao = expressao[:-len(numero)]
    expressao2 = expressao2[:-len(numero)]
    expressao += f'(2**{numero})'
    expressao2 += f'(2**{numero})'
    bot_r['text'] = expressao

pdois1 = Button(janela, text = "2^x", height = altura, width = largura, command = pdois, background = background)
pdois1.grid(column = 4, row = 4, padx = padx, pady = pady)




def rn():
    global expressao
    global expressao2
    expressao += '**(1/'
    expressao2 += '**(1/'
    bot_r["text"] = expressao

rn1 = Button(janela, text = "y√", height = altura, width = largura, command = rn, background = background)
rn1.grid(column = 1, row = 2, padx = padx, pady = pady)




def botsoma():
    global expressao
    global expressao2
    global numero
    global numero2
    numero2 = ""
    expressao2 += "+"
    numero = ""
    expressao += "+"
    bot_r["text"] = expressao

soma = Button(janela, text = "+", height = altura, width = largura, command = botsoma, background = background)
soma.grid(column = 7, row = 9, padx = padx, pady = pady)




def botsub():
    global expressao
    global numero
    global expressao2
    global numero2
    numero2 = ""
    expressao2 += "-"
    numero = ""
    expressao += "-"
    bot_r["text"] = expressao

sub = Button(janela, text = "-", height = altura, width = largura, command = botsub, background = background)
sub.grid(column = 7, row = 8, padx = padx, pady = pady)




def botmult():
    global expressao
    global numero
    global expressao2
    global numero2
    numero2 = ""
    expressao2 += "*"
    numero = ""
    expressao += "*"
    bot_r["text"] = expressao

mult = Button(janela, text = "*", height = altura, width = largura, command = botmult, background = background)
mult.grid(column = 7, row = 7, padx = padx, pady = pady)




def botdiv():
    global expressao
    global expressao2
    global numero
    global numero2
    numero2 = ""
    expressao2 += "/"
    numero = ""
    expressao += "/"
    bot_r["text"] = expressao

div = Button(janela, text = "/", height = altura, width = largura, command = botdiv, background = background)
div.grid(column = 7, row = 6, padx = padx, pady = pady)




def rq():
    global expressao
    global expressao2
    global numero
    global numero2
    numero2 = ""
    expressao2 += "**0.5"
    numero = ""
    expressao += "**0.5"
    bot_r["text"] = expressao

rq1 = Button(janela, text = "²√", height = altura, width = largura, command = rq, background = background)
rq1.grid(column = 1, row = 3, padx = padx, pady = pady)




def rc():
    global expressao
    global expressao2
    global numero
    global numero2
    numero2 = ""
    expressao2 += "**(1/3)"
    numero = ""
    expressao += "**(1/3)"
    bot_r["text"] = expressao

rc1 = Button(janela, text = "³√", height = altura, width = largura, command = rc, background = background)
rc1.grid(column = 2, row = 3, padx = padx, pady = pady)




def poc():
    global expressao
    global expressao2
    global numero
    global numero2
    expressao = expressao[:-len(numero)]
    expressao2 = expressao2[:-len(numero)]
    expressao2 += f"({numero}/100)"
    expressao += f"({numero}/100)"
    numero2 = ""
    numero = ""
    bot_r["text"] = expressao

poc1 = Button(janela, text = "%", height = altura, width = largura, command = poc, background = background)
poc1.grid(column = 6, row = 4, padx = padx, pady = pady)




def np():
    global expressao
    global expressao2
    global numero
    global numero2
    global contador

    contador += 1
    provisória = expressao2[:-len(numero)]

    if contador % 2 == 1: # se contador = impar
        expressao3 = ""
        numero = f'(-{numero})'
        expressao3 = f'{provisória}{numero}'
        expressao = expressao3
    else: # se contador = par
        numero = f'{numero2}'
        expressao = expressao2
    bot_r["text"] = expressao

pn = Button(janela, text = "+/-", height = altura, width = largura, command = np, background = background)
pn.grid(column = 4, row = 20, padx = padx, pady = pady)




def pdez():
    global expressao
    global expressao2
    global numero
    expressao = expressao[:-len(numero)]
    expressao2 = expressao2[:-len(numero)]
    expressao2 += f'(10**{numero})'
    expressao += f'(10**{numero})'
    bot_r["text"] = expressao

pde = Button(janela, text = "10^x", height = altura, width = largura, command = pdez, background = background)
pde.grid(column = 5, row = 4, padx = padx, pady = pady)




def pi1():
    global expressao
    global expressao2
    expressao2 += f'{pi}'
    expressao += f'{pi}'
    bot_r["text"] = expressao

pii = Button(janela, text = "π", height = altura, width = largura, command = pi1, background = background)
pii.grid(column = 4, row = 2, padx = padx, pady = pady)




def e1():
    global expressao
    global expressao2
    expressao2 += f'{e}'
    expressao += f'{e}'
    bot_r["text"] = expressao

ee1 = Button(janela, text = "e", height = altura, width = largura, command = e1, background = background)
ee1.grid(column = 5, row = 2, padx = padx, pady = pady)




def t1():
    global expressao
    global expressao2
    expressao2 += f'{tau}'
    expressao += f'{tau}'
    bot_r["text"] = expressao

tt1 = Button(janela, text = "τ", height = altura, width = largura, command = t1, background = background)
tt1.grid(column = 3, row = 2, padx = padx, pady = pady)




def fact1():
    global expressao
    global expressao2
    global numero
    expressao = expressao[:-len(numero)]
    expressao2 = expressao2[:-len(numero)]
    expressao2 += f'factorial({numero})'
    expressao += f'factorial({numero})'
    bot_r["text"] = expressao

fc1 = Button(janela, text = "n!", height = altura, width = largura, command = fact1, background = background)
fc1.grid(column = 6, row = 6, padx = padx, pady = pady)




def p():
    global expressao
    global expressao2
    global numero
    global numero2
    numero2 = ""
    numero = ""
    expressao2 += "**"
    expressao += "**"
    bot_r["text"] = expressao

po = Button(janela, text = "^", height = altura, width = largura, command = p, background = background)
po.grid(column = 6, row = 5, padx = padx, pady = pady)




def aspab():
    global expressao
    global expressao2
    expressao += "("
    expressao2 += "("
    bot_r["text"] = expressao

aspab1 = Button(janela, text = "(", height = altura, width = largura, command = aspab, background = background)
aspab1.grid(column = 4, row = 6, padx = padx, pady = pady)




def aspfe():
    global expressao
    global expressao2
    expressao += ")"
    expressao2 += ")"
    bot_r["text"] = expressao

aspab1 = Button(janela, text = ")", height = altura, width = largura, command = aspfe, background = background)
aspab1.grid(column = 5, row = 6, padx = padx, pady = pady)




def di():
    global expressao
    global expressao2
    global numero
    global numero2
    numero = ""
    numero2 = ""
    expressao2 += "//"
    expressao += "//"
    bot_r["text"] = expressao

di1 = Button(janela, text = "//", height = altura, width = largura, command = di, background = background)
di1.grid(column = 7, row = 5, padx = padx, pady = pady)




def rd():
    global expressao
    global expressao2
    global numero
    global numero2
    numero = ""
    numero2 = ""
    expressao2 += "%"
    expressao += "%"
    bot_r["text"] = expressao

rd1 = Button(janela, text = "mod", height = altura, width = largura, command = rd, background = background)
rd1.grid(column = 7, row = 4, padx = padx, pady = pady)




def nqud():
    global expressao
    global expressao2
    global numero
    expressao = expressao[:-len(numero)]
    expressao2 = expressao2[:-len(numero)]
    expressao1 = f'{numero}*{numero}'
    expressao2 += expressao1
    expressao += expressao1
    bot_r["text"] = expressao

naq = Button(janela, text = "x²", height = altura, width = largura, command = nqud, background = background)
naq.grid(column = 1, row = 4, padx = padx, pady = pady)




def ncub():
    global expressao
    global expressao2
    global numero
    expressao = expressao[:-len(numero)]
    expressao2 = expressao2[:-len(numero)]
    expressao1 = f'{numero}*{numero}*{numero}'
    expressao2 += expressao1
    expressao += expressao1
    bot_r["text"] = expressao

nac = Button(janela, text = "x³", height = altura, width = largura, command = ncub, background = background)
nac.grid(column = 2, row = 4, padx = padx, pady = pady)




def umdiv():
    global expressao
    global expressao2
    global numero
    expressao = expressao[:-len(numero)]
    expressao2 = expressao2[:-len(numero)]
    expressao1 = f'(1/({numero}))'
    expressao2 += expressao1
    expressao += expressao1
    bot_r["text"] = expressao

umd = Button(janela, text = "1/x", height = altura, width = largura, command = umdiv, background = background)
umd.grid(column = 3, row = 4, padx = padx, pady = pady)




def botpont():
    global expressao
    global numero
    global expressao2
    global numero2
    numero2 += "."
    numero += "."
    expressao2 += "."
    expressao += "."
    bot_r["text"] = expressao

pont = Button(janela, text = ",", height = altura, width = largura, command = botpont, background = background)
pont.grid(column = 6, row = 20, padx = padx, pady = pady)




def deletar():
    global expressao
    global expressao2
    expressao2 = expressao2[:-1]
    global numero
    numero = numero[:-1]
    global numero2
    numero2 = numero2[:-1]
    expressao = expressao[:-1]
    bot_r["text"] = expressao

deletar1 = Button(janela, text = "x", height = altura, width = largura, command = deletar, background = background)
deletar1.grid(column = 7, row = 2, padx = padx, pady = pady)




def lempar():
    global expressao
    global numero
    global expressao2
    global numero2
    global contador 
    contador = 0
    numero2 = ""
    expressao2 = ""
    expressao = ""
    numero = ""
    bot_r["text"] = expressao

lempar1 = Button(janela, text = "C", height = altura, width = largura, command = lempar, background = background)
lempar1.grid(column = 6, row = 2, padx = padx, pady = pady)




def botao0():
    global expressao
    global numero
    global expressao2
    global numero2
    numero2 += "0"
    expressao2 += "0"
    numero += "0"
    expressao += "0"
    bot_r["text"] = expressao

bot0 = Button(janela, text = "0", height = altura, width = largura, command = botao0, background = background)
bot0.grid(column = 5, row = 20, padx = padx, pady = pady)




def botao1():
    global expressao
    global numero
    global expressao2
    global numero2
    numero2 += "1"
    expressao2 += "1"
    numero += "1"
    expressao += "1"
    bot_r["text"] = expressao

bot1 = Button(janela, text = "1", height = altura, width = largura, command = botao1, background = background)
bot1.grid(column = 4, row = 9, padx = padx, pady = pady)




def botao2():
    global expressao
    global numero
    global expressao2
    global numero2
    numero2 += "2"
    expressao2 += "2"
    numero += "2"
    expressao += "2"
    bot_r["text"] = expressao

bot2 = Button(janela, text = "2", height = altura, width = largura, command = botao2, background = background)
bot2.grid(column = 5, row = 9, padx = padx, pady = pady)




def botao3():
    global expressao
    global numero
    global expressao2
    global numero2
    numero2 += "3"
    expressao2 += "3"
    numero += "3"
    expressao += "3"
    bot_r["text"] = expressao


bot3 = Button(janela, text = "3", height = altura, width = largura, command = botao3, background = background)
bot3.grid(column = 6, row = 9, padx = padx, pady = pady)




def botao4():
    global expressao
    global numero
    global expressao2
    global numero2
    numero2 += "4"
    expressao2 += "4"
    numero += "4"
    expressao += "4"
    bot_r["text"] = expressao

bot4 = Button(janela, text = "4", height = altura, width = largura, command = botao4, background = background)
bot4.grid(column = 4, row = 8, padx = padx, pady = pady)




def botao5():
    global expressao
    global numero
    global expressao2
    global numero2
    numero2 += "5"
    expressao2 += "5"
    numero += "5"
    expressao += "5"
    bot_r["text"] = expressao

bot5 = Button(janela, text = "5", height = altura, width = largura, command = botao5, background = background)
bot5.grid(column = 5, row = 8, padx = padx, pady = pady)




def batao6():
    global expressao
    global numero
    global expressao2
    global numero2
    numero2 += "6"
    expressao2 += "6"
    numero += "6"
    expressao += "6"
    bot_r["text"] = expressao

bot6 = Button(janela, text = "6", height = altura, width = largura, command = batao6, background = background)
bot6.grid(column = 6, row = 8, padx = padx, pady = pady)




def botao7():
    global expressao
    global numero
    global expressao2
    global numero2
    numero2 += "7"
    expressao2 += "7"
    numero += "7"
    expressao += "7"
    bot_r["text"] = expressao

bot7 = Button(janela, text = "7", height = altura, width = largura, command = botao7, background = background)
bot7.grid(column = 4, row = 7, padx = padx, pady = pady)




def botao8():
    global expressao
    global numero
    global expressao2
    global numero2
    numero2 += "8"
    expressao2 += "8"
    numero += "8"
    expressao += "8"
    bot_r["text"] = expressao

bot8 = Button(janela, text = "8", height = altura, width = largura, command = botao8, background = background)
bot8.grid(column = 5, row = 7, padx = padx, pady = pady)




def botao9():
    global expressao
    global numero
    global expressao2
    global numero2
    numero2 += "9"
    expressao2 += "9"
    numero += "9"
    expressao += "9"
    bot_r["text"] = expressao

bot9 = Button(janela, text = "9", height = altura, width = largura, command = botao9, background = background)
bot9.grid(column = 6, row = 7, padx = padx, pady = pady)




janela.mainloop()
