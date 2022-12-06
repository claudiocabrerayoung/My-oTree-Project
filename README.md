# My-oTree-Project
Este repositorio albergará los códigos asociados a mi primer proyecto de oTree, el cual consistirá en crear un juego de confianza (trust game) e implementarlo en un entorno de producción.

## What I did and did not accomplish during my project development

### First task 
#### Backend 

**I was able to...**

- I succesfully randomized the pairing of participants in every round 
- I was able to assign the role of the participants at random in each round (remember there should always be one trustor and one trustee per group), which can be verified if the number of participants is increased to a number larger than and multiple of 2.

**I was unable to...**

- I was NOT able to make any of the randomizations session-configurable. At the beginning, I opted to use in references to the SESSIONS_CONFIG list of dictionaries (actually one dict. as I used only one app) in the element defined under the constant class that would've been useful to get configurable (i.e., number of rounds, number of participants, endowment, multiplier). However, this approach proved to be incorrect, in as it was just a transition of manual dependency from the '_init_.py' to the "settings.py" archive.

#### Frontend

- I created the tables partially. Specifically, I did include correctly the round number and the information about that player who was watching the screen, but not the information for the other participant. In other words, each player was able to watch their results, but no the one of the other one. The reason for this was that I didn't come up with a way to call the secondary player (for each role's case). as I was my approach was to implement a if-statement that had as condition to display a corespondent screen to each player according to their id, and I didn't get any valid identifier to call the secondary player.

- I implement the slider only for the Trustor, as the Trustees amount had as a upper bound the 'sent_amount_BY_P1 * MULTIPLIER' amount, and I couldn't apply a list(range()) conversion to such part in that such part was neither an integer nor a string, but a oTree-column and didn't accept conversions as far as I know.

### Second task

**I was able to...**

- I installed PostgreSQL and psycopg2. I had to reset my PC, though, since the installer showed me the following message:

_Problem running pos-install step. Installation may not complete correctly. The database cluster initialisation failed._ 

and was indeed not correctly installed. Everything was fine after the reset.

- I created the the postgres database and named it myGame_DB (I will upload a file with the image in the repository).


**I was unable to...**

- I was totally UNABLE to connect such database to the project. I simply didn't manage to understand where to create the environment variables and the specific way in which they needed to be structured.


## Third task

I accomplished every sub-task required. 




