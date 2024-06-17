# Restaurant Simulation

## Description

This project is a console restaurant simulation where the user can set the amount of tables in it, and the amount of min and max time that the clients will stay on the tables. 
Once the settings are done, the clients will start to enter the restaurant and use the tables. The number of clients in each group of clients can vary, for example, is more likely that a bigger group will enter at night compared to the morning. 
If all tables are being used clients can wait, but if the wait line is to big, they will go away. 
The program locates the clients in a logical way, trying to match the sizes of the tables with the sizes of the groups of clients. 
The program will finish when the restaurant closes, and will show the stats. 
Take in mind that the program is for default set to run very fast, so you can get to the end of the day as soon as possible and see the stats. This can be changed by incrementing the value in the time.sleep() call.
The program prints everything that happends in the simulation. 

## Features

- Real-time client flow.
- Different sizes of tables and clients. 
- Different tendencies in size and staying time in different time frames of the day.
- Different volume of clients in the different time frames of the day.

## Technologies Used

- **Python**: For the core logic and simulation.
- **Threading**: To handle real-time updates.
- **Time**: To be able to sleep the program in the loop
- **Random**: To generate random values.

## Installation

To run this project, you need to have Python installed. Follow these steps:

1. Clone the repository:
    ```bash
    git clone 
    ```https://github.com/LeonardoEnriqueVila/Restaurant
2. Navigate to the project directory:
    ```bash
    cd Restaurant
    ```

## Usage

To start the simulation, run the following command:
```bash
python clock.py