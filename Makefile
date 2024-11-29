all:
	make -k -C template
	make -k -C vorlage
	make -k -C V01
	make -k -C V16
	make -k -C V44
	make -k -C V61

template:
	make -C template

vorlage:
	make -C vorlage

V01:
	make -C V01

V16:
	make -C V16

V44:
	make -C V44

V61:
	make -C V61

clean:
	make -k -C template clean
	make -k -C vorlage clean
	make -k -C V01 clean
	make -k -C V16 clean
	make -k -C V44 clean
	make -k -C V61 clean

.PHONY: clean template vorlage V01 V16 V44 V61
