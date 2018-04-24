SELECT Monthname(charged_datetime) as Month, sum(amount) as Total
from billing
WHERE YEAR(charged_datetime) = 2012 and MONTH(charged_datetime) = 03;

SELECT client_id, sum(amount) as Total
from billing
WHERE client_id = 2;

SELECT client_id, domain_name as sites
FROM sites
WHERE client_id = 10;

SELECT client_id, count(domain_name) as Total_Site, Monthname(created_datetime) as Month_Created, Year(created_datetime) as Year_Created
from sites
WHERE client_id = 20
GROUP BY domain_name;


SELECT domain_name, count(leads_id) as Total_lead, date_format(registered_datetime, "%M %e, %Y") as date_created
from leads
JOIN sites on leads.site_id = sites.site_id
WHERE date(registered_datetime) between date("2011/01/01")and date("2011/02/15")
GROUP by domain_name;

Select Concat(clients.first_name, " ", clients.last_name) as Name, count(leads_id) as Total_Lead
from clients
Left JOIN sites on clients.client_id = sites.client_id
Left Join leads on sites.site_id = leads.site_id
Where date(leads.registered_datetime) between date("2011/01/01")and date("2011/12/31")
Group By Name;

SELECT Concat(clients.first_name, " ", clients.last_name) as Name, count(leads.leads_id) as Total_Lead, DATE_FORMAT(leads.registered_datetime,"%M") as Month
from clients
JOIN sites on clients.client_id = sites.client_id
Join leads on sites.site_id = leads.site_id
Where date(leads.registered_datetime) between date("2011/1/1")and date("2011/6/30")
Group By Month, Name;

SELECT Concat(clients.first_name, " ", clients.last_name) as Name, sites.domain_name as website, count(leads.leads_id) as Total_Lead, date_format(leads.registered_datetime, "%M %e, %Y") as date_generated
from clients
JOIN sites on clients.client_id = sites.client_id
Join leads on sites.site_id = leads.site_id
Where date(leads.registered_datetime) between date("2011/1/1") and date("2011/12/31")
GROUP BY website
Order by clients.client_id;

SELECT Concat(clients.first_name, " ", clients.last_name) as Name, sites.domain_name as website, count(leads.leads_id) as number_of_lead
from clients
JOIN sites on clients.client_id = sites.client_id
JOIN leads on sites.site_id = leads.site_id
GROUP BY website;

SELECT Concat(clients.first_name, " ", clients.last_name) as Name, sum(amount) as Total_Amount, Monthname(billing.charged_datetime) as Month, Year(billing.charged_datetime) as Year
from billing
Join clients on billing.client_id = clients.client_id
Group By NAME, Month, Year
order by billing.client_id, Year, Month;

SELECT Concat(clients.first_name, " ", clients.last_name) as Name, group_concat(sites.domain_name, " / ")
from clients
JOIN sites on clients.client_id = sites.client_id
group by clients.client_id














