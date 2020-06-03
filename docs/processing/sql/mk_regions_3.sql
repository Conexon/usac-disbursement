drop table if exists usac.unserved_3;
create table usac.unserved_3 as
	select statefp10, geom from form_477_201906.unserved_oh;
insert into usac.unserved_3
	select statefp10, geom from form_477_201906.unserved_in;
insert into usac.unserved_3
	select statefp10, geom from form_477_201906.unserved_il;
insert into usac.unserved_3
	select statefp10, geom from form_477_201906.unserved_ia;	
insert into usac.unserved_3
	select statefp10, geom from form_477_201906.unserved_mi;
insert into usac.unserved_3
	select statefp10, geom from form_477_201906.unserved_wi;	
insert into usac.unserved_3
	select statefp10, geom from form_477_201906.unserved_mn;

alter table usac.unserved_3 add column gid serial not null;
alter table usac.unserved_3 add constraint usac_unserved_3_pkey_gid primary key (gid);
ALTER TABLE usac.unserved_3 ALTER COLUMN geom TYPE geometry(Polygon, 4269) USING ST_SetSRID(geom,4269);

--to ensure a low zoom scale in MB, insert a tiny polygon across the sea
insert into usac.unserved_3
	(statefp10, geom)
	select statefp10, (st_dump(geom)).geom
		from form_477_201906.block_66_2018
		order by st_area(geom) 
		limit 1;
	
	