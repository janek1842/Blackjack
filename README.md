# Installation and run :file_folder:

If some extensions are missing please type: 

```
pip install -r requirements.txt
```
To run the game please type:

```
python menu.py
```
## Admin credentials:

```
Login: adminadmin
Password: adminadmin
```
## Media sources

Avatars and playing cards were taken from:

- https://game-icons.net/
- https://commons.wikimedia.org/wiki/Main_Page

# Project description :hearts: :clubs: :diamonds: :spades:

This project is about a popular card game blackjack- *in polish oczko*. It was made with Python3 with the use of Qt which is tool for designing and building graphical user interfaces (GUIs) with Qt Widgets. There is also not too big database based on SQLite.  

## What are the rules :grey_question:

The main goal for the player is to reach 21 points (blackjack) or to get as close as possible to this value but not to go beyond that! To do this, player is taking cards from the decks located in the middle of the table. Every card has its own value which are summed up for every user. Player has also possibility to pass the game to stop it. 

To add a bit more excitement, the game is being played for money. At the beginning players are betting for how much they want to play and this sum is added or taken from their overall money at the end (depending on their result).   

## How to play :grey_question: 

To begin with, please run the game. In the left panel you might see five places where you can login or create a new account to play this game. If you login properly, you are allowed to change your account features like avatar, description or password. After that, you will get similar view. 

<img width="1261" alt="mainPanel" src="https://user-images.githubusercontent.com/56030577/145471598-ef6911f8-5e18-49a2-822f-199cab0fd9f6.png">

If you want to adjust you profile features please click **Manage**.

<img width="1262" alt="ManageView" src="https://user-images.githubusercontent.com/56030577/145471943-f72a0ca2-5058-42ec-94cb-d80c6f7e471e.png">

This app has the possibility to view that ranking (specified by money) and also more detailed statistics of every user. To view this please click **RANKING/STATISTICS** button to show this panel.

After getting to know with all these features you can click **PLAY** button to specify parameters of the game. Here you can choose maximum 5 and minimum 2 players from currently logged users and Artificial Intelligence represented by your computer with specified level of advancement (easy, medium, hard). Moreover, you can specify layout of your cards from two possible options and number of decks (in order to harden guessing remaining cards). There is also option to change the time interval between player moves.  

<img width="1264" alt="optionpanel" src="https://user-images.githubusercontent.com/56030577/145474461-24371e88-d218-43d0-90c0-117a302242b7.png">

If you are ready, you can click **START GAME** to begin adventure with blackjack. :rocket:

Now, you are allowed to enter your **BET** - the amount of money based on which your final result will be calculated. After that, the game starts and you decide whether to **HIT** (take next card) or **STAND** (pause). Observe your score and frame color to control your status **(WAIT/LOSE/WIN/TURN)**. After each round, you can **REPLAY** your game to enjoy it once more!  

![image](https://user-images.githubusercontent.com/56030577/148691415-23ec09bf-4f37-4c75-bb3b-9c1ba1d46187.png)

![image](https://user-images.githubusercontent.com/56030577/148691712-46f0bf8e-a953-4845-bcd6-1773c7759bdf.png)

# Compatibility :computer:

This game has been tested positively on Windows 10 and Linux Arch OS. 












