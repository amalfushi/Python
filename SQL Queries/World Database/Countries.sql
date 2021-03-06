USE world;
#return every country with slovene as a language
-- SELECT countries.name, languages.language, languages.percentage
-- From countries
-- LEFT JOIN languages
-- ON countries.id = languages.id
-- WHERE languages.language = 'slovene';

#return the countries and the number of cities ordered by most
-- SELECT countries.name, COUNT(cities.id) AS cities
-- FROM countries
-- LEFT JOIN cities
-- ON countries.id = cities.country_id
-- GROUP BY countries.id
-- ORDER BY cities DESC;

#all cities in mexico with a pop >500,000
-- SELECT cities.name, cities.population
-- FROM cities
-- LEFT JOIN countries
-- ON cities.country_code = countries.code
-- WHERE countries.name = 'Mexico' AND cities.population > 500000
-- ORDER BY cities.population DESC;

#All languages in each countrie with a percentage greater than 89%
-- SELECT countries.name, languages.language, languages.percentage
-- FROM countries
-- LEFT JOIN languages
-- ON countries.id = languages.country_id
-- WHERE languages.percentage > 89
-- ORDER BY languages.percentage DESC;

# all countries with surface area below 501 and pop greater than 100,000
-- SELECT countries.name, countries.surface_area, countries.population
-- FROM countries
-- WHERE countries.surface_area < 501 AND countries.population > 100000

#6 all constitutional monarchies with a capitol greater than 200 
#and a life expectancy greater than 76
-- SELECT name, government_form, capital, life_expectancy
-- FROM countries
-- WHERE government_form = "Constitutional Monarchy" AND capital > 200 AND life_expectancy > 76


#7 all cities of argentina inside the buenos aires district with a population
# greater than 500,000.  Should return Country name, city name, district, and pop
-- Select countries.name, cities.name, cities.district, cities.population
-- FROM countries
-- LEFT JOIN cities
-- ON countries.id = cities.country_id
-- WHERE countries.name = 'Argentina' AND cities.district = 'Buenos Aires' AND cities.population > 500000

#8 summary of countries in each reagion.  display name of region and number of countries
# arrange by number of countries descending
-- SELECT region, count(id) AS countries
-- FROM countries
-- GROUP BY countries.region
-- ORDER BY countries DESC;
