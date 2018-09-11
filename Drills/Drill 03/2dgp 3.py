from pico2d import *
os.chdir("C:\\Users\\Administrator\\Desktop\\2017180023----\\Labs\\Lecture03")

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

isrect=true # true=rect false=circle
rectway=3  # 1=LEFT 2=TOP 3=RIGHT 4=BOTTOM

x = 400
y=90
if(x==400,y==90):
    if(isrect==true):
        if(rectway==1):
             clear_canvas_now()
             grass.draw_now(400, 30)
             character.draw_now(x, y)
             x = x - 2
             delay(0.01)

             if(x<=50):
                 rectway=4

        elif(rectway==2):
             clear_canvas_now()
             grass.draw_now(400, 30)
             character.draw_now(x, y)
             y = y + 2
             delay(0.01)

             if(y>=500):
                 rectway=1

        elif(rectway==3):
             clear_canvas_now()
             grass.draw_now(400, 30)
             character.draw_now(x, y)
             x = x -2
             delay(0.01)

             if(x<=50):
                 rectway=2

        elif(rectway==4):
             clear_canvas_now()
             grass.draw_now(400, 30)
             character.draw_now(x, y)
             x = x -2
             delay(0.01)

             if(x<=50):
                 rectway=3
        
    
while (x < 800):
    if()
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, 90)
    x = x + 2
    delay(0.01)
    
close_canvas()
 
