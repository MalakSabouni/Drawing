import pygame
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
#for change the chape of the mouse use #cursor



window=pygame.display.set_mode((1400,700))
window.fill((255, 255, 255))
pygame.display.set_caption("my first pygame")
mouse=pygame.mouse.get_pressed()  
rad=12
width=40
height=40
v=1
lenth=12
color = [
    [(255,204,204),(255,229,204),(255,229,204),(255,255,204),(204,255,204),(204,255,255),(204,204,255),(229,204,255),(255,102,102),(255,153,51),(255,255,255)],
    [(255,0,0),(255,128,0),(255,255,0),(0,255,0),(0,153,76),(51,255,255),(0,0,255),(127,0,255),(255,0,255),(255,0,127),(128,128,128)],
    [(51,0,0),(51,25,0),(51,51,0),(0,51,0),(0,51,25),(0,25,51),(0,51,51),(0,0,51),(51,0,51),(51,0,25),(0,0,0)]
    
]

#background 
def bg():
    pygame.init()
    pygame.draw.line(window,(0,0,0),(0,578),(1400,578),5)
    pygame.draw.rect(window,(192,192,192),(0,578,1400,135))#
    pygame.display.update()
    text = str("""prodused by malak sabouni :) >> 3/1/2020""")
    font = pygame.font.SysFont("comicsansms", 15)
    text = font.render(text, True, (0,0,0))
    window.blit(text, (590, 650))
bg()

pen_or_bruch=True
h=0
w=0
###draw the color rects
def draw_color():
    global h,w
    for rows in color:
        for column in rows:
            pygame.draw.rect(window,(column),(0+w,700-40-h-v,width,height),)
            pygame.display.update()

            w += width
        h +=height
        w = 0
    h=0
#

#fontcolor function
def fontcolor (posx,posy):
    count1,count2,count3=0,0,0
    fac1,fac2,fac3=1,1,1
    for i in range (11):
        if (posy<700) and (posy>700-width):
            if posx<width*fac1:
                font=color[0][count1]
                return font
            count1 += 1
            fac1 += 1
        
        elif ((posy<700-width) and (posy>700-(2*width))):
            if posx<width*fac2:
                font=color[1][count2]
                return font
            count2 += 1
            fac2 += 1
        
        elif ((posy<700-(2*width)) and (posy>700-3*width)):
            if posx<width*fac3:
                font=color[2][count3]
                return font
            count3 += 1
            fac3 += 1
            
        else:
            return (0,0,0)

#setting rects
        
l1=[pygame.image.load("2x/1.png")]
l2=[pygame.image.load("2x/2.png")]
l3=[pygame.image.load("2x/3.png")]
ris=[pygame.image.load("2x/ris.png")]
bruch=[pygame.image.load("2x/bruch.png")]
fill=[pygame.image.load("2x/fill.png")]
c=[pygame.image.load("2x/c.png")]
write=[pygame.image.load("2x/write.png")]
open_=[pygame.image.load("2x/open.png")]
save1=[pygame.image.load("2x/save.png")]


#draw_setting fun
def setting():
    window.blit(l1[0],(1340,593))
    window.blit(l3[0],(1220,593))
    window.blit(l2[0],(1280,593))
    window.blit(ris[0],(1280,655))
    window.blit(bruch[0],(1100,593))
    window.blit(fill[0],(1220,655))
    window.blit(c[0],(1340,655))
    window.blit(write[0],(1160,593))
    window.blit(open_[0],(1160,655))
    window.blit(save1[0],(1100,655))
    pygame.display.update()


    


#Change pygame caption
def changeCaption(txt):
   pygame.display.set_caption(txt)
#function for get the color of pixels

#save
def save(path):
    path=str(path)+".txt"
    file = open(path, 'w')
    for y in range(574):
        for x in range(1400):
            color=window.get_at((x,y))
            #color=color[:3]
            print(color,end="\n",file=file)
    file.close()
   # Overwrite the current file, or if it doesn't exist create a new one
    name = path.split("/")
    changeCaption(name[-1])
def showFileNav(op=False):
   #Op is short form for open as open is a key word
    window = Tk()
    window.attributes("-topmost", True)
    window.withdraw()
    myFormats = [('Windows Text File','*.txt')]
    if op:
       filename = askopenfilename(title="Open File",filetypes=myFormats) # Ask the user which file they want to open
    else:
       filename = asksaveasfilename(title="Save File",filetypes=myFormats) # Ask the user choose a path to save their file to
       
    if filename: #If the user seletced something 
       x = filename[:] # Make a copy
       return x


#Opens the file from the given path and displays it to the screen
#load
def openFile(path):
    x=-1
    y=0
    count=0
    with open(path, 'r') as f:
        for i in f:
            count += 1
            x +=1
            tuples = tuple(int(number) for number in i.replace('(', '').replace(')', '').replace('...', '').split(','))
            pygame.draw.rect(window,tuples,(x,y,1,1))
            if x % 1400 == 0:
                y += 1
                x=0
    f.close()
    pygame.display.update()
    

