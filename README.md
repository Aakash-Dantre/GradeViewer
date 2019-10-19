# GRADEVIEWER

get your grades instantly on your terminal(for IIITH UG2 only).

uses selenium, chromedriver to scrape moodle.



## steps

- unzip chromedriver_linux64.zip

- 

  ~~~bash
  ```
  mv chromedriver /usr/bin/chromedriver
  chown root:root /usr/bin/chromedriver
  chmod +x /usr/bin/chromedriver
  ```
  ~~~

- `pip3 install selenuim`
- `pip3 install inquirer`
- `pip3 install texttable`
- run grades.py