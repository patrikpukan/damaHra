import tkinter as tk

canvas=tk.Canvas(width=480 , height=480+40)
canvas.pack()

def brandNewGame():
  global stav, povolenie, typ_fig, sur_fig, b,w, pomocka, narade, winB, winQ
  # winB.place(x=800,y=800)
  # winQ.place(x=800,y=800)
  winB.destroy()
  winQ.destroy()
  stav=[[0,2,0,2,0,2,0,2],[2,0,2,0,2,0,2,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0]]
  typ_fig=0
  sur_fig=[0,0]
  povolenie=[]
  narade="white"
  b=0
  w=0
  board()
  pomocka=0

def policko(xp,yp,farbap):
    canvas.create_rectangle(xp,yp,xp+50,yp+50,fill=farbap)

def figure(y,x,farbaf,farbaf_okraj):
    yf=(40+25+(50*y))
    xf=(40+25+(50*x))
    return canvas.create_oval(xf-23,yf-23,xf+23,yf+23,fill=farbaf,outline=farbaf_okraj,width=3)

def win(kto):
    global winQ, winB
    canvas.delete("all")
    canvas.create_rectangle(10,10,470,210,width=3)
    canvas.create_text(240,110,text="Winner: "+str(kto),font=100)
    winB=tk.Button(canvas, text="New Game",width=50, command = brandNewGame)
    winQ=tk.Button(canvas,text = "Quit Game",width=50, command = quit)
    winB.place(x=50, y=230)
    winQ.place(x=50, y=330)


def tah(narade,riadok,stlpec,viacskok):
    global vyhodenie
    global povolenie
    global povolenie_skok
    board()
    povolenie_skok=[]
    povolenie=[]
    vyhodenie=[]
    if stav[riadok][stlpec]==1 and narade=="white":
        povol(riadok,stlpec,1,0,viacskok)
    if stav[riadok][stlpec]==3 and narade=="white":
        povol(riadok,stlpec,3,0,viacskok)
    if stav[riadok][stlpec]==2 and narade=="black":
        povol(riadok,stlpec,2,0,viacskok)
    if stav[riadok][stlpec]==4 and narade=="black":
        povol(riadok,stlpec,4,0,viacskok)

        
    for i in povolenie:
        y=((i[0])*50)+40
        x=((i[1])*50)+40
        policko(x,y,"green")

    if povolenie_skok!=[]:
        for i in povolenie_skok:
            y=((i[0])*50)+40
        x=((i[1])*50)+40
        policko(x,y,"blue")
        
def povol(ria,stl,typ,dvojskok,viacskok):
    if typ==2:
        ria+=1
        if 0<=ria<=7:
            stlpec=[stl-1,stl+1]
            if 0<= stlpec[0] <=7:
                if stav[ria][stlpec[0]]==0 and dvojskok==0 and viacskok==0:
                    povolenie.append([ria,stlpec[0]])
                    vyhodenie.append(["x"])
                else:
                    if stav[ria][stlpec[0]]== 1 or stav[ria][stlpec[0]]== 3:
                        if 0<=(ria+1)<=7 and 0<=(stlpec[0]-1)<=7:
                            if stav[ria+1][stlpec[0]-1]==0:
                                if dvojskok==1:
                                    povolenie_skok.append([ria+1,stlpec[0]-1])
                                else:
                                    povolenie.append([ria+1,stlpec[0]-1])
                                vyhodenie.append([ria,stlpec[0]])
                                povol(ria+1,stlpec[0]-1,2,1,1)

            if 0<= stlpec[1] <=7:
                if stav[ria][stlpec[1]]==0 and dvojskok==0 and viacskok==0:
                    povolenie.append([ria,stlpec[1]])
                    vyhodenie.append(["x"])
                else:
                    if stav[ria][stlpec[1]]==1 or stav[ria][stlpec[1]]== 3:
                         if 0<=(ria+1)<=7 and 0<=(stlpec[1]+1)<=7:
                             if stav[ria+1][stlpec[1]+1]==0:
                                if dvojskok==1:
                                    povolenie_skok.append([ria+1,stlpec[1]+1])
                                else:
                                    povolenie.append([ria+1,stlpec[1]+1])
                                vyhodenie.append([ria,stlpec[1]])
                                povol(ria+1,stlpec[1]+1,2,1,1)
    elif typ==1:
        ria-=1
        if 0<=ria<=7:
            stlpec=[stl-1,stl+1]
            if 0<= stlpec[0] <=7:
                if stav[ria][stlpec[0]]==0 and dvojskok==0 and viacskok==0:
                    povolenie.append([ria,stlpec[0]])
                    vyhodenie.append(["x"])
                else:
                    if stav[ria][stlpec[0]]== 2 or stav[ria][stlpec[0]]== 4:
                        if 0<=(ria-1)<=7 and 0<=(stlpec[0]-1)<=7:
                            if stav[ria-1][stlpec[0]-1]==0:
                                if dvojskok==1:
                                    povolenie_skok.append([ria-1,stlpec[0]-1])
                                else:
                                    povolenie.append([ria-1,stlpec[0]-1])
                                vyhodenie.append([ria,stlpec[0]])
                                povol(ria-1,stlpec[0]-1,1,1,1)

            if 0<= stlpec[1] <=7:
                if stav[ria][stlpec[1]]==0 and dvojskok==0 and viacskok==0:
                    povolenie.append([ria,stlpec[1]])
                    vyhodenie.append(["x"])
                else:
                    if stav[ria][stlpec[1]]== 2 or stav[ria][stlpec[1]]== 4:
                        if 0<=(ria-1)<=7 and 0<=(stlpec[1]+1)<=7:
                            if stav[ria-1][stlpec[1]+1]==0:
                                if dvojskok==1:
                                    povolenie_skok.append([ria-1,stlpec[1]+1])
                                else:
                                    povolenie.append([ria-1,stlpec[1]+1])
                                vyhodenie.append([ria,stlpec[1]])
                                povol(ria-1,stlpec[1]+1,1,1,1)
    elif typ==3 or typ==4:
        if typ==3:
            pomocka=[1,3]
        else:
            pomocka=[2,4]
        
        riadok=ria+1
        stlpec=stl+1
        while 0<=riadok<=7 and 0<=stlpec<=7:
            if stav[riadok][stlpec]==0:
                povolenie.append([riadok,stlpec])
            elif  stav[riadok][stlpec]==pomocka[0] or stav[riadok][stlpec]==pomocka[1]:
                break
            riadok+=1
            stlpec+=1

        riadok=ria+1
        stlpec=stl-1
        
        while 0<=riadok<=7 and 0<=stlpec<=7:
            if stav[riadok][stlpec]==0:
                povolenie.append([riadok,stlpec])
            elif  stav[riadok][stlpec]==pomocka[0] or stav[riadok][stlpec]==pomocka[1]:
                break
            riadok+=1
            stlpec-=1

        riadok=ria-1
        stlpec=stl+1
        while 0<=riadok<=7 and 0<=stlpec<=7:
            if stav[riadok][stlpec]==0:
                povolenie.append([riadok,stlpec])
            elif  stav[riadok][stlpec]==pomocka[0] or stav[riadok][stlpec]==pomocka[1]:
                break
            riadok-=1
            stlpec+=1
            
        riadok=ria-1
        stlpec=stl-1
        while 0<=riadok<=7 and 0<=stlpec<=7:
            if stav[riadok][stlpec]==0:
                povolenie.append([riadok,stlpec])
            elif  stav[riadok][stlpec]==pomocka[0] or stav[riadok][stlpec]==pomocka[1]:
                break
            riadok-=1
            stlpec-=1

            
