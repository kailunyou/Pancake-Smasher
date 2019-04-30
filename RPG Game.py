


from gamelib import*
import random
game=Game(800,800,"BunnyGame",5)



#Background stuff
titlescreen=Image("titlescreen.png",game)
bg=Image("forest1.png",game)
game.setBackground(bg)
titlescreen.resizeTo(game.width,game.height)
bg.resizeTo(800,800)
house=Image("house.png",game)
house.moveTo(150,558)
house.resizeBy(-60)
sCoin=Animation("SecretCarrotCoin.png",6,game,937/6,156)
sCoin.moveTo(-700,550)
sCoin.resizeBy(-60)
animationinc=Image("animationinc.png",game)
buny=Animation("bunnys.png",6,game,396/6,89)
buny.resizeBy(100)
buny.moveTo(400,300)
blackscreen=Image("blackscreen.jpg",game)
blackscreen.resizeTo(800,800)
f=Font(white,50,blue)
ff=Font(black,75)
firstscreen=Image("storyboard.png",game)
firstscreen.resizeTo(800,800)
end=Image("end.jpg",game)
endsong=Sound("endS.wav",2)
plasma=Image("plasmaball.png",game)
#Player stuff
playerL=Animation("bunnyL.png",6,game,396/6,89)
playerR=Animation("bunnyR.png",6,game,395/6,88)
playerL.moveTo(170,550)
playerL.setSpeed(1,0)
playerR.moveTo(170,550)
playerR.setSpeed(1,0)
playerL.visible=False
playerR.visible=True
house.health=100
plasma=[]
for index in range(250):
    plasma.append(Image("plasmaball.png",game))
for index in range(250):
    plasma[index].visible=False
    plasma[index].resizeBy(-50)
    plasma[index].move()
#Goon stuff
goon=[]
for index in range(10):
    goon.append(Animation("GoonL.png",9,game,2400/3,1800/3))
for index in range(10):
    goon[index].resizeBy(-75)
    goon[index].setSpeed(2,90)
    goon[index].moveTo(random.randint(2000,3000),653)






#Jumping stuff/variables
jumping=False
landed=False
factor=1
scrollx=(0)




#music
songg=Sound("sh.wav",1)



#loading screen
while not game.over:
    game.processInput()
    blackscreen.draw()
    buny.draw()
    animationinc.draw()
    game.drawText("Loading...",325,500,f)
    if game.time<1:
        game.over=True
    game.update(60)
    game.displayTime()
game.over=False

#TitleScreen
while not game.over:
    game.processInput()
    firstscreen.draw()
    titlescreen.draw()
    if keys.Pressed[K_p]:
        titlescreen.visible=False
    if keys.Pressed[K_SPACE]:
        game.over=True
    if keys.Pressed[K_o]:
        titlescreen.visible=True
    game.update(20)

game.over=False

#Game
while not game.over:
    game.processInput()
    bg.draw()
    game.scrollBackground("right",0)
    house.draw()
    playerR.draw()
    playerL.draw()
    sCoin.draw()
    songg.play()
    for index in range(10):
        goon[index].move()

    #PlayerMovement/Jump/Scrollx
    if playerR.y<650:
        landed=False
    else:
        landed=True
    if keys.Pressed[K_w] and landed and not jumping:
        jumping=True
    if jumping:
        playerL.y -=27*factor
        playerR.y -=27*factor
        factor*=.95
        landed = False
    if factor < .18:
            jumping = False
            factor = 1
    if not landed:
        playerL.y+=10
        playerR.y+=10
        
    if keys.Pressed[K_a]:
        game.scrollBackground("right",5)
        playerR.visible=False
        playerL.visible=True
        house.moveTo(scrollx+150,558)
        sCoin.moveTo(scrollx-700,500)
        for index in range(10):
            goon[index].draw()
            goon[index].x+=4
        playerL.draw()
        scrollx+=5
       
        
    if keys.Pressed[K_d]:
        game.scrollBackground("left",5)
        playerL.visible=False
        playerR.visible=True
        house.moveTo(scrollx+150,558)
        sCoin.moveTo(scrollx-700,500)
        for index in range(10):
            goon[index].draw()
            goon[index].x-=4
        playerR.draw()   
        scrollx-=5
    for index in range(10):
        if goon[index].collidedWith(house):
            goon[index].moveTo(random.randint(1000,2000),653)
            house.health-=100
    if house.health==0:
        game.over=True
    for index in range(250):
        if keys.Pressed[K_SPACE]and playerR.visible==True:
            plasma[index].visible=True
            plasma[index].moveTo(playerR.x,playerR.y)
            plasma[index].draw()
        if keys.Pressed[K_SPACE]and playerL.visible==True:
            plasma[index].visible=True
            plasma[index].moveTo(playerL.x,playerL.y)
            plasma[index].draw()
    for index in range(10):
        if goon[index].collidedWith(plasma[index])and plasma[index].visible==True:
            goon[index].moveTo(random.randint(1000,2000),653)
        
    game.update(30)    

game.over=False
while not game.over:
    game.processInput()
    endsong.play()
    end.draw()  
    game.drawText("game over",400,300,ff)
    game.drawText("you tried",410,600,ff)
    game.drawText("Press [SPACE] to Exit the game",20,700,f)
    if keys.Pressed[K_SPACE]:
        game.over=True
    
            
    game.update(30)
game.over=False
game.quit()


        




    #game.drawText("scrollx:"+str(scrollx),playerR.x,playerR.y-30)
    #game.drawText("Ypos:"+str(playerR.y),playerR.x,playerR.y-40)
        
        

        
        
    
    
