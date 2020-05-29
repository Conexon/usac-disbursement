drop table if exists usac.unserved_1;
create table usac.unserved_1 as
	select statefp10, geom from form_477_201906.unserved_me;  
insert into usac.unserved_1
 	select statefp10, geom from form_477_201906.unserved_nh;
insert into usac.unserved_1
 	select statefp10, geom from form_477_201906.unserved_vt;	
insert into usac.unserved_1
 	select statefp10, geom from form_477_201906.unserved_ny;	
insert into usac.unserved_1
 	select statefp10, geom from form_477_201906.unserved_ma;
insert into usac.unserved_1
	select statefp10, geom from form_477_201906.unserved_ct;
insert into usac.unserved_1
 	select statefp10, geom from form_477_201906.unserved_ri;
insert into usac.unserved_1
 	select statefp10, geom from form_477_201906.unserved_pa;
insert into usac.unserved_1
	select statefp10, geom from form_477_201906.unserved_nj;
insert into usac.unserved_1
 	select statefp10, geom from form_477_201906.unserved_de;
insert into usac.unserved_1
	select statefp10, geom from form_477_201906.unserved_md;	

alter table usac.unserved_1 add column gid serial not null;
alter table usac.unserved_1 add constraint usac_unserved_1_pkey_gid primary key (gid);
ALTER TABLE usac.unserved_1 ALTER COLUMN geom TYPE geometry(Polygon, 4269) USING ST_SetSRID(geom,4269);

--to ensure a low zoom scale in MB, insert a tiny polygon across the sea
insert into usac.unserved_1
	(statefp10, geom)
	select statefp10, (st_dump(geom)).geom
		from form_477_201906.block_66_2018
		order by st_area(geom) 
		limit 1;

	
	