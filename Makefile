ENDPOINT := http://localhost:5042

wivia:
	curl $(ENDPOINT)/pj/PJ1/power/on; echo
	curl $(ENDPOINT)/pj/PJ2/power/on; echo
	curl $(ENDPOINT)/pj/PJ3/power/on; echo
	curl $(ENDPOINT)/hdmi_msw/in/1/out/1; echo
	curl $(ENDPOINT)/hdmi_msw/in/2/out/2; echo
	curl $(ENDPOINT)/hdmi_msw/in/3/out/3; echo

macro-wivia:
	curl $(ENDPOINT)/macro/wivia; echo

bd:
	curl $(ENDPOINT)/pj/PJ1/power/on; echo
	curl $(ENDPOINT)/pj/PJ2/power/on; echo
	curl $(ENDPOINT)/pj/PJ3/power/on; echo
	curl $(ENDPOINT)/hdmi_msw/in/7/out/1; echo
	curl $(ENDPOINT)/hdmi_msw/in/7/out/2; echo
	curl $(ENDPOINT)/hdmi_msw/in/7/out/3; echo

macro-bd:
	curl $(ENDPOINT)/macro/bd; echo

ext-hdmi-each:
	curl $(ENDPOINT)/pj/PJ1/power/on; echo
	curl $(ENDPOINT)/pj/PJ2/power/on; echo
	curl $(ENDPOINT)/pj/PJ3/power/on; echo
	curl $(ENDPOINT)/hdmi_msw/in/4/out/1; echo
	curl $(ENDPOINT)/hdmi_msw/in/5/out/2; echo
	curl $(ENDPOINT)/hdmi_msw/in/6/out/3; echo

macro-ext-hdmi-each:
	curl $(ENDPOINT)/macro/ext_hdmi_each; echo

ext-hdmi-3:
	curl $(ENDPOINT)/pj/PJ1/power/on; echo
	curl $(ENDPOINT)/pj/PJ2/power/on; echo
	curl $(ENDPOINT)/pj/PJ3/power/on; echo
	curl $(ENDPOINT)/hdmi_msw/in/6/out/1; echo
	curl $(ENDPOINT)/hdmi_msw/in/6/out/2; echo
	curl $(ENDPOINT)/hdmi_msw/in/6/out/3; echo

macro-ext-hdmi-3:
	curl $(ENDPOINT)/macro/ext_hdmi_3; echo

off:
	curl $(ENDPOINT)/pj/PJ1/power/off; echo
	curl $(ENDPOINT)/pj/PJ2/power/off; echo
	curl $(ENDPOINT)/pj/PJ3/power/off; echo

macro-off:
	curl $(ENDPOINT)/macro/off; echo