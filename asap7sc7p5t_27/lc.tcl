#Read all liberty files to a TCL list my_lib.
set my_lib [glob ./LIB/CCS/asap7sc7p5t_*]
#Interate over each .lib of list to read and write a .db file.
foreach ele $my_lib {
set lwr_idx [string last / $ele]
set upr_idx [string last .lib $ele]
set str [string range $ele [expr $lwr_idx + 1] [expr $upr_idx - 1]]
echo "$str"
read_lib $ele
write_lib $str -format db -output ./DB/CCS/${str}.db
}
