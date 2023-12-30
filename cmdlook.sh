cat look.txt | sed 's/$/ /g' | tr -d '\n' | sed 's/ /", "/g' | sed 's/^/["/g' | sed 's/", "$/"]/g' | sed 's/$/\n/g' > diff.txt; cat diff.txt


