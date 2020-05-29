drop table if exists usac.unserved_4;
create table usac.unserved_4 as
	select statefp10, geom from form_477_201906.unserved_tx;
insert into usac.unserved_4
	select statefp10, geom from form_477_201906.unserved_ok;
insert into usac.unserved_4
	select statefp10, geom from form_477_201906.unserved_ks;
insert into usac.unserved_4
	select statefp10, geom from form_477_201906.unserved_mo;	
insert into usac.unserved_4
	select statefp10, geom from form_477_201906.unserved_ar;	
insert into usac.unserved_4
	select statefp10, geom from form_477_201906.unserved_la;

alter table usac.unserved_4 add column gid serial not null;
alter table usac.unserved_4 add constraint usac_unserved_4_pkey_gid primary key (gid);
ALTER TABLE usac.unserved_4 ALTER COLUMN geom TYPE geometry(Polygon, 4269) USING ST_SetSRID(geom,4269);

--to ensure a low zoom scale in MB, insert a tiny polygon across the sea
insert into usac.unserved_4
	(statefp10, geom)
	select statefp10, (st_dump(geom)).geom
		from form_477_201906.block_66_2018
		order by st_area(geom) 
		limit 1;
	
	