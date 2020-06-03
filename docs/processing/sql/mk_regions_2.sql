drop table if exists usac.unserved_2;
create table usac.unserved_2 as
	select statefp10, geom from form_477_201906.unserved_dc;
insert into usac.unserved_2
	select statefp10, geom from form_477_201906.unserved_wv;
insert into usac.unserved_2
	select statefp10, geom from form_477_201906.unserved_va;
insert into usac.unserved_2
	select statefp10, geom from form_477_201906.unserved_ky;	
insert into usac.unserved_2
	select statefp10, geom from form_477_201906.unserved_tn;	
insert into usac.unserved_2
	select statefp10, geom from form_477_201906.unserved_nc;
insert into usac.unserved_2
	select statefp10, geom from form_477_201906.unserved_ms;
insert into usac.unserved_2
	select statefp10, geom from form_477_201906.unserved_al;
insert into usac.unserved_2
	select statefp10, geom from form_477_201906.unserved_ga;
insert into usac.unserved_2
	select statefp10, geom from form_477_201906.unserved_sc;
insert into usac.unserved_2
	select statefp10, geom from form_477_201906.unserved_fl;
	

alter table usac.unserved_2 add column gid serial not null;
alter table usac.unserved_2 add constraint usac_unserved_2_pkey_gid primary key (gid);
ALTER TABLE usac.unserved_2 ALTER COLUMN geom TYPE geometry(Polygon, 4269) USING ST_SetSRID(geom,4269);

--to ensure a low zoom scale in MB, insert a tiny polygon across the sea
insert into usac.unserved_2
	(statefp10, geom)
	select statefp10, (st_dump(geom)).geom
		from form_477_201906.block_66_2018
		order by st_area(geom) 
		limit 1;
	
	