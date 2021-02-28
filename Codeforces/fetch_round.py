from selenium import webdriver
import sys
import os

PATH = "..\chromedriver.exe"
driver = webdriver.Chrome(PATH)

contest = sys.argv[1]

driver.get("https://codeforces.com/contest/" + contest + "/problems")

problems = driver.find_elements_by_class_name("problemindexholder")
noOfProblems = len(problems)

for i in range(0,noOfProblems):
    problem = problems[i]
    problemIndex = problem.get_attribute("problemindex")
    dirPath = ".\\" + contest + "\\" + problemIndex
    os.makedirs(dirPath)
    problem.screenshot(dirPath + "\\problem.png")
    inputs = problem.find_elements_by_class_name("input")
    outputs = problem.find_elements_by_class_name("output")
    for j in range(0, len(inputs)):
        file = open(dirPath + "\\input" + str(j+1) + ".txt", "w")
        file.write(inputs[j].find_element_by_tag_name("pre").text)
        file.close()
        file = open(dirPath + "\\output" + str(j+1) + ".txt", "w")
        file.write(outputs[j].find_element_by_tag_name("pre").text)
        file.close()

