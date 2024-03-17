# Test-Automation-with-Selenium-Python
About This is a sample test Automation Framework utilizing selenium with Python built to automate 7 tests for https://www.demoblaze.com/.

design pattern followed is Page Object Model. Browsers used are chrome, firefox, ie and edge

# Requirements 

Python                         3.10.10   

pytest                         7.2.2

pytest-depends                 1.0.1

pytest-forked                  1.6.0

pytest-html                    4.1.1

pytest-metadata                3.1.1

pytest-order                   1.2.0

pytest-xdist                   3.5.0

selenium                       4.8.3

# How To Run

run command   py.test --html=results/report.html --browser_name={browser} -m {tag} -n 2 -v

browser can take values chrome,firefox,ie,edge

tag can take values regression or sanity

