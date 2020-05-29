

drop table if exists usac.disbursement;
create table usac.disbursement 
(
	State character varying (2),
	id_498 character varying(9), 
	sac character varying(6),
	sac_name character varying,
	hcl money, 
	hcm money, 
	ias money,
	icls money, 
	lss money, 
	sna money,
	svs money, 
	fhcs money,
	incs money,
	icc money,
	mobility_1 money,
	cacm money,
	rbe money,
	acam money,
	bls money,
	ak_plan money,
	caf2_auc money,
	pr_mobile money,
	usvi_mobile money,
	acam_2 money,
	year integer,
	month character varying(3)
);

copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/ak.csv'
	csv header delimiter '	';
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/al.csv'
	csv header delimiter '	';	
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/an.csv'
	csv header delimiter '	';
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/ar.csv'
	csv header delimiter '	';
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/as.csv'
	csv header delimiter '	';
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/az.csv'
	csv header delimiter '	';
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/ca.csv'
	csv header delimiter '	';	
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/co.csv'
	csv header delimiter '	';
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/ct.csv'
	csv header delimiter '	';
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/dc.csv'
	csv header delimiter '	';

copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/de.csv'
	csv header delimiter '	';
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/fl.csv'
	csv header delimiter '	';	
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/ga.csv'
	csv header delimiter '	';
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/gu.csv'
	csv header delimiter '	';
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/hi.csv'
	csv header delimiter '	';
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/ia.csv'
	csv header delimiter '	';
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/id.csv'
	csv header delimiter '	';	
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/il.csv'
	csv header delimiter '	';
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/in.csv'
	csv header delimiter '	';
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/ks.csv'
	csv header delimiter '	';

copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/ky.csv'
	csv header delimiter '	';
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/la.csv'
	csv header delimiter '	';	
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/ma.csv'
	csv header delimiter '	';
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/md.csv'
	csv header delimiter '	';
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/me.csv'
	csv header delimiter '	';
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/mi.csv'
	csv header delimiter '	';
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/mn.csv'
	csv header delimiter '	';	
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/mo.csv'
	csv header delimiter '	';
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/mp.csv'
	csv header delimiter '	';
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/ms.csv'
	csv header delimiter '	';

copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/mt.csv'
	csv header delimiter '	';
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/nc.csv'
	csv header delimiter '	';	
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/nd.csv'
	csv header delimiter '	';
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/ne.csv'
	csv header delimiter '	';
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/nh.csv'
	csv header delimiter '	';
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/nj.csv'
	csv header delimiter '	';
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/nm.csv'
	csv header delimiter '	';	
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/nv.csv'
	csv header delimiter '	';
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/ny.csv'
	csv header delimiter '	';
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/oh.csv'
	csv header delimiter '	';
	
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/ok.csv'
	csv header delimiter '	';
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/or.csv'
	csv header delimiter '	';	
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/pa.csv'
	csv header delimiter '	';
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/pr.csv'
	csv header delimiter '	';
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/ri.csv'
	csv header delimiter '	';
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/sc.csv'
	csv header delimiter '	';
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/sd.csv'
	csv header delimiter '	';	
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/tn.csv'
	csv header delimiter '	';
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/tx.csv'
	csv header delimiter '	';
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/ut.csv'
	csv header delimiter '	';
	
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/va.csv'
	csv header delimiter '	';
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/vi.csv'
	csv header delimiter '	';	
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/vt.csv'
	csv header delimiter '	';
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/wa.csv'
	csv header delimiter '	';
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/wi.csv'
	csv header delimiter '	';
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/wv.csv'
	csv header delimiter '	';
copy usac.disbursement from '/Users/mike/Documents/Data/USAC/disbursement/csv/wy.csv'
	csv header delimiter '	';	


select state, count(*) 
	from usac.disbursement 
	group by state
	order by state;


