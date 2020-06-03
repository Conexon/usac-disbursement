#bl_import.sh
#shell script
#import place shape files
db=fcc
schema=form_477_201906
echo "Today is $(date)"

rm *.shp
rm *.xml
rm *.dbf
rm *.prj
rm *.shx

for i in *.zip
do
file=${i:0:21} 
cty=${i:8:2}  #get the state fips id
echo i is $i
echo file is $file
echo cty is $cty
unzip $i -d ./

#load to db
shp2pgsql -s 4269 -D -I -W latin1 -g geom $file'.shp' $schema.'block_'$cty'_2018' | psql -p 5432 -h localhost $db 

rm *.cpg
rm *.shp
rm *.xml
rm *.dbf
rm *.prj
rm *.shx

done
