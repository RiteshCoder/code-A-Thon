# Here are the Libraries that we imported
from datetime import datetime
import random
import time
import turtle
from turtle import *
import webbrowser
from random import *

#Setup for the Turtle Screen
wn = turtle.Screen()
setup(1200,600)
#Adding Image Background
wn.bgpic("_logo_.gif")
wn.bgcolor("blue")
time.sleep(5)
turtle.resetscreen()
turtle.clearscreen()
wn.bgcolor("blue")
#Making a Function called "main" because it is the main code to run this project
def main():
    #Making Variables for the Text styles and fonts
    style = ('Courier', 30, 'italic')
    style1 = ('Courier', 20, 'italic')
    style2 = ('Courier', 25, 'italic')
    #Adding a Name for the turtle window
    wn.title("Dads Personal Assistant Dashboard")
    #Making a function called "clearhome" so that when you click e, you got to the homepage again
    def clearhome(screen,you):
        #Telling turtle to clear the screen and reset the turtles back to their orginal postiton
        turtle.resetscreen()
        turtle.clearscreen()
        #Saying to turtle to make the background color to blue
        wn.bgcolor("blue")
        # calling the Funtction "main" to run again
        main()
    #Making a function to open the weather network
    def temps(temp,yu):
        webbrowser.open('https://www.theweathernetwork.com/ca')  
    #Telling all turtles to listen to activities such as clicking on it
    turtle.listen()
    #Seting the window length and width
    wn.setup(width=1200, height=600)
    #Making all the turtles
    music = turtle.Turtle()
    film = turtle.Turtle()
    home_chores = turtle.Turtle()
    game = turtle.Turtle()
    #Seting the turtle speed
    music.speed(10)
    game.speed(10)
    home_chores.speed(10)
    film.speed(10)
    #Seting the width of the turtles
    music.width(5)
    game.width(5)
    home_chores.width(5)
    film.width(5)
    film.pensize(5)
    

    #Making functions to open a songs in yuotube
    def song_1(yup,huj):
        webbrowser.open('https://www.youtube.com/watch?v=7QXGVOc3JN8')
    def song_2(tuyu,dftyjfj):
        webbrowser.open('https://www.youtube.com/watch?v=mRWj5knSvC0')
    def song_3(yhdgykfdsj,ehkfgjk):
        webbrowser.open('https://www.youtube.com/watch?v=2OURYl7LuaY&list=RD2OURYl7LuaY&start_radio=1')
    #functions for drawing the sections
    def song_4(whbcejh,efcvbls):
        webbrowser.open('https://www.youtube.com/watch?v=hzK0uCp4nIg&list=RD2OURYl7LuaY&index=16')
    def song_5(ejcbekfjv,dsfjhgvuerwyk):
        webbrowser.open('https://www.youtube.com/watch?v=FzLpP8VBC6E')
    def song_6(dhfbjcieufubm,sdjvbhk):
        webbrowser.open('https://www.youtube.com/watch?v=7mWd8fOG7qI')
    def song_7(jkdfhvf,weqjfgdkq):
        webbrowser.open('https://www.youtube.com/watch?v=ECV3Jck-Dt8')
    def song_8(jkdfhhf,weqjfdkq):
        webbrowser.open('https://www.youtube.com/watch?v=Uw7xmfeL8gI')
    def sudoku(jggvguk,fchf):
        webbrowser.open('https://www.websudoku.com/')
    def tictactoe(sfjkhbeddgg,efhbdsfydeo):
        webbrowser.open('https://playtictactoe.org/')
    def chess_(wqfcbhdsfvchj,fuihefjhbc):
        webbrowser.open('https://www.chess.com/play/computer')
    def sl_(ejhdbcfejh,ewcge):
        webbrowser.open('https://toytheater.com/snakes-and-ladders/')
    def sports_(sportchannel,youtube):
        def cricket(happpy,live):
            webbrowser.open('https://www.youtube.com/watch?v=oOhJTq3uYnk')
        def basket(livegme,tht):
            webbrowser.open('https://www.youtube.com/watch?v=P5_xgip67ac')
        def tennis(funlive,think):
            webbrowser.open("https://www.youtube.com/watch?v=Bc588DD6xmI")
        def soccer(go,soccr):
            webbrowser.open("https://www.youtube.com/watch?v=ZmUhQWxh1ls")
        turtle.resetscreen()
        turtle.clearscreen()
        wn.setup(width=600, height=600)
        wn.bgpic("_sport_.gif")
        home = turtle.Turtle()
        home.color("white")
        home.penup()
        home.left(90)
        home.forward(280)
        home.left(90)
        home.forward(137.5)
        home.write("Click me to go back", font=style1, align="center")
        turtle.listen()
        home.onclick(clearhome)
        cri = turtle.Turtle()
        cri.color("white")
        cri.penup()
        cri.left(90)
        cri.forward(253)
        cri.write("Click me to watch cricket", font=style1, align="center")
        cri.onclick(cricket)
        bas = turtle.Turtle()
        bas.color("white")
        bas.penup()
        bas.left(90)
        bas.forward(137.5)
        bas.left(90)
        bas.forward(120)
        bas.right(90)
        bas.write("Click me to watch Basketball", font=style1, align="center")
        bas.onclick(basket)
        
        ten = turtle.Turtle()
        ten.color("white")
        ten.penup()
        ten.right(90)
        ten.forward(275)
        ten.left(180)
        ten.write("Click me to watch Tennis", font=style1, align="center")
        ten.onclick(tennis)

        soc = turtle.Turtle()
        soc.color("white")
        soc.penup()
        soc.forward(137.5)
        soc.right(90)
        soc.forward(137.5)
        soc.left(180)
        soc.write("Click me to watch Soccer", font=style1, align="center")
        soc.onclick(soccer)

    #Making a function to show the Games section
    def games(hdgfxgh,jytcffcgfctg):
        turtle.resetscreen()
        turtle.clearscreen()
        wn.setup(width=600, height=600)
        wn.bgpic("chess1.gif")
        turtle.listen()
        turtle.onkey(clearhome, "e")
        wn.bgcolor("blue")
        home = turtle.Turtle()
        home.color("white")
        home.penup()
        home.left(90)
        home.forward(280)
        home.left(90)
        home.forward(137.5)
        home.write("Click me to go back", font=style1, align="center")
        turtle.listen()
        home.onclick(clearhome)

        sudoku_ = turtle.Turtle()
        sudoku_.color("white")
        sudoku_.penup()
        sudoku_.forward(150)
        sudoku_.left(90)
        sudoku_.forward(200)
        sudoku_.write("Click me to play Sudoku", font=style1, align="center")
        sudoku_.onclick(sudoku)
        
        tic = turtle.Turtle()
        tic.color("white")
        tic.penup()
        tic.left(180)
        tic.forward(150)
        tic.right(90)
        tic.forward(200)
        tic.write("Click me to play TTC", font=style1, align="center")
        tic.onclick(tictactoe)

        chess = turtle.Turtle()
        chess.color("white")
        chess.penup()
        chess.left(180)
        chess.forward(150)
        chess.left(90)
        chess.forward(200)
        chess.write("Click me to play Chess", font=style1, align="center")
        chess.forward(5)
        chess.left(180)
        chess.onclick(chess_)

        sl = turtle.Turtle()
        sl.color("white")
        sl.penup()
        sl.forward(150)
        sl.right(90)
        sl.forward(200)
        sl.left(180)
        sl.write("Click me to play SNL", font=style1, align="center")
        sl.onclick(sl_)
    #defining and links for the songs
    def ytsongs(io,so):
        turtle.resetscreen()
        turtle.clearscreen()
        wn.setup(width=600, height=600)
        turtle.listen()
        turtle.onkey(clearhome, "e")
        home = turtle.Turtle()
        home.color("white")
        home.penup()
        home.left(90)
        home.forward(280)
        home.left(90)
        home.forward(150)
        home.left(90)
        home.forward(50)
        home.right(90)
        home.forward(18)
        home.write("Click me to go back", font=style1, align="center")
        turtle.listen()
        home.onclick(clearhome)

        wn.bgcolor("dodger blue")
        wn.bgpic("music1.gif")
        song1 = turtle.Turtle()
        song1.color("white")
        song1.penup()
        song1.left(180)
        song1.setpos(-137.5,0)
        song1.right(90)
        song1.forward(137.5)
        song1.write("Naalai Namathe", font=style1, align="center")
        song1.onclick(song_1)
        song2 = turtle.Turtle()
        song2.color("white")
        song2.penup()
        song2.left(90)
        song2.forward(275)
        song2.write("Putham Pudhu Kaalai", font=style1, align="center")
        song2.onclick(song_2)
        
        song3 = turtle.Turtle()
        song3.color("white")
        song3.penup()
        song3.forward(137.5)
        song3.left(90)
        song3.forward(137.5)
        song3.write("Madai Thirandhu Thavum", font=style1, align="center")
        song3.onclick(song_3)

        song4 = turtle.Turtle()
        song4.color("white")
        song4.penup()
        song4.right(90)
        song4.forward(275)
        song4.write("Tholvi Nilaiye Ninaithal", font=style1, align="center")
        song4.left(180)
        song4.onclick(song_4)

        song5 = turtle.Turtle()
        song5.color("white")
        song5.penup()
        song5.forward(137.5)
        song5.right(90)
        song5.forward(137.5)
        song5.write("Vaaranam Aayiram", font=style1, align="center")
        song5.left(180)
        song5.onclick(song_5)

        song6 = turtle.Turtle()
        song6.color("white")
        song6.penup()
        song6.left(180)
        song6.forward(137.5)
        song6.left(90)
        song6.forward(137.5)
        song6.write("Vaadi Pulla Vaadi", font=style1, align="center")
        song6.left(180)
        song6.onclick(song_6)

        song7 = turtle.Turtle()
        song7.color("white")
        song7.penup()
        song7.left(180)
        song7.forward(137.5)
        song7.write("Natpe Thunai", font=style1, align="center")
        song7.right(90)
        song7.onclick(song_7)

        song8 = turtle.Turtle()
        song8.color("white")
        song8.penup()
        song8.forward(137.5)
        song8.left(90)
        song8.write("Anjaan - Ek Do Teen Video", font=style1, align="center")
        song8.onclick(song_8)
        turtle.mainloop()
    #Making the temp/time page
    def time_temp(i,q):
        turtle.resetscreen()
        turtle.clearscreen()
        wn.setup(width=600, height=600)
        wn.bgpic("timetemp1.gif")
        turtle.listen()
        turtle.onkey(clearhome, "e")
        #today = date.today()
        game.color("white")
        home = turtle.Turtle()
        home.color("black")
        home.penup()
        home.left(90)
        home.forward(280)
        home.left(90)
        home.forward(150)
        home.write("Click me to go back", font=style1, align="center")
        turtle.listen()
        home.onclick(clearhome)
        
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.speed(0)
        pen.pensize(3)
        #Making a function to make a clock
        def clock(h, m, s, pen):
            pen.up()
            pen.goto(0, 210)
            pen.setheading(180)
            pen.color("black")
            wn.tracer(0)
            pen.pendown()
            pen.circle(210)
            pen.penup()
            pen.goto(0,0)
            pen.setheading(90)

            for _ in range(12):
                pen.fd(190)
                pen.pendown()
                pen.fd(20)
                pen.penup()
                pen.goto(0,0)
                pen.rt(30)
            pen.penup()
            pen.goto(0,0)
            pen.color("blue")
            pen.setheading(90)
            angle = (h / 12) * 360
            pen.rt(angle)
            pen.pendown()
            pen.fd(100)
            
            pen.penup()
            pen.goto(0,0)
            pen.color("black")
            pen.setheading(90)
            angle = (m / 60) * 360
            pen.rt(angle)
            pen.pendown()
            pen.fd(180)

            pen.penup()
            pen.goto(0,0)
            pen.color("gold")
            pen.setheading(90)
            angle = (s / 60) * 360
            pen.rt(angle)
            pen.pendown()
            pen.fd(120)
            
        while True:
            h = int(time.strftime("%H"))
            m = int(time.strftime("%M"))
            s = int(time.strftime("%s"))
            clock(h, m, s, pen)
            wn.update()
            time.sleep(1)
            pen.clear()
            pen.hideturtle()
            #This is how when we click the turtle, it goes to the weather network to see the time
            temp = turtle.Turtle()
            temp.penup()
            temp.color("black")
            temp.forward(280)
            temp.setpos(0,250)
            temp.color("black")
            temp.write("Click me to see temprature", font=style1, align="center")
            temp.onclick(temps)
            
    #Making a function to make the music section
    def music_button():
        wn.register_shape("music10.gif")
        music10 = turtle.Turtle()
        music10.shape("music10.gif")
        music10.penup()
        music10.forward(275)
        music10.left(90)
        music10.forward(137.5)
        #music.hideturtle()
        music.color("white")
        music.penup()
        music.forward(137.5)
        music.left(90)
        music.pendown()
        for s in range(4):
            music.forward(275)
            music.right(90)
        music.right(90)
        music.forward(137.5)
        music.penup()
        music.left(90)
        music.forward(137.5)
        music.write('Music/Songs', font=style, align='center')

    music_button()
    def health0():
        def h(sghius,fvh):
            
            def bmi_(dfjhbs,hiy):
                h=float(input('Enter your height (in m): '))
                w=float(input('Enter your weight (in kg): '))

                BMI =round(w/(h**2))
                print('You have a BMI of: {0} and you are ' .format(BMI), end='')

                if BMI < 18.5:
                    print('underweighted')
                elif BMI >= 18.5 and BMI < 25:
                    print('ideal')
                elif BMI >=25 and BMI < 30:
                    print('overweighted')
                elif BMI >= 30:
                    print('obese')
            def heart_(check,heartrate):
                webbrowser.open('https://onlineheartrate.com/')
            turtle.resetscreen()
            turtle.clearscreen()
            wn.setup(width=600, height=600)
            wn.bgpic("_health_.gif")
            home = turtle.Turtle()
            home.color("black")
            home.penup()
            home.left(90)
            home.forward(280)
            home.left(90)
            home.forward(137.5)
            home.write("Click me to go back", font=style1, align="center")
            turtle.listen()
            home.onclick(clearhome)
            bmi = turtle.Turtle()
            bmi.penup()
            bmi.color("black")
            bmi.left(90)
            bmi.forward(250)
            bmi.write("BMI Calculator", font=style1, align="center")
            turtle.listen()
            bmi.onclick(bmi_)
            heart = turtle.Turtle()
            heart.penup()
            heart.right(90)
            heart.forward(275)
            heart.left(180)
            heart.write("Click to view heart rate", font=style1, align="center")
            turtle.listen()
            heart.onclick(heart_)
        wn.register_shape("health_.gif")
        health = turtle.Turtle()
        health.shape("health_.gif")
        health.penup()
        health.right(90)
        health.forward(137.5)
        
        health1 = turtle.Turtle()
        health1.color("white")
        health1.width(5)
        health1.forward(137.5)
        health1.right(90)
        for x in range(4):
            health1.forward(275)
            health1.right(90)
        health1.right(90)
        health1.forward(137.5)
        health1.left(90)
        health1.penup()
        health1.forward(137.5)
        health1.left(180)
        health1.write('Health', font=style, align='center')
        turtle.listen()
        health1.onclick(h)
    health0()
    #Making a function to make the games section
    def film_button():
        wn.register_shape("chess2.gif")
        chess2 = turtle.Turtle()
        chess2.shape("chess2.gif")
        chess2.penup()
        chess2.left(180)
        chess2.forward(275)
        chess2.left(90)
        chess2.forward(137.5)
        #film.hideturtle()
        film.color("white")
        film.penup()
        film.left(180)
        film.forward(137.5)
        film.left(90)
        film.pendown()
        for s in range(4):
            film.forward(275)
            film.right(90)
        
        film.forward(137.5)
        film.penup()
        film.right(90)
        film.forward(137.5)
        film.right(90)
        film.write('Games/Trivia', font=style, align='center')
        #film.left(180)
        
    film_button()
    #Making a function to make the money planner
    def home_button():
        #home_chores.hideturtle()
        wn.register_shape("money10.gif")
        money10 = turtle.Turtle()
        money10.shape("money10.gif")
        money10.penup()
        money10.forward(275)
        money10.right(90)
        money10.forward(137.5)
        home_chores.color("white")
        home_chores.penup()
        home_chores.forward(137.5)
        
        for s in range(4):
            home_chores.pendown()
            home_chores.forward(275)
            home_chores.right(90)
        home_chores.right(90)
        home_chores.forward(137.5)
        home_chores.penup()
        home_chores.left(90)
        home_chores.forward(137.5)
        home_chores.write('Monthly Planner', font=style, align='center')
        home_chores.left(90)
    def sports():
        #home_chores.hideturtle()
        wn.register_shape("sports.gif")
        sport0 = turtle.Turtle()
        sport0.shape("sports.gif")
        sport0.penup()
        sport0.left(90)
        sport0.forward(137.5)
        sport = turtle.Turtle()
        sport.color("white")
        sport.width(5)
        sport.penup()
        sport.left(180)
        sport.pendown()
        sport.forward(137.5)
        sport.right(90)
        for q in range(4):
            sport.forward(275)
            sport.right(90)
        sport.right(90)
        sport.forward(137.5)
        sport.left(90)
        sport.penup()
        sport.forward(137.5)
        sport.write("Sports", font=style, align='center')
        turtle.listen()
        sport.onclick(sports_)
        
        
    sports()
    home_button()
    #Making a function to make the time and temp section
    def game_button():
        #game.hideturtle()
        wn.register_shape("timetemp2.gif")
        weather3 = turtle.Turtle()
        weather3.shape("timetemp2.gif")
        weather3.penup()
        weather3.left(180)
        weather3.forward(275)
        weather3.right(90)
        weather3.forward(137.5)
        game.color("white")
        game.penup()
        game.left(180)
        game.forward(137.5)
        game.pendown()
        for s in range(4):
            game.forward(275)
            game.right(90)
        game.right(90)
        game.forward(137.5)
        game.penup()
        game.left(90)
        game.forward(137.5)
        game.write('Temperature/Time', font=style2, align='center')
        game.right(90)
    game_button()
    #This function will run what to do when you click on the monthly planner turtle
    def planner(pykd,dhjk):
        turtle.resetscreen()
        turtle.clearscreen()
        wn.setup(width=600, height=600)
        turtle.listen()
        turtle.onkey(clearhome, "e")
        home = turtle.Turtle()
        home.color("white")
        home.penup()
        home.left(90)
        home.forward(280)
        home.right(90)
        home.forward(170)
        home.right(90)
        home.forward(35)
        home.right(90)
        home.write("Click me to go back", font=style1, align="center")
        turtle.listen()
        home.onclick(clearhome)

        wn.bgcolor("light pink")
        wn.bgpic("money.gif")
        
        
        #all the expences
        car_loan = int(input("Enter  car loan amount: "))
        house_loan = int(input("Enter house loan amount: "))
        water_bill = int(input("Enter water bill amount: "))
        electric_bill = int(input("Enter electric bill amount: "))
        groceries = int(input("Enter grocery expence: "))
        internet = int(input("Enter internet expence: "))
        landline = int(input("Enter landline expence: "))
        furnace_gas_bill = int(input("Enter furnace gas bill expence: "))
        morgage_protection = int(input("Enter morgage protection expence: "))
        home_insurance = int(input("Enter home insurance expence: "))
        sim_card = int(input("Enter sim card bill amount: "))
        car_gas = int(input("Enter car gas expence: "))
        hot_water_rental = int(input("Enter hot water rental bill: "))
        other_expences = int(input("Enter other expences: "))
        car_loan_insurance = int(input("Enter car loan insurance: "))
        resp = int(input("Enter resp amount: "))
        rrsp = int(input("Enter rrsp amount: "))
        credit_card = int(input("Enter credit card expences: "))
        salary = int(input("Enter salary amount: "))
        amount = int(input("Enter savings amount: "))
        expectedamount = int(input("Enter  amount"))
        month = 30
        year = 12
        daily = amount * expectedamount
        monthly = daily * month
        yearly = monthly * year
        total = credit_card + rrsp + resp + car_loan_insurance + other_expences + hot_water_rental + car_gas + sim_card + home_insurance + morgage_protection + furnace_gas_bill + landline + internet + groceries + electric_bill + water_bill + house_loan + car_loan 
        saving = salary - total
        
        

        # to write all the expences down oon the turtle window
        expence = turtle.Turtle()
        expence.color("white")
        expence.penup()
        expence.left(90)
        expence.forward(275)
        expence.write("Car Loan = $" + str(car_loan), font=style1, align='center')
        expence.left(90)
        expence.forward(180)
        expence.write("House Loan = $" + str(house_loan), font=style1, align='center')
        expence.left(90)
        expence.forward(35)
        expence.write("Water Bill = $" + str(water_bill), font=style1, align='center')
        expence.forward(35)
        expence.write("Electric Bill = $" + str(electric_bill), font=style1, align='center')
        expence.forward(35)
        expence.write("Groceries = $" + str(groceries), font=style1, align='center')
        expence.forward(35)
        expence.write("Internet = $" + str(internet), font=style1, align='center')
        expence.forward(35)
        expence.write("Landline = $" + str(landline), font=style1, align='center')
        expence.forward(35)
        expence.write("Furnace = $" + str(furnace_gas_bill), font=style1, align='center')
        expence.forward(35)
        expence.write("Loan Protect = $" + str(morgage_protection), font=style1, align='center')
        expence.forward(35)
        expence.write("Home Insure = $" + str(home_insurance), font=style1, align='center')
        expence.forward(35)
        expence.write("SIM Card = $" + str(sim_card), font=style1, align='center')
        expence.forward(35)
        expence.write("Car Gas = $" + str(car_gas), font=style1, align='center')
        expence.forward(35)
        expence.write("Hot Water = $" + str(hot_water_rental), font=style1, align='center')
        expence.forward(35)
        expence.write("Other Expence = $" + str(other_expences), font=style1, align='center')
        expence.forward(35)
        expence.write("Credit Card = $" + str(credit_card), font=style1, align='center')
        expence.forward(35)
        expence.write("Car Insure = $" + str(car_loan_insurance), font=style1, align='center')
        expence.forward(35)
        expence.left(90)
        expence.write("RESP = $" + str(resp), font=style1, align='center')
        expence.forward(180)
        expence.write("RRSP = $" + str(rrsp), font=style1, align='center')
        expence.forward(180)
        expence.write("Salary = $" + str(salary), font=style1, align='center')
        expence.left(90)
        expence.forward(35)
        expence.write("Savings = $" + str(saving), font=style1, align='center')
        expence.forward(35)
        expence.write("Total Expenses = $" + str(total), font=style1, align='center')
        expence.forward(35)
        expence.write("Daily = $" + str(daily), font=style1, align='center')
        expence.forward(35)
        expence.write("Monthly = $" + str(monthly), font=style1, align='center')
        expence.forward(35)
        expence.write("Yearly = $" + str(yearly), font=style1, align='center')
        turtle.listen()
        turtle.mainloop()
        


    #telling when you click any turtle on the page, to do what it is supposed to do
    turtle.onkey(clearhome, "e")
    film.onclick(games)
    game.onclick(time_temp)
    music.onclick(ytsongs)
    home_chores.onclick(planner)
    turtle.mainloop()

#Calling the function "main" so that the code runs
main()
