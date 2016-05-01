#This file holds all of the CREATE TABLE statments to build the database

CREATE TABLE Game (
  Name  VARCHAR(255) NOT NULL,
  Console  VARCHAR(255) NOT NULL,
  PRIMARY KEY(Name)
);


CREATE TABLE Event (
  Event_id INT(9),
  Evenet_date DATE NOT NULL,
  Prize_money  INT,
  Max_participants  INT,
  Location VARCHAR(255) NOT NULL,
  Start_time DATE NOT NULL,
  Is_streaming BOOLEAN NOT NULL,
  Provides_stream BOOLEAN NOT NULL,
  PRIMARY KEY (Event_id)
);

CREATE TABLE Player (
  Username VARCHAR(20),
  F_name VARCHAR(255),
  L_name VARCHAR(255),
  Location VARCHAR(255),
  Ranking INT,
  PRIMARY KEY (Username)
);

CREATE TABLE Event_staff (
  Staff_id INT(9),
  Event_id INT(9),
  F_name VARCHAR(255),
  L_name VARCHAR(255),
  PRIMARY KEY(Staff_id),
  FOREIGN KEY(Event_id) REFERENCES Event(Event_id)
);

CREATE TABLE Hosts (
  Event_id INT(9) NOT NULL,
  Game_name VARCHAR(255) NOT NULL,
  PRIMARY KEY(Event_id, Game_name),
  FOREIGN KEY(Event_id) REFERENCES Event(Event_id),
  FOREIGN KEY(Game_name) REFERENCES Game(Name)
);

CREATE TABLE Competes_in (
  Event_id INT(9) NOT NULL,
  Username VARCHAR(20) NOT NULL,
  PRIMARY KEY(Event_id, Username),
  FOREIGN KEY(Event_id) REFERENCES Event(Event_id),
  FOREIGN KEY(Username) REFERENCES Player(Username)
);

CREATE TABLE Tournament_organizers (
  Staff_id INT(9) NOT NULL,
  Experience INT,
  PRIMARY KEY(Staff_id),
  FOREIGN KEY(Staff_id) REFERENCES Event_staff(Staff_id)
);

CREATE TABLE Helpers (
  Staff_id INT(9) NOT NULL,
  Competency BOOLEAN NOT NULL,
  PRIMARY KEY(Staff_id),
  FOREIGN KEY(Staff_id) REFERENCES Event_staff(Staff_id)
);

CREATE TABLE Stream_operators (
  Staff_id INT(9) NOT NULL,
  Program_knowledge VARCHAR(255),
  Bring_equipment BOOLEAN NOT NULL,
  PRIMARY KEY(Staff_id),
  FOREIGN KEY(Staff_id) REFERENCES Event_staff(Staff_id)
);

CREATE TABLE Controllers (
  Controller_name VARCHAR(255),
  Game_name VARCHAR(255) NOT NULL,
  PRIMARY KEY(Controller_name, Game_name),
  FOREIGN KEY(Game_name) REFERENCES Game(Name)
);

CREATE TABLE Main_characters (
  Character_name VARCHAR(255) NOT NULL,
  Username VARCHAR(20) NOT NULL,
  PRIMARY KEY(Character_name, Username),
  FOREIGN KEY(Username) REFERENCES Player(Username)
);
