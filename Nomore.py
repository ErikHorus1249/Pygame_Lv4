import turtle
screen = turtle.Screen()
screen.bgcolor("green")
# tao nv 1
boss=turtle.Turtle()
boss.shape("turtle")
boss.penup()

# tao nv 2
huan=turtle.Turtle()
huan.shape("arrow")
huan.penup()


speed= 15
def tien ():
    tien=boss.ycor()
    boss.sety(tien + speed)
def lui ():
    lui=boss.ycor()
    boss.sety(lui - speed)
def trai ():
    trai=boss.xcor()
    boss.setx(trai - speed)
def phai ():
    phai=boss.xcor()
    boss.setx(phai + speed)


def tien2 ():
    tienHuan=huan.ycor()
    huan.sety(tienHuan + speed)
def lui2 ():
    luiHuan=huan.ycor()
    huan.sety(luiHuan - speed)
def trai2 ():
    traiHuan=huan.xcor()
    huan.setx(traiHuan-speed)
def phai2 ():
    phaiHuan=huan.xcor()
    huan.setx(phaiHuan+speed)

# nv1 ban
bullet1 =turtle.Turtle()
bullet1.shape("corcle")
bullet1.penup()
bullet1.hideturtle()
def shoot ():
    xboss=boss.xcor()
    yboss=boss.ycor()
bullet.goto(xboss,yhuan)
bullet.showturtle()
for i in range (0,50):
    bullet.forward(10)
if (bullet1.xcor()<a/2)and(bullet1.xcor()>a/2):
    bullet1.hideturtle()
    break
elif (bullet1.ycor()<-b/2)and(bullet1.ycor()>b/2):
    bullet1.hideturtle()
    break



screen.onkey(tien,"w")
screen.onkey(lui,"s")
screen.onkey(trai,"a")
screen.onkey(phai,"d")

screen.onkey(tien2,"i")
screen.onkey(lui2,"k")
screen.onkey(trai2,"j")
screen.onkey(phai2,"l")
screen.listen()




# kiem tra va cham giua 2 nv
def isConllsion (t1,t2) :
    #khoang cach giua nv1 va nv2
    d = math.sprt(math.pow(t1.xcor()-t2.xcor,2)+math.pow(t1.ycor()-t2.ycor(),2))
    if  d < 20 :
        return True
    else :
        return False
# ham kt vat khi cham bien
def boundaryChecking(t):
    if (t.xcor()<-300) or (t.xcor()>300):
        t.right(180)
        t.setposition(ramdom.randint(randow.randint(-300,300),ramdom.randint(-300,300))
    if (t.ycor()<-300) or (t.ycor()>300):
        t.right(180)
        t.setposition(ramdom.randint(randow.randint(-300,300),ramdom.randint(-300,300))