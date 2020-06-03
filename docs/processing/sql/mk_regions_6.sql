drop table if exists usac.unserved_6;
create table usac.unserved_6 as
	select statefp10, geom from form_477_201906.unserved_wa;
insert into usac.unserved_6
	select statefp10, geom from form_477_201906.unserved_or;
insert into usac.unserved_6
	select statefp10, geom from form_477_201906.unserved_id;
insert into usac.unserved_6
	select statefp10, geom from form_477_201906.unserved_ca;	
insert into usac.unserved_6
	select statefp10, geom from form_477_201906.unserved_nv;
insert into usac.unserved_6
	select statefp10, geom from form_477_201906.unserved_hi;
insert into usac.unserved_6
	select statefp10, geom from form_477_201906.unserved_ak;	

alter table usac.unserved_6 add column gid serial not null;
alter table usac.unserved_6 add constraint usac_unserved_6_pkey_gid primary key (gid);
ALTER TABLE usac.unserved_6 ALTER COLUMN geom TYPE geometry(Polygon, 4269) USING ST_SetSRID(geom,4269);

--to ensure a low zoom scale in MB, insert a tiny polygon across the sea
insert into usac.unserved_6
	(statefp10, geom)
	select statefp10, (st_dump(geom)).geom
		from form_477_201906.block_66_2018
		order by st_area(geom) 
		limit 1;	
	