drop table if exists usac.unserved_5;
create table usac.unserved_5 as
	select statefp10, geom from form_477_201906.unserved_mt;
insert into usac.unserved_5
	select statefp10, geom from form_477_201906.unserved_nd;
insert into usac.unserved_5
	select statefp10, geom from form_477_201906.unserved_sd;
insert into usac.unserved_5
	select statefp10, geom from form_477_201906.unserved_wy;	
insert into usac.unserved_5
	select statefp10, geom from form_477_201906.unserved_ne;	
insert into usac.unserved_5
	select statefp10, geom from form_477_201906.unserved_co;
insert into usac.unserved_5
	select statefp10, geom from form_477_201906.unserved_ut;	
insert into usac.unserved_5
	select statefp10, geom from form_477_201906.unserved_az;
insert into usac.unserved_5
	select statefp10, geom from form_477_201906.unserved_nm;

alter table usac.unserved_5 add column gid serial not null;
alter table usac.unserved_5 add constraint usac_unserved_5_pkey_gid primary key (gid);
ALTER TABLE usac.unserved_5 ALTER COLUMN geom TYPE geometry(Polygon, 4269) USING ST_SetSRID(geom,4269);

--to ensure a low zoom scale in MB, insert a tiny polygon across the sea
insert into usac.unserved_5
	(statefp10, geom)
	select statefp10, (st_dump(geom)).geom
		from form_477_201906.block_66_2018
		order by st_area(geom) 
		limit 1;
	
	