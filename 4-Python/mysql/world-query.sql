/* Queries */
use world;
/*
1. What query would you run to get all the countries that speak Slovene? 
Your query should return the name of the country, language and language percentage. 
Your query should arrange the result by language percentage in descending order. (1)
*/
select c.name, l.language, l.percentage
from countries as c
join languages as l on c.id = l.country_id
order by l.percentage desc;
/*
2. What query would you run to display the total number of cities for each country? 
Your query should return the name of the country and the total number of cities. 
Your query should arrange the result by the number of cities in descending order. (3)
*/
select countries.name, count(cities.id)
from countries
join cities 
on countries.id = cities.country_id
order by count(cities.id) desc;
/*
3. What query would you run to get all the cities in Mexico with a population of greater than 500,000? 
Your query should arrange the result by population in descending order. (1)
*/
select cities.name, cities.population 
from countries
join cities 
on countries.id = cities.country_id
where countries.name='Mexico'
and cities.population>500000
order by cities.population desc;
/*
4. What query would you run to get all languages in each country with a percentage greater than 89%? 
Your query should arrange the result by percentage in descending order. (1)
*/
select countries.name, languages.language, languages.percentage
from countries
join languages on countries.id = languages.country_id
where languages.percentage>89
order by languages.percentage desc, languages.language, countries.name;
/*
5. What query would you run to get all the countries with Surface Area below 501 
and Population greater than 100,000? (2)
*/
SELECT countries.name, countries.surface_area, countries.population
FROM countries
WHERE countries.surface_area < 501 
AND countries.population > 100000;
/*
6. What query would you run to get countries with only Constitutional Monarchy with a capital greater than 200 and a life expectancy greater than 75 years? (1)
*/
SELECT countries.name, countries.government_form, countries.capital
FROM countries
WHERE countries.government_form = 'Constitutional Monarchy'
	AND countries.life_expectancy > 75
	AND countries.capital > 200;
/*
7. What query would you run to get all the cities of Argentina inside the Buenos Aires district and have the population greater than 500, 000? 
The query should return the Country Name, City Name, District and Population. (2)
*/
SELECT countries.name, cities.name, cities.district, cities.population
FROM countries
	JOIN cities ON countries.id = cities.country_id
WHERE countries.name = 'Argentina'
	AND cities.district = 'Buenos Aires'
	AND cities.population > 500000;
/*
8. What query would you run to summarize the number of countries in each region? 
The query should display the name of the region and the number of countries. 
Also, the query should arrange the result by the number of countries in descending order. (2)
*/
SELECT countries.region, COUNT(countries.id) AS num_countries
FROM countries
GROUP BY countries.region
ORDER BY num_countries DESC;