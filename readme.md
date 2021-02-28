This is the freshers' assignment given by DevClub IITD.

# Task 1: Moodle Auto-Login

This task requires to open iitd moodle login page, accept credentials and solve captcha and login automatically.

The script for this task is in `.\Moodle` directory.

### Running the script:
 From the `.\Moodle` directory, run the following terminal command:

````python moodleLogin.py ````

After succesful loading up of page, enter the username and password in the terminal prompt whivh will be shown.
Password is accepted using getpass library, and hence will not be visible while typing.

# Task 2: Codeforces Problem Scraper

This task requires to scrap all the problems of a particular contest number being provided as argument.

The script for this task is in `.\Codeforces` directory.

### Running the script:
From the `.\Codeforces` directory, run the following terminal command:
````python fetch_round.py <contest_no>````
where 'contest_no' is a valid integer contest number.

After a successful run, a new directory will be created in the `.\Codeforces` directory with the name of the contest number and containing sub-directories for each problem separately. Each problem's sub-directory contains an image of problem and sample input and output as text files.