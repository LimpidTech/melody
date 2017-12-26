bin/melody.pex: bin/tox
	tox package

bin/tox:
	pex tox -c tox -o $@

clean:
	rm bin/tox

.PHONY: clean
