# Test-Automation-with-Selenium-Python
About This is a sample test Automation Framework utilizing selenium with Python built to automate 7 tests for https://www.demoblaze.com/.

design pattern followed is Page Object Model. Browsers used are chrome, firefox, ie and edge

# Requirements 

Python                         3.9.4    

pytest                         6.2.3

pytest-depends                 1.0.1

pytest-forked                  1.3.0

pytest-html                    3.1.1

pytest-metadata                1.11.0

pytest-order                   0.11.0

pytest-xdist                   2.2.1

selenium                       3.141.0

# How To Run

run command   py.test --html=results/report.html --browser_name={browser} -m {tag} -n 2 -v

browser can take values chrome or firefox

tag can take values regression or sanity

