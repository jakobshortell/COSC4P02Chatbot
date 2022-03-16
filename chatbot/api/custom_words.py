import json
import hashlib
import os
from scrapers.clubs import ClubScraper
from scrapers.departments import DepartmentScraper
from scrapers.courses import CoursesScraper
from scrapers.programs import ProgramScraper
from scrapers.restaurant import RestaurantScraper
from scrapers.buildings import BuildingScraper

departments = DepartmentScraper().get()
clubs = ClubScraper().get()
courses = CoursesScraper().get()
programs = ProgramScraper().get()
restaurant = RestaurantScraper().get()
buildings = BuildingScraper().get()


f = open("temp.txt", "w")

for i in departments:
    words = departments[i]['name'].lower()
    words = words.replace(' ', '\n')
    f.write(words + '\n')

for i in clubs:
    words = clubs[i]['name'].lower()
    words = words.replace(' ', '\n')
    f.write(words + '\n')

for i in courses:
    words = courses[i]['program_code'].lower()
    words = words.replace(' ', '\n')
    f.write(words + '\n')

for i in programs:
    words = programs[i]['name'].lower()
    words = words.replace(' ', '\n')
    f.write(words + '\n')

for i in restaurant:
    words = restaurant[i]['name'].lower()
    words = words.replace(' ', '\n')
    f.write(words + '\n')

for i in buildings:
    words = buildings[i]['code'].lower()
    words = words.replace(' ', '\n')
    f.write(words + '\n')

f.close()

line_hash = set()

f = open("customWords.txt", "w")

for line in open("temp.txt", "r"):
  hash_value = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
  if hash_value not in line_hash:
    f.write(line)
    line_hash.add(hash_value)

f.close()

os.remove("temp.txt")


