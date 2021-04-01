# zeek-sanitize

A Python script to sanitize Zeek logs.

## Usage

sanitize.py &lt;salt value> &lt;field list, comma delimited>

Such as:

cat conn.log | zeek-cut | python sanitize.py mysalt 2,4

```
$ gunzip -c /usr/local/zeek/logs/2021-03-31/conn.08\:53\:31-09\:00\:00.log.gz | zeek-cut | python sanitize.py makethisreallylongandhardtoguessorthehashcanbereversed 2,4
1617195206.877965	CV2G122dMtlNo3Rgv3	REDACTED-7636a2a15e	61584	REDACTED-ad8b9fc128	53	tcp	-	0.001868	36	0	SH	T	T	0	SADF	5	248	0	0	-
1617195208.313508	CiGr4JlEgsxOUYMOb	REDACTED-7636a2a15e	61585	REDACTED-20e2efb3f9	443	tcp	ssl	0.332086	644	0	OTH	T	F	0	SADFR	8	976	0	0	-
1617195208.570164	CReLnb2aY5DOKCMWde	REDACTED-7636a2a15e	49319	REDACTED-20e2efb3f9	443	tcp	-	0.078987	0	0	SH	T	F	0	FA	2	80	0	0	-
1617195208.570410	CAJ3YR8nOCnyuqe5b	REDACTED-7636a2a15e	61586	REDACTED-20e2efb3f9	443	tcp	ssl	2.631273	4974	0	S0	T	F	0	SAD	20	5786	0	0	-
1617195209.624320	CBfKJH3pgyAdQe096j	REDACTED-7636a2a15e	61587	REDACTED-20e2efb3f9	443	tcp	ssl	0.358553	644	0	OTH	T	F	0	SADFR	8	976	0	0	-
1617195210.388744	CX71x135MpsFYRfDYk	REDACTED-7636a2a15e	61588	REDACTED-20e2efb3f9	443	tcp	ssl	0.345588	644	0	OTH	T	F	0	SADFR	8	976	0	0	-
```

## License

Creative Commons BY-SA

https://creativecommons.org/licenses/by-sa/4.0/

https://creativecommons.org/licenses/by-sa/4.0/legalcode
