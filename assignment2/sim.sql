select sum(f1.count * f2.count) from Frequency f1, Frequency f2 where  f1.docid < f2.docid
and f1.docid = '10080_txt_crude' and f2.docid = '17035_txt_earn' and f1.term = f2.term;