def board():
    canvas.delete("all")
    canvas.create_rectangle(10,10,470,470,width=3)
    farb="red"
    farb2="black"
    y=-10
    for i in range(8):
        x=40
        y+=50
        farb,farb2=farb2,farb
        for j in range(8):
            farb,farb2=farb2,farb
            policko(x,y,farb)
            x+=50

            if stav[i][j]==1:
                figure(i,j,"white","black")
            elif stav[i][j]==2:
                figure(i,j,"black","grey")
            elif stav[i][j]==3:
                figure(i,j,"white","red")
            elif stav[i][j]==4:
                figure(i,j,"black","white")
    if narade=="white":
        canvas.create_text(240,500,text="White's Turn",font=60)
    else:
        canvas.create_text(240,500,text="Black's Turn",font=60)
    canvas.create_text(80,500,text="Black's Score: "+str(w),font=40)
    canvas.create_text(400,500,text="White's Score:"+str(b),font=40)
    
def klik(event):
    global pomocka
    global povolenie
    global vyhodenie
    global narade
    global typ_fig
    global sur_fig
    global w
    global b
    xk=((event.x)-40)//50
    yk=((event.y)-40)//50
    if 0<=xk<=7 and 0<=yk<=7:
        if [yk,xk] not in povolenie and pomocka==1:
            pomocka=0
            if narade=="white":
                narade="black"
            else:
                narade="white"
        if [yk,xk] in povolenie:
            stav[yk][xk]=typ_fig
            stav[sur_fig[0]][sur_fig[1]]=0
            
            if typ_fig==1 or typ_fig==2:
                k=-1
                for i in povolenie:
                    k+=1
                    if i == [yk,xk]:
                        break
                if vyhodenie[k] != ["x"]:
                    stav[vyhodenie[k][0]][vyhodenie[k][1]]=0
                    if narade=="white":
                        b+=1
                    else:
                        w+=1
            else:
                pom1=[]
                pom2=[]
                r=sur_fig[0]
                s=sur_fig[1]
                while r!=yk:
                    if r > yk:
                        pom1.append(r)
                        r-=1
                    else:
                        pom1.append(r)
                        r+=1
                        
                while s!=xk:
                    if s > xk:
                        pom2.append(s)
                        s-=1
                    else:
                        pom2.append(s)
                        s+=1
                for i in range(len(pom1)):
                    if  stav[pom1[i]][pom2[i]]!=0:
                        if narade=="white":
                            b+=1
                        else:
                            w+=1
                    stav[pom1[i]][pom2[i]]=0
                    
            vyhodenie=[]
            povolenie=[]
            
            
            for i in range(8):
                if stav[0][i]==1:
                    stav[0][i]=3
                if stav[7][i]==2:
                    stav[7][i]=4
            
            board()
            if povolenie_skok!=[]:
                for i in povolenie_skok:
                    y=((i[0])*50)+40
                    x=((i[1])*50)+40
                    policko(x,y,"blue")
                    pomocka=1
                    typ_fig=stav[yk][xk]
                    sur_fig=[yk,xk]
                    tah(narade,yk,xk,1)
                    
            else:
                pomocka=0
                if narade=="white":
                    narade="black"
                else:
                    narade="white"
                board()
        else:
            typ_fig=stav[yk][xk]
            sur_fig=[yk,xk]
            tah(narade,yk,xk,0)
    if b==8:
        win("White")
    if w==8:
        win("Black")
global stav
stav=[[0,2,0,2,0,2,0,2],[2,0,2,0,2,0,2,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,1,0,1,0,1,0,1],[1,0,1,0,1,0,1,0]]

typ_fig=0
sur_fig=[0,0]
global povolenie
povolenie=[]
narade="white"
b=0
w=0
board()
pomocka=0
canvas.bind("<Button-1>",klik)


