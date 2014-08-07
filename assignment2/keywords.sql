select docid, sum(count) from
(SELECT docid, count from frequency where term = 'washington'
UNION
SELECT  docid, count from frequency where term ='taxes' 
UNION 
SELECT docid, count from frequency where term = 'treasury') as tbl group by docid order by sum(count) desc ;