import responder
import vm5808h
import pjlink

api = responder.API()


@api.route("/")
def hello_world(req, resp):
    resp.text = "hello, world!"


@api.route("/hdmi_msw/version")
def get_version(req, resp):
    resp.media = vm5808h.check_version()


@api.route("/hdmi_msw/in/{input_port}/out/{output_port}")
def switch_port(req, resp, *, input_port, output_port):
    resp.media = vm5808h.switch_port(input_port="{:0>2}".format(input_port), output_port="{:0>2}".format(output_port))


@api.route("/pj/{logical_projector_name}/power/status")
def get_projector_power_status(req, resp, *, logical_projector_name):
    resp.media = pjlink.get_power_status(pjlink.get_physical_projector_data_from_logical_name(logical_projector_name))


@api.route("/pj/{logical_projector_name}/power/on")
def set_projector_power_on(req, resp, *, logical_projector_name):
    resp.media = pjlink.set_power_on(pjlink.get_physical_projector_data_from_logical_name(logical_projector_name))


@api.route("/pj/{logical_projector_name}/power/off")
def set_projector_power_off(req, resp, *, logical_projector_name):
    resp.media = pjlink.set_power_off(pjlink.get_physical_projector_data_from_logical_name(logical_projector_name))


@api.route("/macro/wivia")
def macro_wivia(req, resp):
    resp.media = [
        pjlink.set_power_on(pjlink.get_physical_projector_data_from_logical_name("PJ1")),
        pjlink.set_power_on(pjlink.get_physical_projector_data_from_logical_name("PJ2")),
        pjlink.set_power_on(pjlink.get_physical_projector_data_from_logical_name("PJ3")),
        vm5808h.switch_port(input_port="01", output_port="01"),
        vm5808h.switch_port(input_port="02", output_port="02"),
        vm5808h.switch_port(input_port="03", output_port="03")
    ]


@api.route("/macro/bd")
def macro_bd(req, resp):
    resp.media = [
        pjlink.set_power_on(pjlink.get_physical_projector_data_from_logical_name("PJ1")),
        pjlink.set_power_on(pjlink.get_physical_projector_data_from_logical_name("PJ2")),
        pjlink.set_power_on(pjlink.get_physical_projector_data_from_logical_name("PJ3")),
        vm5808h.switch_port(input_port="07", output_port="01"),
        vm5808h.switch_port(input_port="07", output_port="02"),
        vm5808h.switch_port(input_port="07", output_port="03")
    ]


@api.route("/macro/ext_hdmi_each")
def macro_ext_hdmi_each(req, resp):
    resp.media = [
        pjlink.set_power_on(pjlink.get_physical_projector_data_from_logical_name("PJ1")),
        pjlink.set_power_on(pjlink.get_physical_projector_data_from_logical_name("PJ2")),
        pjlink.set_power_on(pjlink.get_physical_projector_data_from_logical_name("PJ3")),
        vm5808h.switch_port(input_port="04", output_port="01"),
        vm5808h.switch_port(input_port="05", output_port="02"),
        vm5808h.switch_port(input_port="06", output_port="03")
    ]


@api.route("/macro/ext_hdmi_3")
def macro_ext_hdmi_3(req, resp):
    resp.media = [
        pjlink.set_power_on(pjlink.get_physical_projector_data_from_logical_name("PJ1")),
        pjlink.set_power_on(pjlink.get_physical_projector_data_from_logical_name("PJ2")),
        pjlink.set_power_on(pjlink.get_physical_projector_data_from_logical_name("PJ3")),
        vm5808h.switch_port(input_port="06", output_port="01"),
        vm5808h.switch_port(input_port="06", output_port="02"),
        vm5808h.switch_port(input_port="06", output_port="03")
    ]


@api.route("/macro/off")
def macro_off(req, resp):
    resp.media = [
        pjlink.set_power_off(pjlink.get_physical_projector_data_from_logical_name("PJ1")),
        pjlink.set_power_off(pjlink.get_physical_projector_data_from_logical_name("PJ2")),
        pjlink.set_power_off(pjlink.get_physical_projector_data_from_logical_name("PJ3"))
    ]


if __name__ == '__main__':
    api.run()
