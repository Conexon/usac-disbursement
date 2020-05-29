--add and populate the costs data
alter table usac.sac drop column if exists high_cost;
alter table usac.sac add column high_cost money;
update usac.sac set high_cost = high_cost.high_cost
	from 
	(
		select sac, sum(hcl+hcm+ias+icls+lss+sna+svs) as high_cost
		from usac.disbursement
		where year in ('2015','2016','2017','2018','2019','2020')
		group by sac
		order by sac
	) as high_cost
	where sac.sac=high_cost.sac;

alter table usac.sac drop column if exists caf;
alter table usac.sac add column caf money;
update usac.sac set caf = caf.caf
	from 
	(
		select sac, sum(fhcs+incs+icc+mobility_1+cacm+rbe+acam+bls+ak_plan+caf2_auc+pr_mobile+usvi_mobile+acam_2) as caf
		from usac.disbursement
		where year in ('2015','2016','2017','2018','2019','2020')
		group by sac
		order by sac
	) as caf
	where sac.sac=caf.sac;

alter table usac.sac drop column if exists total;
alter table usac.sac add column total money;
update usac.sac set total = high_cost + caf;

select sac, high_cost, caf, total
	from usac.sac
	order by sac
	
