<h3><u>PASSWORD GENERATOR:</u></h3>
<br>

This project generates passwords using four different methods.  It produces
five examples of each style so that the one that looks best can be used.  The
methods provided are:<br>

<b><u>random</u></b>: generates a character string of random length, between a minimum
and maximum, that has a randomly generated set of upper case letters, lower
case letters, digits and special characters.  The range of each type of 
character is configurable via global settings at the top of the script.<br>

<b><u>2 Words</u></b>: generates a password from two words of the English language, taken
at random from the nltk (Natural Language Toolkit) python module word list,
plus a 3-4 digit number, separated by a randomly chosen delimiter.<br>

<b><u>2 Opposing Words</u></b>: Generates a password using two opposing words as listed in
opposites.txt, along with a 3-4 digit number and separated by a randomly chosen
delimiter.<br>

<b><u>2 Nerfed Opposing Words</u></b>: Generates a password by choosing two opposing words
as listed in opposites.txt and nerfing them with letters and characters, for 
instance by replacing some 'i' characters with a 1 (one), some 'o' characters
with a 0, etc.

Studies show that passwords that are completely random characters as in the
first method are hardest to hack.  Other studies show that related words separated
by a delimiter are the easiest to remember, so the first method would be most
suitable for secure accounts like a bank, while the other, two word methods
would be best where less security is needed and the need to be able to remember
the password is greater, such as a computer login.

<br>
<br>
The output, as text in a DOS window, is as shown below.

**GENERATED PASSWORDS**:

  | TYPE               | PASSWORD                      |
  |--------------------|-------------------------------|
  | Random:            | 5e$4cyC                       |
  |                    | fY,yT3Vk                      |
  |                    | rj3%9yBCjio6                  |
  |                    | XF8za1W-J$f5\6                |
  |                    | TN9hI;rt/ReZiehF              |
  |                    | Yc4unwRdrk:xq*kCuo4to         |
  | 2 Words:           | poverty_nu_513                |
  |                    | slavikite-Hobbesian-6054      |
  |                    | superexaminer;stercorite;5138 |
  |                    | servitor;Byblis;1066          |
  |                    | quinte_lithosis_6356          |
  | 2 Opposing Words:  | north/south/3674              |
  |                    | separate;connect;3440         |
  |                    | end-begin-3377                |
  |                    | noon-midnight-7794            |
  |                    | foreigner-native-7089         |
  | 2 Nerfed Opposing: | f@ilure-5ucc3ss               |
  |                    | hum@ne-cru3l                  |
  |                    | l@nd-wa7er                    |
  |                    | en3my/fri3nd                  |
  |                    | lif3:de@7h                    |



