from tkinter import *
from path.funções import *
texto1 = ""

def help1():
    global contador1, contador2, contador3, contador4, contador5, contador6, contador7
    contador1 = 0
    contador2 = 0
    contador3 = 0
    contador4 = 0
    contador5 = 0
    contador6 = 0
    contador7 = 0
    helptab1 = Tk()
    helptab1.geometry("540x600")
    helptab1.title("HELP-TAB (1 de 9)")
    helptab1.config(background = "#404040")
    texto = Label(helptab1, text= "Sistema De Ajuda", background = "#404040")
    texto.grid(column = 0, row = 0, padx = 105, pady = 25)
    
    texto1 = "                                                                                                       "
    texto = Label(helptab1, text = texto1, background = "#404040")
    texto.grid(column = 0, row = 2, padx = 105, pady = 5)
    
    def textof():
        global texto1
        global contador1
        contador1 += 1
        if contador1 % 2 == 1: # se contador = impar
            texto1 = "Botão usado para raiz de um número x a outro número y"
            texto = Label(helptab1, text = texto1, background = "#404040")
            texto.grid(column = 0, row = 2, padx = 105, pady = 5)
        else:
            texto1 = "                                                                                                       "
            texto = Label(helptab1, text = texto1, background = "#404040")
            texto.grid(column = 0, row = 2, padx = 105, pady = 5)

    bot_1 = Button(helptab1, text = "⇓                  y√                  ⇓", height = altura, width = 20, command = textof, background = background)
    bot_1.grid(column = 0, row = 1, padx = 105, pady = 5)


    texto1 = "                                                                                                       "
    texto = Label(helptab1, text = texto1, background = "#404040")
    texto.grid(column = 0, row = 4, padx = 105, pady = 5)

    def textog():
        global texto1
        global contador2
        contador2 += 1
        if contador2 % 2 == 1: # se contador = impar
            texto1 = "Gera um número aleatório entre 0 e 0.999....."
            texto = Label(helptab1, text = texto1, background = "#404040")
            texto.grid(column = 0, row = 4, padx = 105, pady = 5)
        else:
            texto1 = "                                                                                                       "
            texto = Label(helptab1, text = texto1, background = "#404040")
            texto.grid(column = 0, row = 4, padx = 105, pady = 5)
    
    bot_1 = Button(helptab1, text = "⇓                 rand                 ⇓", height = altura, width = 20, command = textog, background = background)
    bot_1.grid(column = 0, row = 3, padx = 105, pady = 5)


    texto1 = "                                                                                                       "
    texto = Label(helptab1, text = texto1, background = "#404040")
    texto.grid(column = 0, row = 6, padx = 105, pady = 5)

    def tau():
        global texto1
        global contador3
        contador3 += 1
        if contador3 % 2 == 1: # se contador = impar
            texto1 = "Usado para gerar o valor de Tau (τ)"
            texto = Label(helptab1, text = texto1, background = "#404040")
            texto.grid(column = 0, row = 6, padx = 105, pady = 5)
        else:
            texto1 = "                                                                                                       "
            texto = Label(helptab1, text = texto1, background = "#404040")
            texto.grid(column = 0, row = 6, padx = 105, pady = 5)
    
    bot_1 = Button(helptab1, text = "⇓                   τ                  ⇓", height = altura, width = 20, command = tau, background = background)
    bot_1.grid(column = 0, row = 5, padx = 105, pady = 5)



    texto1 = "                                                                                                       "
    texto = Label(helptab1, text = texto1, background = "#404040")
    texto.grid(column = 0, row = 8, padx = 105, pady = 5)

    def pi():
        global texto1
        global contador4
        contador4 += 1
        if contador4 % 2 == 1: # se contador = impar
            texto1 = "Usado para gerar o valor de pi (π)"
            texto = Label(helptab1, text = texto1, background = "#404040")
            texto.grid(column = 0, row = 8, padx = 105, pady = 5)
        else:
            texto1 = "                                                                                                       "
            texto = Label(helptab1, text = texto1, background = "#404040")
            texto.grid(column = 0, row = 8, padx = 105, pady = 5)
    
    bot_1 = Button(helptab1, text = "⇓                   π                  ⇓", height = altura, width = 20, command = pi, background = background)
    bot_1.grid(column = 0, row = 7, padx = 105, pady = 5)



    texto1 = "                                                                                                       "
    texto = Label(helptab1, text = texto1, background = "#404040")
    texto.grid(column = 0, row = 10, padx = 105, pady = 5)

    def e():
        global texto1
        global contador5
        contador5 += 1
        if contador5 % 2 == 1: # se contador = impar
            texto1 = "Usado para gerar o valor de Euler(e)"
            texto = Label(helptab1, text = texto1, background = "#404040")
            texto.grid(column = 0, row = 10, padx = 105, pady = 5)
        else:
            texto1 = "                                                                                                       "
            texto = Label(helptab1, text = texto1, background = "#404040")
            texto.grid(column = 0, row = 10, padx = 105, pady = 5)
    
    bot_1 = Button(helptab1, text = "⇓                   e                  ⇓", height = altura, width = 20, command = e, background = background)
    bot_1.grid(column = 0, row = 9, padx = 105, pady = 5)



    texto1 = "                                                                                                       "
    texto = Label(helptab1, text = texto1, background = "#404040")
    texto.grid(column = 0, row = 12, padx = 105, pady = 5)

    def C():
        global texto1
        global contador6
        contador6 += 1
        if contador6 % 2 == 1: # se contador = impar
            texto1 = "Usado para limpar o visor"
            texto = Label(helptab1, text = texto1, background = "#404040")
            texto.grid(column = 0, row = 12, padx = 105, pady = 5)
        else:
            texto1 = "                                                                                                       "
            texto = Label(helptab1, text = texto1, background = "#404040")
            texto.grid(column = 0, row = 12, padx = 105, pady = 5)
    
    bot_1 = Button(helptab1, text = "⇓                   C                  ⇓", height = altura, width = 20, command = C, background = background)
    bot_1.grid(column = 0, row = 11, padx = 105, pady = 5)



    texto1 = "                                                                                                       "
    texto = Label(helptab1, text = texto1, background = "#404040")
    texto.grid(column = 0, row = 14, padx = 105, pady = 5)

    def X():
        global texto1
        global contador7
        contador7 += 1
        if contador7 % 2 == 1: # se contador = impar
            texto1 = "Usado para remover o último digito no visor"
            texto = Label(helptab1, text = texto1, background = "#404040")
            texto.grid(column = 0, row = 14, padx = 105, pady = 5)
        else:
            texto1 = "                                                                                                       "
            texto = Label(helptab1, text = texto1, background = "#404040")
            texto.grid(column = 0, row = 14, padx = 105, pady = 5)
    
    bot_1 = Button(helptab1, text = "⇓                   x                  ⇓", height = altura, width = 20, command = X, background = background)
    bot_1.grid(column = 0, row = 13, padx = 105, pady = 5)



    def pp(): # pagina 2
        global contador8, contador9, contador10, contador11, contador12, contador13, contador14
        contador8  = 0
        contador9  = 0
        contador10 = 0
        contador11 = 0
        contador12 = 0
        contador13 = 0
        contador14 = 0
        helptab2 = Tk()
        helptab2.geometry("540x600")
        helptab2.title("HELP-TAB (2 de 9)")
        helptab2.config(background = "#404040")
        texto = Label(helptab2, text= "Sistema De Ajuda", background = "#404040")
        texto.grid(column = 0, row = 0, padx = 105, pady = 25)
    
        texto1 = "                                                                                                       "
        texto = Label(helptab2, text = texto1, background = "#404040")
        texto.grid(column = 0, row = 2, padx = 105, pady = 5) 

        def rq():
            global texto1
            global contador8
            contador8 += 1
            if contador8 % 2 == 1: # se contador = impar
                texto1 = "Raiz quadrada de um número x"
                texto = Label(helptab2, text = texto1, background = "#404040")
                texto.grid(column = 0, row = 2, padx = 105, pady = 5)
            else:
                texto1 = "                                                                                                       "
                texto = Label(helptab2, text = texto1, background = "#404040")
                texto.grid(column = 0, row = 2, padx = 105, pady = 5)
    
        bot_1 = Button(helptab2, text = "⇓                   ²√                 ⇓", height = altura, width = 20, command = rq, background = background)
        bot_1.grid(column = 0, row = 1, padx = 105, pady = 5)



        texto1 = "                                                                                                       "
        texto = Label(helptab2, text = texto1, background = "#404040")
        texto.grid(column = 0, row = 4, padx = 105, pady = 5) 

        def rc():
            global texto1
            global contador9
            contador9 += 1
            if contador9 % 2 == 1: # se contador = impar
                texto1 = "Raiz cúbica de um número x"
                texto = Label(helptab2, text = texto1, background = "#404040")
                texto.grid(column = 0, row = 4, padx = 105, pady = 5)
            else:
                texto1 = "                                                                                                       "
                texto = Label(helptab2, text = texto1, background = "#404040")
                texto.grid(column = 0, row = 4, padx = 105, pady = 5)
    
        bot_1 = Button(helptab2, text = "⇓                   ³√                 ⇓", height = altura, width = 20, command = rc, background = background)
        bot_1.grid(column = 0, row = 3, padx = 105, pady = 5)
        


        texto1 = "                                                                                                       "
        texto = Label(helptab2, text = texto1, background = "#404040")
        texto.grid(column = 0, row = 6, padx = 105, pady = 5) 

        def bin():
            global texto1
            global contador10
            contador10 += 1
            if contador10 % 2 == 1: # se contador = impar
                texto1 = "Número decimal em Binário"
                texto = Label(helptab2, text = texto1, background = "#404040")
                texto.grid(column = 0, row = 6, padx = 105, pady = 5)
            else:
                texto1 = "                                                                                                       "
                texto = Label(helptab2, text = texto1, background = "#404040")
                texto.grid(column = 0, row = 6, padx = 105, pady = 5)
    
        bot_1 = Button(helptab2, text = "⇓                  BIN                 ⇓", height = altura, width = 20, command = bin, background = background)
        bot_1.grid(column = 0, row = 5, padx = 105, pady = 5)
        


        texto1 = "                                                                                                       "
        texto = Label(helptab2, text = texto1, background = "#404040")
        texto.grid(column = 0, row = 8, padx = 105, pady = 5) 

        def oct():
            global texto1
            global contador11
            contador11 += 1
            if contador11 % 2 == 1: # se contador = impar
                texto1 = "Número decimal em Octal"
                texto = Label(helptab2, text = texto1, background = "#404040")
                texto.grid(column = 0, row = 8, padx = 105, pady = 5)
            else:
                texto1 = "                                                                                                       "
                texto = Label(helptab2, text = texto1, background = "#404040")
                texto.grid(column = 0, row = 8, padx = 105, pady = 5)
    
        bot_1 = Button(helptab2, text = "⇓                  OCT                 ⇓", height = altura, width = 20, command = oct, background = background)
        bot_1.grid(column = 0, row = 7, padx = 105, pady = 5)



        texto1 = "                                                                                                       "
        texto = Label(helptab2, text = texto1, background = "#404040")
        texto.grid(column = 0, row = 10, padx = 105, pady = 5) 

        def hex():
            global texto1
            global contador12
            contador12 += 1
            if contador12 % 2 == 1: # se contador = impar
                texto1 = "Número decimal em Hexadecimal"
                texto = Label(helptab2, text = texto1, background = "#404040")
                texto.grid(column = 0, row = 10, padx = 105, pady = 5)
            else:
                texto1 = "                                                                                                       "
                texto = Label(helptab2, text = texto1, background = "#404040")
                texto.grid(column = 0, row = 10, padx = 105, pady = 5)
    
        bot_1 = Button(helptab2, text = "⇓                  HEX                 ⇓", height = altura, width = 20, command = hex, background = background)
        bot_1.grid(column = 0, row = 9, padx = 105, pady = 5)



        texto1 = "                                                                                                       "
        texto = Label(helptab2, text = texto1, background = "#404040")
        texto.grid(column = 0, row = 12, padx = 105, pady = 5) 

        def deg():
            global texto1
            global contador13
            contador13 += 1
            if contador13 % 2 == 1: # se contador = impar
                texto1 = "Converter para grados"
                texto = Label(helptab2, text = texto1, background = "#404040")
                texto.grid(column = 0, row = 12, padx = 105, pady = 5)
            else:
                texto1 = "                                                                                                       "
                texto = Label(helptab2, text = texto1, background = "#404040")
                texto.grid(column = 0, row = 12, padx = 105, pady = 5)
    
        bot_1 = Button(helptab2, text = "⇓                  deg                 ⇓", height = altura, width = 20, command = deg, background = background)
        bot_1.grid(column = 0, row = 11, padx = 105, pady = 5)



        texto1 = "                                                                                                       "
        texto = Label(helptab2, text = texto1, background = "#404040")
        texto.grid(column = 0, row = 14, padx = 105, pady = 5) 

        def rad():
            global texto1
            global contador14
            contador14 += 1
            if contador14 % 2 == 1: # se contador = impar
                texto1 = "Converter para radianos"
                texto = Label(helptab2, text = texto1, background = "#404040")
                texto.grid(column = 0, row = 14, padx = 105, pady = 5)
            else:
                texto1 = "                                                                                                       "
                texto = Label(helptab2, text = texto1, background = "#404040")
                texto.grid(column = 0, row = 14, padx = 105, pady = 5)
    
        bot_1 = Button(helptab2, text = "⇓                  rad                 ⇓", height = altura, width = 20, command = rad, background = background)
        bot_1.grid(column = 0, row = 13, padx = 105, pady = 5)



        def pp(): # pagina 3
            global contador15, contador16, contador17, contador18, contador19, contador20, contador21
            contador15 = 0
            contador16 = 0
            contador17 = 0
            contador18 = 0
            contador19 = 0
            contador20 = 0
            contador21 = 0
            helptab3 = Tk()
            helptab3.geometry("540x600")
            helptab3.title("HELP-TAB (3 de 9)")
            helptab3.config(background = "#404040")
            texto = Label(helptab3, text= "Sistema De Ajuda", background = "#404040")
            texto.grid(column = 0, row = 0, padx = 105, pady = 25)



            texto1 = "                                                                                                       "
            texto = Label(helptab3, text = texto1, background = "#404040")
            texto.grid(column = 0, row = 2, padx = 105, pady = 5) 

            def x2():
                global texto1
                global contador15
                contador15 += 1
                if contador15 % 2 == 1: # se contador = impar
                    texto1 = "Número ao quadrado"
                    texto = Label(helptab3, text = texto1, background = "#404040")
                    texto.grid(column = 0, row = 2, padx = 105, pady = 5)
                else:
                    texto1 = "                                                                                                       "
                    texto = Label(helptab3, text = texto1, background = "#404040")
                    texto.grid(column = 0, row = 2, padx = 105, pady = 5)
        
            bot_1 = Button(helptab3, text = "⇓                   x²                 ⇓", height = altura, width = 20, command = x2, background = background)
            bot_1.grid(column = 0, row = 1, padx = 105, pady = 5)



            texto1 = "                                                                                                       "
            texto = Label(helptab3, text = texto1, background = "#404040")
            texto.grid(column = 0, row = 4, padx = 105, pady = 5) 

            def x3():
                global texto1
                global contador16
                contador16 += 1
                if contador16 % 2 == 1: # se contador = impar
                    texto1 = "Número ao cubo"
                    texto = Label(helptab3, text = texto1, background = "#404040")
                    texto.grid(column = 0, row = 4, padx = 105, pady = 5)
                else:
                    texto1 = "                                                                                                       "
                    texto = Label(helptab3, text = texto1, background = "#404040")
                    texto.grid(column = 0, row = 4, padx = 105, pady = 5)
        
            bot_1 = Button(helptab3, text = "⇓                   x³                 ⇓", height = altura, width = 20, command = x3, background = background)
            bot_1.grid(column = 0, row = 3, padx = 105, pady = 5)



            texto1 = "                                                                                                       "
            texto = Label(helptab3, text = texto1, background = "#404040")
            texto.grid(column = 0, row = 6, padx = 105, pady = 5) 

            def dx():
                global texto1
                global contador17
                contador17 += 1
                if contador17 % 2 == 1: # se contador = impar
                    texto1 = "1 dividido por x"
                    texto = Label(helptab3, text = texto1, background = "#404040")
                    texto.grid(column = 0, row = 6, padx = 105, pady = 5)
                else:
                    texto1 = "                                                                                                       "
                    texto = Label(helptab3, text = texto1, background = "#404040")
                    texto.grid(column = 0, row = 6, padx = 105, pady = 5)
        
            bot_1 = Button(helptab3, text = "⇓                  1/x                 ⇓", height = altura, width = 20, command = dx, background = background)
            bot_1.grid(column = 0, row = 5, padx = 105, pady = 5)



            texto1 = "                                                                                                       "
            texto = Label(helptab3, text = texto1, background = "#404040")
            texto.grid(column = 0, row = 8, padx = 105, pady = 5) 

            def dsx():
                global texto1
                global contador18
                contador18 += 1
                if contador18 % 2 == 1: # se contador = impar
                    texto1 = "2 sobre x"
                    texto = Label(helptab3, text = texto1, background = "#404040")
                    texto.grid(column = 0, row = 8, padx = 105, pady = 5)
                else:
                    texto1 = "                                                                                                       "
                    texto = Label(helptab3, text = texto1, background = "#404040")
                    texto.grid(column = 0, row = 8, padx = 105, pady = 5)
        
            bot_1 = Button(helptab3, text = "⇓                  2^x                 ⇓", height = altura, width = 20, command = dsx, background = background)
            bot_1.grid(column = 0, row = 7, padx = 105, pady = 5)



            texto1 = "                                                                                                       "
            texto = Label(helptab3, text = texto1, background = "#404040")
            texto.grid(column = 0, row = 10, padx = 105, pady = 5) 

            def dezsx():
                global texto1
                global contador19
                contador19 += 1
                if contador19 % 2 == 1: # se contador = impar
                    texto1 = "10 sobre x"
                    texto = Label(helptab3, text = texto1, background = "#404040")
                    texto.grid(column = 0, row = 10, padx = 105, pady = 5)
                else:
                    texto1 = "                                                                                                       "
                    texto = Label(helptab3, text = texto1, background = "#404040")
                    texto.grid(column = 0, row = 10, padx = 105, pady = 5)
        
            bot_1 = Button(helptab3, text = "⇓                  10^x                ⇓", height = altura, width = 20, command = dezsx, background = background)
            bot_1.grid(column = 0, row = 9, padx = 105, pady = 5)



            texto1 = "                                                                                                       "
            texto = Label(helptab3, text = texto1, background = "#404040")
            texto.grid(column = 0, row = 12, padx = 105, pady = 5) 

            def porcento():
                global texto1
                global contador20
                contador20 += 1
                if contador20 % 2 == 1: # se contador = impar
                    texto1 = "Número porcento"
                    texto = Label(helptab3, text = texto1, background = "#404040")
                    texto.grid(column = 0, row = 12, padx = 105, pady = 5)
                else:
                    texto1 = "                                                                                                       "
                    texto = Label(helptab3, text = texto1, background = "#404040")
                    texto.grid(column = 0, row = 12, padx = 105, pady = 5)
        
            bot_1 = Button(helptab3, text = "⇓                    %                 ⇓", height = altura, width = 20, command = porcento, background = background)
            bot_1.grid(column = 0, row = 11, padx = 105, pady = 5)



            texto1 = "                                                                                                       "
            texto = Label(helptab3, text = texto1, background = "#404040")
            texto.grid(column = 0, row = 14, padx = 105, pady = 5) 

            def mod():
                global texto1
                global contador21
                contador21 += 1
                if contador21 % 2 == 1: # se contador = impar
                    texto1 = "Resto da divisão entre x e y"
                    texto = Label(helptab3, text = texto1, background = "#404040")
                    texto.grid(column = 0, row = 14, padx = 105, pady = 5)
                else:
                    texto1 = "                                                                                                       "
                    texto = Label(helptab3, text = texto1, background = "#404040")
                    texto.grid(column = 0, row = 14, padx = 105, pady = 5)
        
            bot_1 = Button(helptab3, text = "⇓                   mod                ⇓", height = altura, width = 20, command = mod, background = background)
            bot_1.grid(column = 0, row = 13, padx = 105, pady = 5)




            def pp(): # pagina 4
                global contador22, contador23, contador24, contador25, contador26, contador27, contador28
                contador22 = 0
                contador23 = 0
                contador24 = 0
                contador25 = 0
                contador26 = 0
                contador27 = 0
                contador28 = 0
                helptab4 = Tk()
                helptab4.geometry("540x600")
                helptab4.title("HELP-TAB (4 de 9)")
                helptab4.config(background = "#404040")
                texto = Label(helptab4, text= "Sistema De Ajuda", background = "#404040")
                texto.grid(column = 0, row = 0, padx = 105, pady = 25)



                texto1 = "                                                                                                       "
                texto = Label(helptab4, text = texto1, background = "#404040")
                texto.grid(column = 0, row = 2, padx = 105, pady = 5) 

                def exp():
                    global texto1
                    global contador22
                    contador22 += 1
                    if contador22 % 2 == 1: # se contador = impar
                        texto1 = "x vezes 10 elevado a y (exponencial)"
                        texto = Label(helptab4, text = texto1, background = "#404040")
                        texto.grid(column = 0, row = 2, padx = 105, pady = 5)
                    else:
                        texto1 = "                                                                                                       "
                        texto = Label(helptab4, text = texto1, background = "#404040")
                        texto.grid(column = 0, row = 2, padx = 105, pady = 5)
            
                bot_1 = Button(helptab4, text = "⇓                   exp                ⇓", height = altura, width = 20, command = exp, background = background)
                bot_1.grid(column = 0, row = 1, padx = 105, pady = 5)



                texto1 = "                                                                                                       "
                texto = Label(helptab4, text = texto1, background = "#404040")
                texto.grid(column = 0, row = 4, padx = 105, pady = 5) 

                def e():
                    global texto1
                    global contador23
                    contador23 += 1
                    if contador23 % 2 == 1: # se contador = impar
                        texto1 = "e elevado a x"
                        texto = Label(helptab4, text = texto1, background = "#404040")
                        texto.grid(column = 0, row = 4, padx = 105, pady = 5)
                    else:
                        texto1 = "                                                                                                       "
                        texto = Label(helptab4, text = texto1, background = "#404040")
                        texto.grid(column = 0, row = 4, padx = 105, pady = 5)
            
                bot_1 = Button(helptab4, text = "⇓                   e^x                ⇓", height = altura, width = 20, command = e, background = background)
                bot_1.grid(column = 0, row = 3, padx = 105, pady = 5)



                texto1 = "                                                                                                       "
                texto = Label(helptab4, text = texto1, background = "#404040")
                texto.grid(column = 0, row = 6, padx = 105, pady = 5) 

                def abs():
                    global texto1
                    global contador24
                    contador24 += 1
                    if contador24 % 2 == 1: # se contador = impar
                        texto1 = "Valor absoluto (abs)"
                        texto = Label(helptab4, text = texto1, background = "#404040")
                        texto.grid(column = 0, row = 6, padx = 105, pady = 5)
                    else:
                        texto1 = "                                                                                                       "
                        texto = Label(helptab4, text = texto1, background = "#404040")
                        texto.grid(column = 0, row = 6, padx = 105, pady = 5)
            
                bot_1 = Button(helptab4, text = "⇓                   |x|                ⇓", height = altura, width = 20, command = abs, background = background)
                bot_1.grid(column = 0, row = 5, padx = 105, pady = 5)                



                texto1 = "                                                                                                       "
                texto = Label(helptab4, text = texto1, background = "#404040")
                texto.grid(column = 0, row = 8, padx = 105, pady = 5) 

                def piso():
                    global texto1
                    global contador25
                    contador25 += 1
                    if contador25 % 2 == 1: # se contador = impar
                        texto1 = "Piso de um número (Floor)"
                        texto = Label(helptab4, text = texto1, background = "#404040")
                        texto.grid(column = 0, row = 8, padx = 105, pady = 5)
                    else:
                        texto1 = "                                                                                                       "
                        texto = Label(helptab4, text = texto1, background = "#404040")
                        texto.grid(column = 0, row = 8, padx = 105, pady = 5)
            
                bot_1 = Button(helptab4, text = "⇓                   ⌊x⌋                ⇓", height = altura, width = 20, command = piso, background = background)
                bot_1.grid(column = 0, row = 7, padx = 105, pady = 5) 



                texto1 = "                                                                                                       "
                texto = Label(helptab4, text = texto1, background = "#404040")
                texto.grid(column = 0, row = 10, padx = 105, pady = 5) 

                def teto():
                    global texto1
                    global contador26
                    contador26 += 1
                    if contador26 % 2 == 1: # se contador = impar
                        texto1 = "Teto de um número (Ceiling)"
                        texto = Label(helptab4, text = texto1, background = "#404040")
                        texto.grid(column = 0, row = 10, padx = 105, pady = 5)
                    else:
                        texto1 = "                                                                                                       "
                        texto = Label(helptab4, text = texto1, background = "#404040")
                        texto.grid(column = 0, row = 10, padx = 105, pady = 5)
            
                bot_1 = Button(helptab4, text = "⇓                   ⌈x⌉                ⇓", height = altura, width = 20, command = teto, background = background)
                bot_1.grid(column = 0, row = 9, padx = 105, pady = 5)



                texto1 = "                                                                                                       "
                texto = Label(helptab4, text = texto1, background = "#404040")
                texto.grid(column = 0, row = 12, padx = 105, pady = 5) 

                def potencia():
                    global texto1
                    global contador27
                    contador27 += 1
                    if contador27 % 2 == 1: # se contador = impar
                        texto1 = "x pelo expoente y"
                        texto = Label(helptab4, text = texto1, background = "#404040")
                        texto.grid(column = 0, row = 12, padx = 105, pady = 5)
                    else:
                        texto1 = "                                                                                                       "
                        texto = Label(helptab4, text = texto1, background = "#404040")
                        texto.grid(column = 0, row = 12, padx = 105, pady = 5)
            
                bot_1 = Button(helptab4, text = "⇓                    ^                 ⇓", height = altura, width = 20, command = potencia, background = background)
                bot_1.grid(column = 0, row = 11, padx = 105, pady = 5) 



                texto1 = "                                                                                                       "
                texto = Label(helptab4, text = texto1, background = "#404040")
                texto.grid(column = 0, row = 14, padx = 105, pady = 5) 

                def divinteita():
                    global texto1
                    global contador28
                    contador28 += 1
                    if contador28 % 2 == 1: # se contador = impar
                        texto1 = "Divisão inteira"
                        texto = Label(helptab4, text = texto1, background = "#404040")
                        texto.grid(column = 0, row = 14, padx = 105, pady = 5)
                    else:
                        texto1 = "                                                                                                       "
                        texto = Label(helptab4, text = texto1, background = "#404040")
                        texto.grid(column = 0, row = 14, padx = 105, pady = 5)
            
                bot_1 = Button(helptab4, text = "⇓                   //                 ⇓", height = altura, width = 20, command = divinteita, background = background)
                bot_1.grid(column = 0, row = 13, padx = 105, pady = 5) 



                def pp(): # pagina 5
                    global contador29, contador30, contador31, contador32, contador33, contador34, contador35
                    contador29 = 0
                    contador30 = 0
                    contador31 = 0
                    contador32 = 0
                    contador33 = 0
                    contador34 = 0
                    contador35 = 0
                    helptab5 = Tk()
                    helptab5.geometry("540x600")
                    helptab5.title("HELP-TAB (5 de 9)")
                    helptab5.config(background = "#404040")
                    texto = Label(helptab5, text= "Sistema De Ajuda", background = "#404040")
                    texto.grid(column = 0, row = 0, padx = 105, pady = 25)



                    texto1 = "                                                                                                       "
                    texto = Label(helptab5, text = texto1, background = "#404040")
                    texto.grid(column = 0, row = 2, padx = 105, pady = 5) 

                    def log():
                        global texto1
                        global contador29
                        contador29 += 1
                        if contador29 % 2 == 1: # se contador = impar
                            texto1 = "Logaritimo de x na base 10"
                            texto = Label(helptab5, text = texto1, background = "#404040")
                            texto.grid(column = 0, row = 2, padx = 105, pady = 5)
                        else:
                            texto1 = "                                                                                                       "
                            texto = Label(helptab5, text = texto1, background = "#404040")
                            texto.grid(column = 0, row = 2, padx = 105, pady = 5)
                
                    bot_1 = Button(helptab5, text = "⇓                   log                ⇓", height = altura, width = 20, command = log, background = background)
                    bot_1.grid(column = 0, row = 1, padx = 105, pady = 5) 



                    texto1 = "                                                                                                       "
                    texto = Label(helptab5, text = texto1, background = "#404040")
                    texto.grid(column = 0, row = 4, padx = 105, pady = 5) 

                    def logxy():
                        global texto1
                        global contador30
                        contador30 += 1
                        if contador30 % 2 == 1: # se contador = impar
                            texto1 = "Logaritimo de y na base x"
                            texto = Label(helptab5, text = texto1, background = "#404040")
                            texto.grid(column = 0, row = 4, padx = 105, pady = 5)
                        else:
                            texto1 = "                                                                                                       "
                            texto = Label(helptab5, text = texto1, background = "#404040")
                            texto.grid(column = 0, row = 4, padx = 105, pady = 5)
                
                    bot_1 = Button(helptab5, text = "⇓                log-y^x               ⇓", height = altura, width = 20, command = logxy, background = background)
                    bot_1.grid(column = 0, row = 3, padx = 105, pady = 5) 



                    texto1 = "                                                                                                       "
                    texto = Label(helptab5, text = texto1, background = "#404040")
                    texto.grid(column = 0, row = 6, padx = 105, pady = 5) 

                    def lognatural():
                        global texto1
                        global contador31
                        contador31 += 1
                        if contador31 % 2 == 1: # se contador = impar
                            texto1 = "Logaritimo de e na base x"
                            texto = Label(helptab5, text = texto1, background = "#404040")
                            texto.grid(column = 0, row = 6, padx = 105, pady = 5)
                        else:
                            texto1 = "                                                                                                       "
                            texto = Label(helptab5, text = texto1, background = "#404040")
                            texto.grid(column = 0, row = 6, padx = 105, pady = 5)
                
                    bot_1 = Button(helptab5, text = "⇓                   ln                 ⇓", height = altura, width = 20, command = lognatural, background = background)
                    bot_1.grid(column = 0, row = 5, padx = 105, pady = 5) 



                    texto1 = "                                                                                                       "
                    texto = Label(helptab5, text = texto1, background = "#404040")
                    texto.grid(column = 0, row = 8, padx = 105, pady = 5) 

                    def Aparentese():
                        global texto1
                        global contador32
                        contador32 += 1
                        if contador32 % 2 == 1: # se contador = impar
                            texto1 = "Abrir parênteses"
                            texto = Label(helptab5, text = texto1, background = "#404040")
                            texto.grid(column = 0, row = 8, padx = 105, pady = 5)
                        else:
                            texto1 = "                                                                                                       "
                            texto = Label(helptab5, text = texto1, background = "#404040")
                            texto.grid(column = 0, row = 8, padx = 105, pady = 5)
                
                    bot_1 = Button(helptab5, text = "⇓                    (                 ⇓", height = altura, width = 20, command = Aparentese, background = background)
                    bot_1.grid(column = 0, row = 7, padx = 105, pady = 5) 
                    


                    texto1 = "                                                                                                       "
                    texto = Label(helptab5, text = texto1, background = "#404040")
                    texto.grid(column = 0, row = 10, padx = 105, pady = 5) 

                    def Fparentese():
                        global texto1
                        global contador33
                        contador33 += 1
                        if contador33 % 2 == 1: # se contador = impar
                            texto1 = "Fechar parênteses"
                            texto = Label(helptab5, text = texto1, background = "#404040")
                            texto.grid(column = 0, row = 10, padx = 105, pady = 5)
                        else:
                            texto1 = "                                                                                                       "
                            texto = Label(helptab5, text = texto1, background = "#404040")
                            texto.grid(column = 0, row = 10, padx = 105, pady = 5)
                
                    bot_1 = Button(helptab5, text = "⇓                    )                 ⇓", height = altura, width = 20, command = Fparentese, background = background)
                    bot_1.grid(column = 0, row = 9, padx = 105, pady = 5) 



                    texto1 = "                                                                                                       "
                    texto = Label(helptab5, text = texto1, background = "#404040")
                    texto.grid(column = 0, row = 12, padx = 105, pady = 5) 

                    def fatorial():
                        global texto1
                        global contador34
                        contador34 += 1
                        if contador34 % 2 == 1: # se contador = impar
                            texto1 = "Fatotial"
                            texto = Label(helptab5, text = texto1, background = "#404040")
                            texto.grid(column = 0, row = 12, padx = 105, pady = 5)
                        else:
                            texto1 = "                                                                                                       "
                            texto = Label(helptab5, text = texto1, background = "#404040")
                            texto.grid(column = 0, row = 12, padx = 105, pady = 5)
                
                    bot_1 = Button(helptab5, text = "⇓                  n!                  ⇓", height = altura, width = 20, command = fatorial, background = background)
                    bot_1.grid(column = 0, row = 11, padx = 105, pady = 5) 



                    texto1 = "                                                                                                       "
                    texto = Label(helptab5, text = texto1, background = "#404040")
                    texto.grid(column = 0, row = 14, padx = 105, pady = 5) 

                    def div():
                        global texto1
                        global contador35
                        contador35 += 1
                        if contador35 % 2 == 1: # se contador = impar
                            texto1 = "Divisão"
                            texto = Label(helptab5, text = texto1, background = "#404040")
                            texto.grid(column = 0, row = 14, padx = 105, pady = 5)
                        else:
                            texto1 = "                                                                                                       "
                            texto = Label(helptab5, text = texto1, background = "#404040")
                            texto.grid(column = 0, row = 14, padx = 105, pady = 5)
                
                    bot_1 = Button(helptab5, text = "⇓                   /                  ⇓", height = altura, width = 20, command = div, background = background)
                    bot_1.grid(column = 0, row = 13, padx = 105, pady = 5) 



                    def pp(): # pagina 6
                        global contador36, contador37, contador38, contador39, contador40, contador41, contador42
                        contador36 = 0
                        contador37 = 0
                        contador38 = 0
                        contador39 = 0
                        contador40 = 0
                        contador41 = 0
                        contador42 = 0
                        helptab6 = Tk()
                        helptab6.geometry("540x600")
                        helptab6.title("HELP-TAB (6 de 9)")
                        helptab6.config(background = "#404040")
                        texto = Label(helptab6, text= "Sistema De Ajuda", background = "#404040")
                        texto.grid(column = 0, row = 0, padx = 105, pady = 25)
                


                        texto1 = "                                                                                                       "
                        texto = Label(helptab6, text = texto1, background = "#404040")
                        texto.grid(column = 0, row = 2, padx = 105, pady = 5) 

                        def seno():
                            global texto1
                            global contador36
                            contador36 += 1
                            if contador36 % 2 == 1: # se contador = impar
                                texto1 = "Seno de x"
                                texto = Label(helptab6, text = texto1, background = "#404040")
                                texto.grid(column = 0, row = 2, padx = 105, pady = 5)
                            else:
                                texto1 = "                                                                                                       "
                                texto = Label(helptab6, text = texto1, background = "#404040")
                                texto.grid(column = 0, row = 2, padx = 105, pady = 5)
                    
                        bot_1 = Button(helptab6, text = "⇓                  sin                 ⇓", height = altura, width = 20, command = seno, background = background)
                        bot_1.grid(column = 0, row = 1, padx = 105, pady = 5) 



                        texto1 = "                                                                                                       "
                        texto = Label(helptab6, text = texto1, background = "#404040")
                        texto.grid(column = 0, row = 4, padx = 105, pady = 5) 

                        def cosseno():
                            global texto1
                            global contador37
                            contador37 += 1
                            if contador37 % 2 == 1: # se contador = impar
                                texto1 = "Cosseno de x"
                                texto = Label(helptab6, text = texto1, background = "#404040")
                                texto.grid(column = 0, row = 4, padx = 105, pady = 5)
                            else:
                                texto1 = "                                                                                                       "
                                texto = Label(helptab6, text = texto1, background = "#404040")
                                texto.grid(column = 0, row = 4, padx = 105, pady = 5)
                    
                        bot_1 = Button(helptab6, text = "⇓                  cos                 ⇓", height = altura, width = 20, command = cosseno, background = background)
                        bot_1.grid(column = 0, row = 3, padx = 105, pady = 5) 



                        texto1 = "                                                                                                       "
                        texto = Label(helptab6, text = texto1, background = "#404040")
                        texto.grid(column = 0, row = 6, padx = 105, pady = 5) 

                        def tangente():
                            global texto1
                            global contador38
                            contador38 += 1
                            if contador38 % 2 == 1: # se contador = impar
                                texto1 = "Tangente de x"
                                texto = Label(helptab6, text = texto1, background = "#404040")
                                texto.grid(column = 0, row = 6, padx = 105, pady = 5)
                            else:
                                texto1 = "                                                                                                       "
                                texto = Label(helptab6, text = texto1, background = "#404040")
                                texto.grid(column = 0, row = 6, padx = 105, pady = 5)
                    
                        bot_1 = Button(helptab6, text = "⇓                  tan                 ⇓", height = altura, width = 20, command = tangente, background = background)
                        bot_1.grid(column = 0, row = 5, padx = 105, pady = 5) 



                        texto1 = "                                                                                                       "
                        texto = Label(helptab6, text = texto1, background = "#404040")
                        texto.grid(column = 0, row = 8, padx = 105, pady = 5) 

                        def sete():
                            global texto1
                            global contador39
                            contador39 += 1
                            if contador39 % 2 == 1: # se contador = impar
                                texto1 = "Adiciona 7"
                                texto = Label(helptab6, text = texto1, background = "#404040")
                                texto.grid(column = 0, row = 8, padx = 105, pady = 5)
                            else:
                                texto1 = "                                                                                                       "
                                texto = Label(helptab6, text = texto1, background = "#404040")
                                texto.grid(column = 0, row = 8, padx = 105, pady = 5)
                    
                        bot_1 = Button(helptab6, text = "⇓                   7                  ⇓", height = altura, width = 20, command = sete, background = background)
                        bot_1.grid(column = 0, row = 7, padx = 105, pady = 5)



                        texto1 = "                                                                                                       "
                        texto = Label(helptab6, text = texto1, background = "#404040")
                        texto.grid(column = 0, row = 10, padx = 105, pady = 5) 

                        def oito():
                            global texto1
                            global contador40
                            contador40 += 1
                            if contador40 % 2 == 1: # se contador = impar
                                texto1 = "Adiciona 8"
                                texto = Label(helptab6, text = texto1, background = "#404040")
                                texto.grid(column = 0, row = 10, padx = 105, pady = 5)
                            else:
                                texto1 = "                                                                                                       "
                                texto = Label(helptab6, text = texto1, background = "#404040")
                                texto.grid(column = 0, row = 10, padx = 105, pady = 5)
                    
                        bot_1 = Button(helptab6, text = "⇓                   8                  ⇓", height = altura, width = 20, command = oito, background = background)
                        bot_1.grid(column = 0, row = 9, padx = 105, pady = 5)



                        texto1 = "                                                                                                       "
                        texto = Label(helptab6, text = texto1, background = "#404040")
                        texto.grid(column = 0, row = 12, padx = 105, pady = 5) 

                        def nove():
                            global texto1
                            global contador41
                            contador41 += 1
                            if contador41 % 2 == 1: # se contador = impar
                                texto1 = "Adiciona 9"
                                texto = Label(helptab6, text = texto1, background = "#404040")
                                texto.grid(column = 0, row = 12, padx = 105, pady = 5)
                            else:
                                texto1 = "                                                                                                       "
                                texto = Label(helptab6, text = texto1, background = "#404040")
                                texto.grid(column = 0, row = 12, padx = 105, pady = 5)
                    
                        bot_1 = Button(helptab6, text = "⇓                   9                  ⇓", height = altura, width = 20, command = nove, background = background)
                        bot_1.grid(column = 0, row = 11, padx = 105, pady = 5)



                        texto1 = "                                                                                                       "
                        texto = Label(helptab6, text = texto1, background = "#404040")
                        texto.grid(column = 0, row = 14, padx = 105, pady = 5) 

                        def multiplicação():
                            global texto1
                            global contador42
                            contador42 += 1
                            if contador42 % 2 == 1: # se contador = impar
                                texto1 = "Multiplicação"
                                texto = Label(helptab6, text = texto1, background = "#404040")
                                texto.grid(column = 0, row = 14, padx = 105, pady = 5)
                            else:
                                texto1 = "                                                                                                       "
                                texto = Label(helptab6, text = texto1, background = "#404040")
                                texto.grid(column = 0, row = 14, padx = 105, pady = 5)
                    
                        bot_1 = Button(helptab6, text = "⇓                   *                  ⇓", height = altura, width = 20, command = multiplicação, background = background)
                        bot_1.grid(column = 0, row = 13, padx = 105, pady = 5)                  



                        def pp(): # pagina 7
                            global contador43, contador44, contador45, contador46, contador47, contador48, contador49
                            contador43 = 0
                            contador44 = 0
                            contador45 = 0
                            contador46 = 0
                            contador47 = 0
                            contador48 = 0
                            contador49 = 0
                            helptab7 = Tk()
                            helptab7.geometry("540x600")
                            helptab7.title("HELP-TAB (7 de 9)")
                            helptab7.config(background = "#404040")
                            texto = Label(helptab7, text= "Sistema De Ajuda", background = "#404040")
                            texto.grid(column = 0, row = 0, padx = 105, pady = 25)



                            texto1 = "                                                                                                       "
                            texto = Label(helptab7, text = texto1, background = "#404040")
                            texto.grid(column = 0, row = 2, padx = 105, pady = 5) 

                            def secante():
                                global texto1
                                global contador43
                                contador43 += 1
                                if contador43 % 2 == 1: # se contador = impar
                                    texto1 = "Secante de x"
                                    texto = Label(helptab7, text = texto1, background = "#404040")
                                    texto.grid(column = 0, row = 2, padx = 105, pady = 5)
                                else:
                                    texto1 = "                                                                                                       "
                                    texto = Label(helptab7, text = texto1, background = "#404040")
                                    texto.grid(column = 0, row = 2, padx = 105, pady = 5)
                        
                            bot_1 = Button(helptab7, text = "⇓                  sec                 ⇓", height = altura, width = 20, command = secante, background = background)
                            bot_1.grid(column = 0, row = 1, padx = 105, pady = 5)   



                            texto1 = "                                                                                                       "
                            texto = Label(helptab7, text = texto1, background = "#404040")
                            texto.grid(column = 0, row = 4, padx = 105, pady = 5) 

                            def cossecante():
                                global texto1
                                global contador44
                                contador44 += 1
                                if contador44 % 2 == 1: # se contador = impar
                                    texto1 = "Cossecante de x"
                                    texto = Label(helptab7, text = texto1, background = "#404040")
                                    texto.grid(column = 0, row = 4, padx = 105, pady = 5)
                                else:
                                    texto1 = "                                                                                                       "
                                    texto = Label(helptab7, text = texto1, background = "#404040")
                                    texto.grid(column = 0, row = 4, padx = 105, pady = 5)
                        
                            bot_1 = Button(helptab7, text = "⇓                  csc                 ⇓", height = altura, width = 20, command = cossecante, background = background)
                            bot_1.grid(column = 0, row = 3, padx = 105, pady = 5) 



                            texto1 = "                                                                                                       "
                            texto = Label(helptab7, text = texto1, background = "#404040")
                            texto.grid(column = 0, row = 6, padx = 105, pady = 5) 

                            def cotangente():
                                global texto1
                                global contador45
                                contador45 += 1
                                if contador45 % 2 == 1: # se contador = impar
                                    texto1 = "Cotangente de x"
                                    texto = Label(helptab7, text = texto1, background = "#404040")
                                    texto.grid(column = 0, row = 6, padx = 105, pady = 5)
                                else:
                                    texto1 = "                                                                                                       "
                                    texto = Label(helptab7, text = texto1, background = "#404040")
                                    texto.grid(column = 0, row = 6, padx = 105, pady = 5)
                        
                            bot_1 = Button(helptab7, text = "⇓                  cot                 ⇓", height = altura, width = 20, command = cotangente, background = background)
                            bot_1.grid(column = 0, row = 5, padx = 105, pady = 5) 



                            texto1 = "                                                                                                       "
                            texto = Label(helptab7, text = texto1, background = "#404040")
                            texto.grid(column = 0, row = 8, padx = 105, pady = 5) 

                            def quatro():
                                global texto1
                                global contador46
                                contador46 += 1
                                if contador46 % 2 == 1: # se contador = impar
                                    texto1 = "Adiciona 4"
                                    texto = Label(helptab7, text = texto1, background = "#404040")
                                    texto.grid(column = 0, row = 8, padx = 105, pady = 5)
                                else:
                                    texto1 = "                                                                                                       "
                                    texto = Label(helptab7, text = texto1, background = "#404040")
                                    texto.grid(column = 0, row = 8, padx = 105, pady = 5)
                        
                            bot_1 = Button(helptab7, text = "⇓                   4                  ⇓", height = altura, width = 20, command = quatro, background = background)
                            bot_1.grid(column = 0, row = 7, padx = 105, pady = 5) 



                            texto1 = "                                                                                                       "
                            texto = Label(helptab7, text = texto1, background = "#404040")
                            texto.grid(column = 0, row = 10, padx = 105, pady = 5) 

                            def cinco():
                                global texto1
                                global contador47
                                contador47 += 1
                                if contador47 % 2 == 1: # se contador = impar
                                    texto1 = "Adiciona 5"
                                    texto = Label(helptab7, text = texto1, background = "#404040")
                                    texto.grid(column = 0, row = 10, padx = 105, pady = 5)
                                else:
                                    texto1 = "                                                                                                       "
                                    texto = Label(helptab7, text = texto1, background = "#404040")
                                    texto.grid(column = 0, row = 10, padx = 105, pady = 5)
                        
                            bot_1 = Button(helptab7, text = "⇓                   5                  ⇓", height = altura, width = 20, command = cinco, background = background)
                            bot_1.grid(column = 0, row = 9, padx = 105, pady = 5) 



                            texto1 = "                                                                                                       "
                            texto = Label(helptab7, text = texto1, background = "#404040")
                            texto.grid(column = 0, row = 12, padx = 105, pady = 5) 

                            def seis():
                                global texto1
                                global contador48
                                contador48 += 1
                                if contador48 % 2 == 1: # se contador = impar
                                    texto1 = "Adiciona 6"
                                    texto = Label(helptab7, text = texto1, background = "#404040")
                                    texto.grid(column = 0, row = 12, padx = 105, pady = 5)
                                else:
                                    texto1 = "                                                                                                       "
                                    texto = Label(helptab7, text = texto1, background = "#404040")
                                    texto.grid(column = 0, row = 12, padx = 105, pady = 5)
                        
                            bot_1 = Button(helptab7, text = "⇓                   6                  ⇓", height = altura, width = 20, command = seis, background = background)
                            bot_1.grid(column = 0, row = 11, padx = 105, pady = 5)      



                            texto1 = "                                                                                                       "
                            texto = Label(helptab7, text = texto1, background = "#404040")
                            texto.grid(column = 0, row = 14, padx = 105, pady = 5) 

                            def subtração():
                                global texto1
                                global contador49
                                contador49 += 1
                                if contador49 % 2 == 1: # se contador = impar
                                    texto1 = "Subtração"
                                    texto = Label(helptab7, text = texto1, background = "#404040")
                                    texto.grid(column = 0, row = 14, padx = 105, pady = 5)
                                else:
                                    texto1 = "                                                                                                       "
                                    texto = Label(helptab7, text = texto1, background = "#404040")
                                    texto.grid(column = 0, row = 14, padx = 105, pady = 5)
                        
                            bot_1 = Button(helptab7, text = "⇓                   -                  ⇓", height = altura, width = 20, command = subtração, background = background)
                            bot_1.grid(column = 0, row = 13, padx = 105, pady = 5)                             


                            def pp(): # pagina 8
                                global contador50, contador51, contador52, contador53, contador54, contador55, contador56
                                contador50 = 0
                                contador51 = 0
                                contador52 = 0
                                contador53 = 0
                                contador54 = 0
                                contador55 = 0
                                contador56 = 0
                                helptab8 = Tk()
                                helptab8.geometry("540x600")
                                helptab8.title("HELP-TAB (8 de 9)")
                                helptab8.config(background = "#404040")
                                texto = Label(helptab8, text= "Sistema De Ajuda", background = "#404040")
                                texto.grid(column = 0, row = 0, padx = 105, pady = 25)



                                texto1 = "                                                                                                       "
                                texto = Label(helptab8, text = texto1, background = "#404040")
                                texto.grid(column = 0, row = 2, padx = 105, pady = 5) 

                                def senohip():
                                    global texto1
                                    global contador50
                                    contador50 += 1
                                    if contador50 % 2 == 1: # se contador = impar
                                        texto1 = "Seno Hiperbólico de x"
                                        texto = Label(helptab8, text = texto1, background = "#404040")
                                        texto.grid(column = 0, row = 2, padx = 105, pady = 5)
                                    else:
                                        texto1 = "                                                                                                       "
                                        texto = Label(helptab8, text = texto1, background = "#404040")
                                        texto.grid(column = 0, row = 2, padx = 105, pady = 5)
                            
                                bot_1 = Button(helptab8, text = "⇓                 sinh                 ⇓", height = altura, width = 20, command = senohip, background = background)
                                bot_1.grid(column = 0, row = 1, padx = 105, pady = 5)                  



                                texto1 = "                                                                                                       "
                                texto = Label(helptab8, text = texto1, background = "#404040")
                                texto.grid(column = 0, row = 4, padx = 105, pady = 5) 

                                def coship():
                                    global texto1
                                    global contador51
                                    contador51 += 1
                                    if contador51 % 2 == 1: # se contador = impar
                                        texto1 = "Cosseno Hiperbólico de x"
                                        texto = Label(helptab8, text = texto1, background = "#404040")
                                        texto.grid(column = 0, row = 4, padx = 105, pady = 5)
                                    else:
                                        texto1 = "                                                                                                       "
                                        texto = Label(helptab8, text = texto1, background = "#404040")
                                        texto.grid(column = 0, row = 4, padx = 105, pady = 5)
                            
                                bot_1 = Button(helptab8, text = "⇓                 cosh                 ⇓", height = altura, width = 20, command = coship, background = background)
                                bot_1.grid(column = 0, row = 3, padx = 105, pady = 5)         



                                texto1 = "                                                                                                       "
                                texto = Label(helptab8, text = texto1, background = "#404040")
                                texto.grid(column = 0, row = 6, padx = 105, pady = 5) 

                                def tanhip():
                                    global texto1
                                    global contador52
                                    contador52 += 1
                                    if contador52 % 2 == 1: # se contador = impar
                                        texto1 = "Tangente Hiperbólica de x"
                                        texto = Label(helptab8, text = texto1, background = "#404040")
                                        texto.grid(column = 0, row = 6, padx = 105, pady = 5)
                                    else:
                                        texto1 = "                                                                                                       "
                                        texto = Label(helptab8, text = texto1, background = "#404040")
                                        texto.grid(column = 0, row = 6, padx = 105, pady = 5)
                            
                                bot_1 = Button(helptab8, text = "⇓                 tanh                 ⇓", height = altura, width = 20, command = tanhip, background = background)
                                bot_1.grid(column = 0, row = 5, padx = 105, pady = 5)          



                                texto1 = "                                                                                                       "
                                texto = Label(helptab8, text = texto1, background = "#404040")
                                texto.grid(column = 0, row = 8, padx = 105, pady = 5) 

                                def um():
                                    global texto1
                                    global contador53
                                    contador53 += 1
                                    if contador53 % 2 == 1: # se contador = impar
                                        texto1 = "Adiciona 1"
                                        texto = Label(helptab8, text = texto1, background = "#404040")
                                        texto.grid(column = 0, row = 8, padx = 105, pady = 5)
                                    else:
                                        texto1 = "                                                                                                       "
                                        texto = Label(helptab8, text = texto1, background = "#404040")
                                        texto.grid(column = 0, row = 8, padx = 105, pady = 5)
                            
                                bot_1 = Button(helptab8, text = "⇓                   1                  ⇓", height = altura, width = 20, command = um, background = background)
                                bot_1.grid(column = 0, row = 7, padx = 105, pady = 5)   



                                texto1 = "                                                                                                       "
                                texto = Label(helptab8, text = texto1, background = "#404040")
                                texto.grid(column = 0, row = 10, padx = 105, pady = 5) 

                                def dois():
                                    global texto1
                                    global contador54
                                    contador54 += 1
                                    if contador54 % 2 == 1: # se contador = impar
                                        texto1 = "Adiciona 2"
                                        texto = Label(helptab8, text = texto1, background = "#404040")
                                        texto.grid(column = 0, row = 10, padx = 105, pady = 5)
                                    else:
                                        texto1 = "                                                                                                       "
                                        texto = Label(helptab8, text = texto1, background = "#404040")
                                        texto.grid(column = 0, row = 10, padx = 105, pady = 5)
                            
                                bot_1 = Button(helptab8, text = "⇓                   2                  ⇓", height = altura, width = 20, command = dois, background = background)
                                bot_1.grid(column = 0, row = 9, padx = 105, pady = 5)        



                                texto1 = "                                                                                                       "
                                texto = Label(helptab8, text = texto1, background = "#404040")
                                texto.grid(column = 0, row = 12, padx = 105, pady = 5) 

                                def tres():
                                    global texto1
                                    global contador55
                                    contador55 += 1
                                    if contador55 % 2 == 1: # se contador = impar
                                        texto1 = "Adiciona 3"
                                        texto = Label(helptab8, text = texto1, background = "#404040")
                                        texto.grid(column = 0, row = 12, padx = 105, pady = 5)
                                    else:
                                        texto1 = "                                                                                                       "
                                        texto = Label(helptab8, text = texto1, background = "#404040")
                                        texto.grid(column = 0, row = 12, padx = 105, pady = 5)
                            
                                bot_1 = Button(helptab8, text = "⇓                   3                  ⇓", height = altura, width = 20, command = tres, background = background)
                                bot_1.grid(column = 0, row = 11, padx = 105, pady = 5)         



                                texto1 = "                                                                                                       "
                                texto = Label(helptab8, text = texto1, background = "#404040")
                                texto.grid(column = 0, row = 14, padx = 105, pady = 5) 

                                def soma():
                                    global texto1
                                    global contador56
                                    contador56 += 1
                                    if contador56 % 2 == 1: # se contador = impar
                                        texto1 = "Soma"
                                        texto = Label(helptab8, text = texto1, background = "#404040")
                                        texto.grid(column = 0, row = 14, padx = 105, pady = 5)
                                    else:
                                        texto1 = "                                                                                                       "
                                        texto = Label(helptab8, text = texto1, background = "#404040")
                                        texto.grid(column = 0, row = 14, padx = 105, pady = 5)
                            
                                bot_1 = Button(helptab8, text = "⇓                   +                  ⇓", height = altura, width = 20, command = soma, background = background)
                                bot_1.grid(column = 0, row = 13, padx = 105, pady = 5)


                                
                                def pp(): # pagina 9      
                                    global contador57, contador58, contador59, contador60, contador61, contador62, contador63
                                    contador57 = 0
                                    contador58 = 0
                                    contador59 = 0
                                    contador60 = 0
                                    contador61 = 0
                                    contador62 = 0
                                    contador63 = 0            
                                    helptab9 = Tk()
                                    helptab9.geometry("540x600")
                                    helptab9.title("HELP-TAB (8 de 9)")
                                    helptab9.config(background = "#404040")
                                    texto = Label(helptab9, text= "Sistema De Ajuda", background = "#404040")
                                    texto.grid(column = 0, row = 0, padx = 105, pady = 25)       



                                    texto1 = "                                                                                                       "
                                    texto = Label(helptab9, text = texto1, background = "#404040")
                                    texto.grid(column = 0, row = 2, padx = 105, pady = 5) 

                                    def secantehip():
                                        global texto1
                                        global contador57
                                        contador57 += 1
                                        if contador57 % 2 == 1: # se contador = impar
                                            texto1 = "Secante Hiperbólica de x"
                                            texto = Label(helptab9, text = texto1, background = "#404040")
                                            texto.grid(column = 0, row = 2, padx = 105, pady = 5)
                                        else:
                                            texto1 = "                                                                                                       "
                                            texto = Label(helptab9, text = texto1, background = "#404040")
                                            texto.grid(column = 0, row = 2, padx = 105, pady = 5)
                                
                                    bot_1 = Button(helptab9, text = "⇓                 sech                 ⇓", height = altura, width = 20, command = secantehip, background = background)
                                    bot_1.grid(column = 0, row = 1, padx = 105, pady = 5)


                                    texto1 = "                                                                                                       "
                                    texto = Label(helptab9, text = texto1, background = "#404040")
                                    texto.grid(column = 0, row = 4, padx = 105, pady = 5) 

                                    def cossecantehip():
                                        global texto1
                                        global contador58
                                        contador58 += 1
                                        if contador58 % 2 == 1: # se contador = impar
                                            texto1 = "Cossecante Hiperbólica de x"
                                            texto = Label(helptab9, text = texto1, background = "#404040")
                                            texto.grid(column = 0, row = 4, padx = 105, pady = 5)
                                        else:
                                            texto1 = "                                                                                                       "
                                            texto = Label(helptab9, text = texto1, background = "#404040")
                                            texto.grid(column = 0, row = 4, padx = 105, pady = 5)
                                
                                    bot_1 = Button(helptab9, text = "⇓                 csch                 ⇓", height = altura, width = 20, command = cossecantehip, background = background)
                                    bot_1.grid(column = 0, row = 3, padx = 105, pady = 5)



                                    texto1 = "                                                                                                       "
                                    texto = Label(helptab9, text = texto1, background = "#404040")
                                    texto.grid(column = 0, row = 6, padx = 105, pady = 5) 

                                    def cotangentehip():
                                        global texto1
                                        global contador59
                                        contador59 += 1
                                        if contador59 % 2 == 1: # se contador = impar
                                            texto1 = "Cotangente Hiperbólica de x"
                                            texto = Label(helptab9, text = texto1, background = "#404040")
                                            texto.grid(column = 0, row = 6, padx = 105, pady = 5)
                                        else:
                                            texto1 = "                                                                                                       "
                                            texto = Label(helptab9, text = texto1, background = "#404040")
                                            texto.grid(column = 0, row = 6, padx = 105, pady = 5)
                                
                                    bot_1 = Button(helptab9, text = "⇓                 coth                 ⇓", height = altura, width = 20, command = cotangentehip, background = background)
                                    bot_1.grid(column = 0, row = 5, padx = 105, pady = 5)            



                                    texto1 = "                                                                                                       "
                                    texto = Label(helptab9, text = texto1, background = "#404040")
                                    texto.grid(column = 0, row = 8, padx = 105, pady = 5) 

                                    def troca():
                                        global texto1
                                        global contador60
                                        contador60 += 1
                                        if contador60 % 2 == 1: # se contador = impar
                                            texto1 = "Trocar número para negativo ou positivo"
                                            texto = Label(helptab9, text = texto1, background = "#404040")
                                            texto.grid(column = 0, row = 8, padx = 105, pady = 5)
                                        else:
                                            texto1 = "                                                                                                       "
                                            texto = Label(helptab9, text = texto1, background = "#404040")
                                            texto.grid(column = 0, row = 8, padx = 105, pady = 5)
                                
                                    bot_1 = Button(helptab9, text = "⇓                 +/-                  ⇓", height = altura, width = 20, command = troca, background = background)
                                    bot_1.grid(column = 0, row = 7, padx = 105, pady = 5)             



                                    texto1 = "                                                                                                       "
                                    texto = Label(helptab9, text = texto1, background = "#404040")
                                    texto.grid(column = 0, row = 10, padx = 105, pady = 5) 

                                    def zero():
                                        global texto1
                                        global contador61
                                        contador61 += 1
                                        if contador61 % 2 == 1: # se contador = impar
                                            texto1 = "Adiciona 0"
                                            texto = Label(helptab9, text = texto1, background = "#404040")
                                            texto.grid(column = 0, row = 10, padx = 105, pady = 5)
                                        else:
                                            texto1 = "                                                                                                       "
                                            texto = Label(helptab9, text = texto1, background = "#404040")
                                            texto.grid(column = 0, row = 10, padx = 105, pady = 5)
                                
                                    bot_1 = Button(helptab9, text = "⇓                   0                  ⇓", height = altura, width = 20, command = zero, background = background)
                                    bot_1.grid(column = 0, row = 9, padx = 105, pady = 5)          



                                    texto1 = "                                                                                                       "
                                    texto = Label(helptab9, text = texto1, background = "#404040")
                                    texto.grid(column = 0, row = 12, padx = 105, pady = 5) 

                                    def virgula():
                                        global texto1
                                        global contador62
                                        contador62 += 1
                                        if contador62 % 2 == 1: # se contador = impar
                                            texto1 = "Adiciona vírgula"
                                            texto = Label(helptab9, text = texto1, background = "#404040")
                                            texto.grid(column = 0, row = 12, padx = 105, pady = 5)
                                        else:
                                            texto1 = "                                                                                                       "
                                            texto = Label(helptab9, text = texto1, background = "#404040")
                                            texto.grid(column = 0, row = 12, padx = 105, pady = 5)
                                
                                    bot_1 = Button(helptab9, text = "⇓                   ,                  ⇓", height = altura, width = 20, command = virgula, background = background)
                                    bot_1.grid(column = 0, row = 11, padx = 105, pady = 5)       



                                    texto1 = "                                                                                                       "
                                    texto = Label(helptab9, text = texto1, background = "#404040")
                                    texto.grid(column = 0, row = 14, padx = 105, pady = 5) 

                                    def igual():
                                        global texto1
                                        global contador63
                                        contador63 += 1
                                        if contador63 % 2 == 1: # se contador = impar
                                            texto1 = "Atribuíra a solução da expressão no visor"
                                            texto = Label(helptab9, text = texto1, background = "#404040")
                                            texto.grid(column = 0, row = 14, padx = 105, pady = 5)
                                        else:
                                            texto1 = "                                                                                                       "
                                            texto = Label(helptab9, text = texto1, background = "#404040")
                                            texto.grid(column = 0, row = 14, padx = 105, pady = 5)
                                
                                    bot_1 = Button(helptab9, text = "⇓                   =                  ⇓", height = altura, width = 20, command = igual, background = background)
                                    bot_1.grid(column = 0, row = 13, padx = 105, pady = 5)                                                                                                                                                             



                                bot_1 = Button(helptab8, text = "Próxima Página (9)", height = altura, width = 20, command = pp, background = background)
                                bot_1.grid(column = 0, row = 15, padx = 2, pady = 5)

                            bot_1 = Button(helptab7, text = "Próxima Página (8)", height = altura, width = 20, command = pp, background = background)
                            bot_1.grid(column = 0, row = 15, padx = 2, pady = 5)

                        bot_1 = Button(helptab6, text = "Próxima Página (7)", height = altura, width = 20, command = pp, background = background)
                        bot_1.grid(column = 0, row = 15, padx = 2, pady = 5)

                    bot_1 = Button(helptab5, text = "Próxima Página (6)", height = altura, width = 20, command = pp, background = background)
                    bot_1.grid(column = 0, row = 15, padx = 2, pady = 5)

                bot_1 = Button(helptab4, text = "Próxima Página (5)", height = altura, width = 20, command = pp, background = background)
                bot_1.grid(column = 0, row = 15, padx = 2, pady = 5)

            bot_1 = Button(helptab3, text = "Próxima Página (4)", height = altura, width = 20, command = pp, background = background)
            bot_1.grid(column = 0, row = 15, padx = 2, pady = 5)

        bot_1 = Button(helptab2, text = "Próxima Página (3)", height = altura, width = 20, command = pp, background = background)
        bot_1.grid(column = 0, row = 15, padx = 2, pady = 5)

    bot_1 = Button(helptab1, text = "Próxima Página (2)", height = altura, width = 20, command = pp, background = background)
    bot_1.grid(column = 0, row = 15, padx = 2, pady = 5)