run=True
draw_color()
setting()
while run:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run=False
           
            
    mouse=pygame.mouse.get_pressed()
    pos=pygame.mouse.get_pos()
    mousesens=False
    if mouse[0]==1 and mousesens:
        fontcolory=fontcolor(pos[0],pos[1])
        mousesens=False
    if mouse[0]==1 and (pos[0]<447)and pos[1]>575:
        mousens=True
        fontcolory=fontcolor(pos[0],pos[1])
        
    if True: 
        if pos[0]>1100 and pos[1]>580:
            if mouse[0]==1 :
                if pos[0]>1340 and pos[1]>640:#c
                    window.fill((255,255,255))
                    bg()
                    draw_color()
                    setting()
                elif pos[0]>1340 and pos[1]>580:#1
                    rad=4
                    lenth=7
                elif pos[0]>1280 and pos[1]>640:#ris
                    fontcolory=(255,255,255)
                elif pos[0]>1280 and pos[1]>580:#2
                    rad=12
                    lenth=12
                elif pos[0]>1220 and pos[1]>640:#fill
                    window.fill(fontcolory)
                    bg()
                    setting()
                    draw_color()
                elif pos[0]>1220 and pos[1]>580:#3
                    rad=20
                    lenth=20
                elif pos[0]>1160 and pos[1]>640:#open file
                    path = showFileNav(True)
                    if path:
                        openFile(path)
                        savedPath = path
                elif pos[0]>1160 and pos[1]>580:#draw
                    pen_or_bruch=False
                               
                elif pos[0]>1100 and pos[1]>640:#save
                    path = showFileNav()
                    if path:
                        savedPath = path
                        save(savedPath)
                else: #bruch
                    pen_or_bruch=True
                
                    
                    
                    
        if pos[1]<570:#not(pos[0]>1100 and pos[1]>580):
            try:
                if mouse[0]==1 :
                    x=pos[0]
                    y=pos[1]
                    draw=True
                    if pen_or_bruch:
                        pygame.draw.circle(window,fontcolory,(x,y),rad)
                        pygame.display.update()
                    else:
                        pygame.draw.rect(window,fontcolory,(x,y,lenth,lenth))
                        pygame.display.update()
                if draw:
            
                    keys_pressed=pygame.key.get_pressed()
                if keys_pressed[pygame.K_LEFT] or (x>pos[0] and mouse[0]==1):
                    x -=v
                    
                    if pen_or_bruch:
                        if pos[1]>580: #(x<447 and pos[1]>570) or (pos[1]>400 and x>1280):
                            draw=False
                        else:
                            pygame.draw.circle(window,fontcolory,(x,y),rad)
                            pygame.display.update()
                    else:
                        if pos[1]>580:# (x<447 and pos[1]>570) or (pos[1]>400 and x>1280):
                            draw=False
                        else:
                             pygame.draw.rect(window,fontcolory,(x,y,lenth,lenth))
                             pygame.display.update()
                if keys_pressed[pygame.K_RIGHT] or (x<pos[0] and mouse[0]==1):
                    x +=v
                    
                    if pen_or_bruch:
                        if pos[1]>580:#(x<447 and pos[1]>570) or (pos[1]>400 and x>1280):
                            draw=False
                        else:
                            pygame.draw.circle(window,fontcolory,(x,y),rad)
                            pygame.display.update()
                    else:
                        if pos[1]>580:#(x<447 and pos[1]>570) or (pos[1]>400 and x>1280):
                            draw=False
                        else:
                             pygame.draw.rect(window,fontcolory,(x,y,lenth,lenth))
                             pygame.display.update()
                if keys_pressed[pygame.K_UP] or (y>pos[1] and mouse[0]==1):
                    y -= v

                    if pen_or_bruch:
                        if y>580:#(y>570 and pos[0]<447) or (y>400 and pos[0]>1280):
                            draw=False
                        pygame.draw.circle(window,fontcolory,(x,y),rad)
                        pygame.display.update()
                    else:
                        if y>580:##(y>570 and pos[0]<447) or (y>400 and pos[0]>1280):
                            draw=False
                        else:
                            pygame.draw.rect(window,fontcolory,(x,y,lenth,lenth))
                            pygame.display.update()
                if keys_pressed[pygame.K_DOWN] or (y<pos[1] and mouse[0]==1):
                    y += v
                    
                    if pen_or_bruch:
                        
                        if y>580:#(y>570 and pos[0]<447) or (y>400 and pos[0]>1280) :
                            draw=False
                        else:
                            pygame.draw.circle(window,fontcolory,(x,y),rad)
                            pygame.display.update()
                    else:
                        if y>580:#(y>570 and pos[0]<447) or (y>400 and pos[0]>1280):
                            draw=False
                        else:
                             pygame.draw.rect(window,fontcolory,(x,y,lenth,lenth))
                             pygame.display.update()
            except:
                pass
    
    

pygame.quit()

    
    

