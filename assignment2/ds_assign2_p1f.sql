select f.docid, f.term from frequency f , (select docid, term from frequency where term = 'transactions') as tbl where 
f.docid = tbl.docid and f.term = 'world';
