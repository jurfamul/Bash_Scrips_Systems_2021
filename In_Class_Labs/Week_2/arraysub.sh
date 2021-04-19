#!/bin/bash
#declare -a QUOTEARRAY
QUOTEARRAY=("You cannot shake hands with a clenched fist." "Whoever is happy will make others happy too."
"Let us be grateful to people who make us happy." "Very little is needed to make a happy life."
"Be happy for this moment. This moment is your life.")
echo ${QUOTEARRAY[0]//happy/sloppy}
echo ${QUOTEARRAY[1]//happy/sloppy}
echo ${QUOTEARRAY[2]//happy/sloppy}
echo ${QUOTEARRAY[3]//happy/sloppy}
echo ${QUOTEARRAY[4]//happy/sloppy}
