bin/metanic.pex: bin/tox
	tox -e package

bin/tox:
	pex tox -c tox -o $@

clean:
	rm bin/tox

.PHONY: clean
