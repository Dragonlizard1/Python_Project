SELECT CountryCode,Percentage,Language
FROM countrylanguage
WHERE Language LIKE "%Slovene"
ORDER BY Percentage DESC;

SELECT country.name, count(CountryCode) as cities
FROM city
JOIN country on  country.Code =city.CountryCode
GROUP BY CountryCode
ORDER BY count(CountryCode) DESC;

SELECT city.name, city.Population
FROM city
JOIN country on  country.Code =city.CountryCode
WHERE (city.Population > 500000) and (country.name = "Mexico")
ORDER BY Population DESC;

SELECT country.name, countrylanguage.Language, countrylanguage.Percentage
FROM countrylanguage
JOIN country on  country.Code = countrylanguage.CountryCode
WHERE countrylanguage.Percentage > 89
ORDER BY Percentage DESC;

SELECT Name, SurfaceArea, Population
FROM country
WHERE (SurfaceArea < 501) and Population > (100000);

SELECT name, GovernmentForm, Capital, LifeExpectancy
FROM country
WHERE (GovernmentForm LIKE "Constitutional Monarchy") and (Capital > 200) and (LifeExpectancy > 75);

SELECT country.Name, city.Name, city.District, city.Population
FROM city
JOIN country on country.Code =city.CountryCode
WHERE (city.District LIKE "Buenos Aires") and (city.Population > 500000);

SELECT Region, count(name) as countries
FROM country
GROUP BY Region
ORDER BY countries DESC;












