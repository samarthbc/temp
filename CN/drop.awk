BEGIN { c=0;
}
{
If ($1= ="d")
{
c++;
printf("%s\t%s\n",$5,$11);
}
}
/*immediately after END should open braces ‘{‘
END{
printf("The number of packets dropped =%d\n",c);
}
