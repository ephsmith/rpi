DEST_DIR = $(HOME)/dev

dev/examples:
	mkdir -p $(DEST_DIR)
	rsync -rupE arm $(DEST_DIR)
	rsync -rupE lcd $(DEST_DIR)
	cp hex_switch.py $(DEST_DIR)

.PHONY: dev/examples
