#!/bin/bash

find . -type d -name '*_*' | sed 's/^\.\///' | awk 'BEGIN{FS="_"}{print $NF,$1}' | sort >tmp
n=`wc -l tmp | cut -d' ' -f1`
paste <(seq 1 $n) <(cat tmp) >tmp2
while read l; do
    read -ra s <<< "$l"
    i=${s[0]}
    ln=`echo ${s[1]} | awk '{print tolower($0)}'`
    fn=`echo ${s[2]} | awk '{print tolower($0)}'`
    w=`grep ^weight: ${fn}_${ln}/_index.md`
    echo -e "${fn}\t${ln}\t${w} -> ${i}"
    sed -i "s/$w/weight: $i/" ${fn}_${ln}/_index.md
done <tmp2

rm tmp tmp2

