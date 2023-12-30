
{ printf "[\n"; sed "s/.\{17\}/&\n/g" file.txt | sed 's/./&", "/g' | sed 's/, "$/],/g' | sed 's/^/["/g' | sed '$s/.$//g'; printf "]\n"; } > file1.txt


printf "[\n"; sed -e "s/.\{17\}/&\n/g" file.txt | sed "s/./& /g" | sed 's/ /", "/g' | sed 's/, "$/],/g' | sed 's/^/["/g' | sed '$ s/.$//'; printf "]\n"
