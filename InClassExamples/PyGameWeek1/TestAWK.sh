#!/bin/sh

awk '
BEGIN { print "File\tOwner"}
{ print $9, "\t", $3}
END { print " - Done -" }
'
