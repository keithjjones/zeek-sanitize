# zeek-sanitize

A Python script to sanitize Zeek logs.  This is meant to be simple
so that it can be easily copied up to sensors through even a
cut/paste in an SSH session.  The Python libraries this script
references are built in, so nothing extra needs to be installed.

The strength of your redaction lies in the complexity of the salt you choose.

## Usage

sanitize.py _&lt;field list, comma delimited with no spaces>_

Such as:

cat conn.log | zeek-cut | python sanitize.py mysalt 2,4

```
$ zcat conn.08\:53\:31-09\:00\:00.log.gz | zeek-cut | python sanitize.py 2,4
1617195206.877965	CV2G122dMtlNo3Rgv3	REDACTED-1	61584	REDACTED-2	53	tcp	-	0.001868	36	0	SH	T	T	0	SADF	5	248	0	0	-
1617195208.313508	CiGr4JlEgsxOUYMOb	REDACTED-1	61585	REDACTED-3	443	tcp	ssl	0.332086	644	0	OTH	T	F	0	SADFR	8	976	0	0	-
1617195208.570164	CReLnb2aY5DOKCMWde	REDACTED-1	49319	REDACTED-3	443	tcp	-	0.078987	0	0	SH	T	F	0	FA	2	80	0	0	-
1617195208.570410	CAJ3YR8nOCnyuqe5b	REDACTED-1	61586	REDACTED-3	443	tcp	ssl	2.631273	4974	0	S0	T	F	0	SAD	20	5786	0	0	-
1617195209.624320	CBfKJH3pgyAdQe096j	REDACTED-1	61587	REDACTED-3	443	tcp	ssl	0.358553	644	0	OTH	T	F	0	SADFR	8	976	0	0	-
1617195210.388744	CX71x135MpsFYRfDYk	REDACTED-1	61588	REDACTED-3	443	tcp	ssl	0.345588	644	0	OTH	T	F	0	SADFR	8	976	0	0	-
```

## License

Creative Commons BY-SA

https://creativecommons.org/licenses/by-sa/4.0/

https://creativecommons.org/licenses/by-sa/4.0/legalcode
