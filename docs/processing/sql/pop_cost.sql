--pop_costs.sql

-- updates the sac_year table for export to mapbox for showing in the `unbroadband map`
--	this table is the clicable event for all the dollar disbursement amounts
--add and populate the costs data

--EDIT the output table name throughout this script

--first create the output table 
--	change the output name based on the year
--	make sure the table has a primary key

drop table if exists usac.sac_2021;
create table usac.sac_2021 as
	select *
		from usac.sac
	;
alter table usac.sac_2021 add constraint usac_sac_2021_gid_pkey primary key (gid);


--initialize output field high_cost
-- populate output field hight_cost
alter table usac.sac_2021 drop column if exists high_cost;
alter table usac.sac_2021 add column high_cost money;
update usac.sac_2021 set high_cost = high_cost.high_cost
	from 
	(
		--select sac, sum(hcl+hcm+ias+icls+lss+sna+svs) as high_cost
		select sac, sum(amount_disbursed) as high_cost
		from usac.disbursed
		where year_disbursed > 2014 -- in ('2015','2016','2017','2018','2019','2020')
		and fund_type in 
		(
			'HCL', 'HCM', 'IAS', 'ICLS', 'LSS', 'SNA', 'SVS'
			)
		--and sac = '225192' -- used for testing
		group by sac
		order by sac
	) as high_cost
	where sac_2021.sac=high_cost.sac;

--initialize output field caf
-- populate output field caf
alter table usac.sac_2021 drop column if exists caf;
alter table usac.sac_2021 add column caf money;
update usac.sac_2021 set caf = caf.caf
	from 
	(
		-- select sac, sum(fhcs+incs+icc+mobility_1+cacm+rbe+acam+bls+ak_plan+caf2_auc+pr_mobile+usvi_mobile+acam_2) as caf
		-- missing - incs
		select sac, sum(amount_disbursed) as caf
		from usac.disbursed
		where year_disbursed > 2014 --in ('2015','2016','2017','2018','2019','2020')
		and fund_type in
		(
			'FHCS', 'ICC', 'Mobility I', 'CACM', 'RBE', 'ACAM', 'BLS', 
			'AK PLAN', 'CAFII AUC', 'PR Mobile', 'USVI Mobile', 'ACAM_II'
			)
		--and sac = '255181' -- used for testing
		group by sac
		order by sac
	) as caf
	where sac_2021.sac=caf.sac;


--initialize output field total
-- populate output field total
alter table usac.sac_2021 drop column if exists total;
alter table usac.sac_2021 add column total money;
update usac.sac_2021 set total = high_cost + caf;

select sac, high_cost, caf, total, *
select sac, co_lower, co_name, high_cost, caf, source
	from usac.sac_2021
	order by sac
	
--test older version
select sac.state_abbv, sac.sac, sac.high_cost, sac.caf, sac.total, 
		sac_2021.high_cost, sac_2021.caf, sac_2021.total,
		sac_2021.total - sac.total as diff
	from usac.sac, usac.sac_2021
	where sac.sac = sac_2021.sac
	--and sac.high_cost is not null
	--and sac_2021.total - sac.total > '$0'
	order by diff desc
