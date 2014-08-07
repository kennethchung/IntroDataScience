select count(*) from (
select docid, sum(count) term_count  from frequency group by docid HAVING docid) as tbl where tbl.term_count > 300;
